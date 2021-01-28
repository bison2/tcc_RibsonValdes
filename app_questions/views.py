from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import QuestionForm, GabaritoForm


User = get_user_model()
def question (request):
    form = QuestionForm(request.POST or None)
    resposta=  '?'
    if form.is_valid():
        print(form.cleaned_data, form.cleaned_data.get("resposta"))
        resposta = form.cleaned_data.get("resposta")[0]

    context = {
                    "title": "Form Page",
                    "content": "Formulário ",
                    "form": form,
                    "resposta":resposta 
              
              }
    return render(request, 'app_questions/questions.html', context )
    

def gabarito (request):
    

    form = GabaritoForm(request.POST or None)
    gabarito=' ?'
    if form.is_valid():
        print(form.cleaned_data, form.cleaned_data.get('gabarito'))
        gabarito = form.cleaned_data.get("gabarito")
    
    context = {
                    "title": "Gabarito Page",
                    "content": "verificação com o gabarito ",
                    "form": form,
                    "gabarito":gabarito
              
              }
   
    #return confere(request)
    return render(request, 'app_questions/resposta.html', context )

def confere(request):
    
    form = QuestionForm(request.POST or None)
    resposta = 'noooo' 

    if request.method == "POST":
            
        form = QuestionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data, form.cleaned_data.get("resposta"))
            resposta = form.cleaned_data["resposta"][0]
        else:
            print( 'erros')
    
    form2 = GabaritoForm()
    gabarito = 'wake up now'
    
    if request.method == "POST":
        form2 = GabaritoForm(request.POST)
        
        if form2.is_valid():
            print(form2.cleaned_data, form2.cleaned_data.get('gabarito'))
            gabarito = form2.cleaned_data["gabarito"]
        else:
            print( 'erros')

    context = {
                    "title": "confere Page",
                    "content": "verificação com o gabarito ",
                    "form":form,
                    "form2":form2,
                    "resposta":resposta,
                    "gabarito":gabarito 
              
              }        
    return render(request,'app_questions/confere.html', context) 
