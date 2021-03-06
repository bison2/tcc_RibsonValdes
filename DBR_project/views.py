from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    print(request.session.get('cart_id','Unknow'))
      
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
    if request.user.is_authenticated:
        return redirect('/premium')
        #context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)

def premium_page(request):
    print(request.session.get('cart_id','Unknow'))
      
    context = {
                    "title": "Trabalho de conclusão de curso",
                    "content": "Estudo dos princípios do Design-Based Research -DBR e do Technologycal Pedagogical Content Knowledge- TPACK e Desenvolvimento de Sistema Web de Gestão Acadêmica ",
                    "contentdois":"Ribson Coelho Cardoch Valdés. IFB-TSI-2021. Orientadora Me. Cristiane Jorge de Lima Bonfim- IFB/CBRA."
              }
    
    return render(request, "home_premium.html", context)

def about_page(request):
    context = {
                    "title": "About Page",
                    "content": "Bem vindo a About Page"
              }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": "Contact Page",
                    "content": "Bem vindo a Contact Page",
                    "form": contact_form
                   # "brand": "Novo nome da marca"
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {     
                    "title":"LOGIN PAGE",
                    "content":"Bem vindo à pagina de Login.",
                    "form": form
              }
    print("User logged in")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(user)
        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)

def logout_page(request):
    context = {
                "content": "Você efetuou o logout com sucesso! :)"
              }
    logout(request)
    return render(request, "auth/logout.html", context)   

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {        
                    "title":"REGISTER PAGE",
                    "content":"Bem vindo à pagina de Registro.",
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)