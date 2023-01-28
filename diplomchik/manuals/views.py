from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User
from django.template.defaulttags import register

from django import template



@register.filter
def mod(fir_mul,second_mul):
    mult = fir_mul*second_mul
    return mult


@register.filter
def div(fir_div,second_div):
    divide = (fir_div / second_div)
    return divide

@register.filter
def min(fir_div,second_div):
    divide = (fir_div - second_div)
    return divide















# 1-ая страница с бозовым шаблоном
def index(request):
    #data_x = read_xlx()
    #print(data_x, type(data_x))
    klient = User.objects.all()
    name_prod = Article.objects.all().count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits +1
    bbf = BbForm()
    context = {'name_prod': name_prod,'num_visits':num_visits,'klient':klient, 'form':bbf}


    return render(request, "index.html", context=context)

# 2-ая страница для оператора
def coffins(request):
    prod_catalog = Article.objects.filter(type__type="Гроб").all()
    skid = Skidka.objects.all()
    context = {'prod_catalog':prod_catalog,'skid':skid}
    return render(request, "coffince.html", context=context)

def article_descr(request,article_id):
    skid = Skidka.objects.all()
    descr = Article.objects.get(id=article_id)
    context = {'descr':descr,'skid':skid}
    return render(request, 'article_detail.html',context=context)



def crown(request):
    crown_catalog = Article.objects.filter(type__type="Венок").all()
    skid = Skidka.objects.all()
    context = {'crown_catalog':crown_catalog,'skid':skid}
    return render(request, "crown.html", context=context)


def monuments(request):
    monuments_catalog = Article.objects.filter(type__type="Памятник").all()
    skid = Skidka.objects.all()
    context = {'monuments_catalog':monuments_catalog,'skid':skid}
    return render(request, "monument.html", context=context)

def contacts(request):
    return render(request, "contacts.html")







# Регестрация пользователей
def registration(request):
    form = Registration()
    context = {"form": form}
    if request.method == "GET":
        context.update({"mode": "GET"})
        return render(request, 'registration/registration.html', context=context)

    if request.method == "POST":
        # ловим данные из формы
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")


        # записываем нового пользователя
        user = User.objects.create_user(username,email ,password)
        user.save()


        context.update({"mode":"POST"})
        # Логика где происходит сохранение данных в Базу Данных
        return render(request, 'registration/registration.html', context=context)



# Скрыть товар

def hidden(request,article_id):
    art_hid = Article.objects.get(id=article_id)
    art_hid.display = False
    art_hid.save()
    return HttpResponseRedirect('/')