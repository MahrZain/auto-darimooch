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


# Create Views Here
def home(request):
    pr_data = products.objects.all()
    product = Paginator(pr_data, 2)
    if 'page' in request.GET:
        data = request.GET['page']
    else:
        data = page = 1 
    pg_number = product.get_page(data)
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
    }
    return render(request, "index.html", data)


def contact(request):
    return render(request, "contact.html")

def allpro(request):
    pr_data = products.objects.all()
    paginator = Paginator(products.objects.all(), 2)
    page_number = request.GET.get('page')
    pagenum = paginator.get_page(page_number)
    data = {
        'pr_data':pr_data,
        'pagenum': pagenum
    }
    print(data)
    return render(request, 'all_products_page.html', data)

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
    return render(request,"all_products_page.html",{"pr_data":pr_data})

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
        request.session['username'] = user.username
        request.session['email'] = user.email
        login(request, user)
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
    user = User.objects.create_user(first_name=first_name,username=username, email=email, password=password)
    return render(request, "register.html")


def viewproducts(request, myid):
    product = products.objects.filter(id=myid)
    return render(request, "products.html", {"product": product[0]})


def faq(request):
    return render(request, "faq.html")


def search(request):
    result = request.GET["query"]
    fresult = products.objects.filter(title__icontains=result)
    return render(request, "search.html", {"fresult": fresult})
