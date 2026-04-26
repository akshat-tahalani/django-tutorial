from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.shortcuts import redirect 
from .forms import ContactForm


def product_detail_id_redirect(request , id):
    product = get_object_or_404(product ,id= id)
    return redirect('product_detail_slug' ,slug = product.slug)

def product_list(request):
    products = Product.objects.all()
    
    # Search filtering
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            title__icontains=search_query
        ) | products.filter(
            description__icontains=search_query
        )
    
    # Category filtering
    category_name = request.GET.get('category')
    if category_name:
        products = products.filter(category__name=category_name)
    
    # Price filtering
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Filter by availability
    available_only = request.GET.get('available')
    if available_only:
        products = products.filter(is_available=True)
    
    sort_by = request.GET.get('sort', 'created_at')  # default sort
    order = request.GET.get('order', 'desc')
    
    if order == 'desc':
        products = products.order_by(f'-{sort_by}')
    else:
        products = products.order_by(sort_by)
    
    return render(request, 'list.html', {'products': products})
    
    
# rtghe point of using get object or 404 is that if object is able to be got the ngive out tthe object otherwierse give the error 404


def calculate():
    x = 1
    y = 2 
    return x

def product_detail(request ,id):
    product = get_object_or_404(Product , id=id)
    return render(request , 'products/detail.html' , {'product':product})




# Create your views here.
# aview function is a function that takes request and give response 
# so bascially its a rquest handler function

def say_hello(request):
    x = calculate()
    return render(request ,'hello.html', {'name' : 'akii'})


def product_detail_slug(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/detail.html', {'product': product})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        print(f"Name : {name}")
        print(f"Email : {email}")
        print(f"Subject : {subject}")
        print(f"Message : {message}")

        return render(request, 'contact_success.html')
    
    return render(request, 'contact.html', {'form': form})