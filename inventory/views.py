from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def display_laptops(request):
    laptops = models.Laptop.objects.all()
    return render(request, 'home.html', { 'devices': laptops, 'header': 'Laptops', 'edit': "inventory:edit_laptops", 'delete': "inventory:delete_laptops" })

def display_desktops(request):
    desktops = models.Desktop.objects.all()
    return render(request, 'home.html', { 'devices': desktops, 'header': 'Desktops', 'edit': "inventory:edit_desktops", 'delete': "inventory:delete_desktops" })

def display_mobiles(request):
    mobiles = models.Mobile.objects.all()
    return render(request, 'home.html', { 'devices': mobiles, 'header': 'Mobiles', 'edit': "inventory:edit_mobiles", 'delete': "inventory:delete_mobiles" })


def add_laptops(request):
    form = forms.AddLaptopForm()

    if request.method == "POST":
        form = forms.AddLaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_laptops')

    return render(request, 'forms.html', { 'form': form, 'action': "inventory:add_laptops" })


def add_desktops(request):
    form = forms.AddDesktopForm()

    if request.method == "POST":
        form = forms.AddDesktopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_desktops')

    return render(request, 'forms.html', { 'form': form, 'action': "inventory:add_desktops"  })


def add_mobiles(request):
    form = forms.AddMobileForm()

    if request.method == "POST":
        form = forms.AddMobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_mobiles')

    return render(request, 'forms.html', { 'form': form, 'action': "inventory:add_mobiles"  })


def edit_laptops(request, pk):
    laptop = get_object_or_404(models.Laptop, pk=pk)
    pk = laptop.id
    form = forms.AddLaptopForm(instance=laptop)

    if request.method == "POST":
        form = forms.AddLaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_laptops')

    return render(request, 'forms.html', { 'form': form, 'action': f"inventory:edit_laptops", "pk": pk })


def edit_desktops(request, pk):
    desktop = get_object_or_404(models.Desktop, pk=pk)
    pk = desktop.id
    form = forms.AddDesktopForm(instance=desktop)

    if request.method == "POST":
        form = forms.AddDesktopForm(request.POST, instance=desktop)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_desktops')

    return render(request, 'forms.html', { 'form': form, 'action': "inventory:edit_desktops", "pk": pk  })


def edit_mobiles(request, pk):
    mobile = get_object_or_404(models.Mobile, pk=pk)
    pk = mobile.id
    form = forms.AddMobileForm(instance=mobile)

    if request.method == "POST":
        form = forms.AddMobileForm(request.POST, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('inventory:display_mobiles')

    return render(request, 'forms.html', { 'form': form, 'action': "inventory:edit_mobiles", "pk": pk  })


def delete_laptops(request, pk):
    laptop = get_object_or_404(models.Laptop, pk=pk)
    laptop.delete()
    return redirect('inventory:display_laptops')

def delete_desktops(request, pk):
    desktop = get_object_or_404(models.Desktop, pk=pk)
    desktop.delete()
    return redirect('inventory:display_desktops')

def delete_mobiles(request, pk):
    mobile = get_object_or_404(models.Mobile, pk=pk)
    mobile.delete()
    return redirect('inventory:display_mobiles')