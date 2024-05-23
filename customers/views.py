from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_customer')
    else:
        form = CustomerForm()
    customers = Customer.objects.all()
    return render(request, 'customers/add_customer.html', {'form': form, 'customers': customers})
