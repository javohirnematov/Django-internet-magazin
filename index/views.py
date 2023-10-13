from django.shortcuts import render, redirect
from . import forms, models
from .handlers import bot


# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    #Отправляем данные на фронт
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    products = models.Product.objects.filter(product_category=category)
    context = {'products': products}
    return render(request, 'exact_category.html', context)

def get_exact_product(request, pk):
    product = models.Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'exact_product.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = models.Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')

def add_to_cart(request, pk):
    if request.method == 'POST':
        checker = models.Product.objects.get(id=pk)
        if checker.product_amount >= int(request.POST.get('product_amount')):
            models.Cart.objects.create(user_id=request.user.id,
                                       user_product=checker,
                                       user_product_count=int(request.POST.get('product_amount'))).save()
            return redirect('/')
        else:
            return redirect('/')

def user_cart(request):
    cart = models.Cart.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ!\n\n'
        for i in cart:
            main_text += f'Товар: {i.user_product}\n' \
                       f'Количество: {i.user_product_count}\n' \
                         f'Заказчик: {i.user_id}'
        bot.send_message(255380566, main_text)
        cart.delete()
        return redirect('/')


    context = {'cart': cart}
    return render(request, 'user_cart.html', context)

def del_from_cart(request, pk):
    product_to_delete = models.Product.objects.get(id=pk)
    models.Cart.objects.filter(user_id=request.user.id,
                               user_product=product_to_delete).delete()
    return redirect('/cart')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)
    context = {'form': form}
    return render(request, 'registration/register.html', context)

