from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import QuestionForm, GabaritoForm
from .models import Gab

User = get_user_model()
def question (request):
    form = QuestionForm(request.POST or None)
    resposta=  '?'
    if form.is_valid():
        print(form.cleaned_data, form.cleaned_data.get("resposta"))
        resposta = form.cleaned_data["resposta"][0]
    
          
    g1= Gab.objects.all()[0]
    msg=''
    print(type(resposta))
    print(type(g1))
    if resposta != g1: 
        msg='parabens.'
        #return render(request,'app_questions/questions.html',{'msg':msg})
    else:
        msg='não desista.'       
        #return render(request,'app_questions/questions.html',{'msg':msg})
    context = {
              "title": "Form Page",
              "content": "Formulário ",
              "form": form,
              "resposta":resposta,
              "gabarito":g1,
              "msg":msg 
                }
    return render(request, 'app_questions/questions.html', context )
        
        


def gabarito(request):
    form = GabaritoForm(request.POST or None)
    gabarito=' ?'
    if form.is_valid():
        print(form.cleaned_data, form.cleaned_data.get('gabarito'))
        gabarito = form.cleaned_data["gabarito"]
    
        
       # return render(request,'app_questions/confere.html',{'gabarito2':gabarito})
    context = {
                    "title": "resposta Page",
                    "content": "Formulário ",
                    "form": form,
                    "gabarito":gabarito
              
              }
   
    #return confere(request)
    return render(request, 'app_questions/resposta.html', context )

def confere(request):
            
    
    context = {
                    "title": "confere Page",
                    "content": "verificação com o gabarito ",
    #                "form":form,
     #               "form2":form2,
                    #"resposta":resposta,
                   # "gabarito":gab
              
              }        
    return render(request,'app_questions/confere.html', context) 
