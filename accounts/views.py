from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group

from .forms import RegisterForm, LoginForm
from .models import VerificationCode
from .utils import send_email_thread


# ---------------- REGISTER ----------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='user')
            user.groups.add(group)

            login(request, user)
            return redirect('phone_list')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------------- LOGIN ----------------
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request, user)
            return redirect('phone_list')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# ---------------- LOGOUT ----------------
def user_logout(request):
    logout(request)
    return redirect('login')


# ---------------- FORGOT PASSWORD ----------------
def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("username")

        user = User.objects.filter(username=username).first()

        if not user:
            return render(request, "accounts/forgot_password.html", {
                "error": "User topilmadi"
            })

        VerificationCode.objects.filter(user=user).delete()

        code_obj = VerificationCode.objects.create(user=user)

        send_email_thread(
            subject="Parolni tiklash",
            message=f"Code: {code_obj.code}",
            recipient_list=[user.email]
        )

        request.session['reset_user_id'] = user.id

        return redirect("restore_password")

    return render(request, "accounts/forgot_password.html")


# ---------------- RESTORE PASSWORD ----------------
def restore_password(request):
    if request.method == "POST":
        code = request.POST.get("code")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        user_id = request.session.get("reset_user_id")

        if not user_id:
            return redirect("forgot_password")

        user = get_object_or_404(User, id=user_id)

        # 🔥 code number emas string
        code_obj = VerificationCode.objects.filter(
            user=user,
            code=code
        ).first()

        if not code_obj:
            return render(request, "accounts/restore_password.html", {
                "error": "Code noto‘g‘ri"
            })

        if code_obj.is_expired():
            return render(request, "accounts/restore_password.html", {
                "error": "Code eskirgan"
            })

        if password != re_password:
            return render(request, "accounts/restore_password.html", {
                "error": "Parollar mos emas"
            })

        user.set_password(password)
        user.save()

        code_obj.delete()
        request.session.pop('reset_user_id', None)

        return redirect("login")

    return render(request, "accounts/restore_password.html")



