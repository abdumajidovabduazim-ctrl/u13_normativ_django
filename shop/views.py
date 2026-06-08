from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required

from accounts.utils import login_required
from .models import Phone
from .forms import PhoneForm

from rest_framework.views import APIView
from rest_framework.response import Response


def phone_list(request):
    q = request.GET.get('q')
    phones = Phone.objects.all()

    if q:
        phones = phones.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(brand__name__icontains=q)
        )

    paginator = Paginator(phones, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/phone_list.html', {
        'phones': page_obj,
        'page_obj': page_obj,
        'q': q
    })


def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    return render(request, 'shop/phone_detail.html', {
        'phone': phone
    })



@login_required
@permission_required('shop.add_phone', raise_exception=True)
def phone_create(request):
    form = PhoneForm(request.POST or None)

    if form.is_valid():
        phone = form.save(commit=False)
        phone.owner = request.user
        phone.save()
        return redirect('phone_list')

    return render(request, 'shop/phone_form.html', {
        'form': form
    })



@login_required
@permission_required('shop.change_phone', raise_exception=True)
def phone_update(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    # object-level permission (OWNER CHECK)
    if not request.user.has_perm('shop.change_phone') and phone.owner != request.user:
        return redirect('phone_list')

    form = PhoneForm(request.POST or None, instance=phone)

    if form.is_valid():
        form.save()
        return redirect('phone_list')

    return render(request, 'shop/phone_form.html', {
        'form': form
    })



@login_required
@permission_required('shop.delete_phone', raise_exception=True)
def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    # object-level permission (OWNER CHECK)
    if not request.user.has_perm('shop.delete_phone') and phone.owner != request.user:
        return redirect('phone_list')

    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')

    return render(request, 'shop/phone_confirm_delete.html', {
        'phone': phone
    })



class TestAPIView(APIView):
    def get(self, request):
        return Response({
            "message": "Hello DRF"
        })