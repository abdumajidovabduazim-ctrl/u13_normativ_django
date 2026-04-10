from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone
from .forms import PhoneForm


def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'shop/phone_list.html', {'phones': phones})


def phone_create(request):
    form = PhoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('phone_list')
    return render(request, 'shop/phone_form.html', {'form': form})


def phone_update(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    form = PhoneForm(request.POST or None, instance=phone)
    if form.is_valid():
        form.save()
        return redirect('phone_list')
    return render(request, 'shop/phone_form.html', {'form': form})


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'shop/phone_confirm_delete.html', {'phone': phone})