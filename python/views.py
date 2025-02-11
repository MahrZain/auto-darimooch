from django.shortcuts import render, redirect
from products.models import products
from carousel.models import carousel
from banner.models import banner
from logo.models import limage
from announcement.models import Announcement
from navbar.models import nav
from contact.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django_recaptcha.fields import ReCaptchaField
import json
import os


# Create Views Here
def home(request):
    pr_data = products.objects.all()
    product = Paginator(pr_data, 2)
    if "page" in request.GET:
        data = request.GET["page"]
    else:
        data = page = 1
    pg_number = product.get_page(data)
    totalpages = [x + 1 for x in range(product.num_pages)]

    car_data = carousel.objects.all()
    sec_banner = banner.objects.all()
    latest_logo = limage.objects.all()
    msg_text = Announcement.objects.all()
    nav_bar = nav.objects.all()
    all_products = products.objects.all()
    data = {
        "products": pr_data,
        "carousel": car_data,
        "SB": sec_banner,
        "logo": latest_logo,
        "message": msg_text,
        "nav": nav_bar,
        "pg_number": pg_number,
        "totalpages": totalpages,
    }
    return render(request, "index.html", data)


def contact(request):
    return render(request, "contact.html")


# def allpro(request):
#     pr_data = products.objects.all()
#     paginator = Paginator(products.objects.all(), 2)
#     page_number = request.GET.get('page')
#     pagenum = paginator.get_page(page_number)
#     data = {
#         'pr_data':pr_data,
#         'pagenum': pagenum
#     }
#     print(data)
#     return render(request, 'all_products_page.html', data)


def savcontact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        if not email or not email or not phone or not message:
            return render(request, "contact.html")
        else:
            sav = Contact(name=name, email=email, phone=phone, message=message)
            sav.save()
    return render(request, "contact.html")


def allpro(request):
    pr_data = products.objects.all()
    return render(request, "all_products_page.html", {"pr_data": pr_data})


def search(request, mytitle):
    query = request.GET.get("searched")
    products.objects.filter(title=mytitle)
    return render(request, "")


def about(request):
    nav_bar = nav.objects.all()
    data = {
        "nav": nav_bar,
    }
    return render(request, "about.html", data)


def login_view(request):
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return render(request, "login.html")


def loginUser(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        request.session["username"] = user.username
        request.session["email"] = user.email
        login(request, user)
        messages.success(request, "Login Successfull!")
        return redirect("home")

    else:
        messages.error(request, "Login Failed! Check Username & Password!")
        return redirect("login")


def register(request):
    return render(request, "register.html")


def registerUser(request):
    first_name = request.POST["first_name"]
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(
        first_name=first_name, username=username, email=email, password=password
    )
    return render(request, "register.html")


def viewproducts(request, slug):
    product = products.objects.filter(new_slug=slug)
    return render(request, "products.html", {"product": product[0], "slug": slug})


def faq(request):
    return render(request, "faq.html")


def search(request):

    result = request.GET["query"]
    if result == "":
        return redirect("home")
    fresult = products.objects.filter(title__icontains=result)
    if not fresult:
        messages.error(request, "Nothing Found!")
        return render(request, "search.html", {"result": result})
    else:
        return render(request, "search.html", {"fresult": fresult, "result": result})


def smtp(request):
    email = request.GET["news_email"]
    send_mail(
        "News Letter For DariMooch",
        f"Hi this Email:  { email }   Want To Subscribe For Your News Letter. -- form DariMooch",
        "info@nullxcoder.xyz",
        ["nullxcoder0@gmail.com"],
        fail_silently=False,
    )
    return redirect("home")


def complaint(request):
    return render(request, "complaint.html")


def submit_complaint(request):
    if request.method == 'POST':
        email = request.POST["email"]
        complain = request.POST["complain"]
        
        #Recaptcha Stuff
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LdG8xoqAAAAAP4IU6KwAJIIuQiuJgiU3BcJiGUB'
        captchaData = {
            'secret': secretkey,
            'response':clientkey
        }
        r = request.POST('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        print('hello')
    return render(request, "complaint.html")
