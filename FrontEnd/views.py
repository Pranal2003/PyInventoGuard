from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    items = Product.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    cars_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user

            # Check if order quantity is greater than available quantity
            product = instance.product
            if instance.order_quantity > product.quantity:
                # Order cannot be fulfilled, add error to the specific field
                form.add_error('order_quantity', 'Order quantity exceeds available quantity.')
            else:
                instance.save()

                # Update product quantity
                product.quantity -= instance.order_quantity
                product.save()

                return redirect('dashboard-index')
    else:
        form = OrderForm()

    context = {
        'items': items,
        'order': orders,
        'form': form,
        'product': products,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'cars_count': cars_count,
    }
    return render(request, 'dashboard/index.html', context)
@login_required(login_url='user-login')
def cars(request):
    items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM table frontend_product wher')
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    cars_count = items.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-cars')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'cars_count': cars_count,
    }
    return render(request, 'dashboard/cars.html',context)

def cars_delete(request,pk):
    items = Product.objects.get(id=pk)
    if request.method=='POST':
        items.delete()
        return redirect('dashboard-cars')
    return render(request,'dashboard/cars_delete.html')

def cars_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=item)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('dashboard-cars')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/cars_update.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    cars_count = Product.objects.all().count()
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'orders_count':orders_count,
        'cars_count':cars_count,
    }
    return render(request, 'dashboard/staff.html' , context)
def staff_details(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers' : workers,
    }
    return render(request,'dashboard/staff-details.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    cars_count = Product.objects.all().count()
    context = {
        'orders' : orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'cars_count':cars_count,
    }
    return render(request, 'dashboard/order.html',context)