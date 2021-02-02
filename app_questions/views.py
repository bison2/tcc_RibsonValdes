from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import QuestionForm, GabForm
from .models import Gab

User = get_user_model()
def question (request):
    form = QuestionForm(request.POST or None)

    resposta=  '?'
    gabarito='?'
    if form.is_valid():
        print(form.cleaned_data, form.cleaned_data.get("resposta"), form.cleaned_data.get("gabarito"))
        resposta = form.cleaned_data["resposta"].lower()
        gabarito = form.cleaned_data["gabarito"].lower()

          
    #g1= Gab.objects.all()[0]
    #form_gab = GabaritoForm(request.POST or None)
    #gabarito='?'
    #if form_gab.is_valid():
     #   print(form.cleaned_data, form.clean_data.get("gabarito"))
#        gabarito = form.cleaned_data["gabarito"]

    msg=''
    
    if resposta == gabarito: 
        msg='parabens.Vc acertou :-)'
        #return render(request,'app_questions/questions.html',{'msg':msg})
    else:
        msg='não desista.Tente de novo :-|  '       
        #return render(request,'app_questions/questions.html',{'msg':msg})

    print(type(resposta))
    print(type(gabarito))    
    print(msg)
    context = {
              "title": "Form Page",
              "content": "Formulário ",
              "form": form,
             # "form_gab": form_gab,
              "resposta":resposta,
              "gabarito":gabarito,
              "msg":msg 
                }
    return render(request, 'app_questions/questions.html', context )
        
        


def gabarito(request):
    form = GabForm(request.POST or None)
   # gabarito=' ?'
    gab = Gab.objects.all()
    pergunta =  '?'
    resposta ='?'
    gabarito= str(gab.first()).lower()
    if form.is_valid():
        form.save()
        #form = GabForm()
        #print(form.cleaned_data, form.cleaned_data.get('pergunta'), form.cleaned_data.get('gabarito'))
    #    gabarito = form.cleaned_data["gabarito"]


        pergunta = form.cleaned_data["pergunta"].lower()
        resposta = str(form.cleaned_data["resposta"]).lower()
        
        msg=''
    
    if resposta == gabarito: 
        msg='parabens.Vc acertou :-)'
       # return redirect('questions:confere' )
    else:
        msg='não desista.Tente de novo :-|'       
        #return redirect('questions:confere')

    print(type(pergunta))
    print(type(gabarito), gabarito)
    print(type(resposta), resposta)    
    print(msg)
       # return render(request,'app_questions/confere.html',{'gabarito2':gabarito})
    context = {
                    "title": "resposta Page",
                    "content": "Formulário ",
                    "form": form,
                    "gabarito":gabarito,
                    "msg":msg
              
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
                   # "gabarito":gabarito,
                   
              
              }        
    return render(request,'app_questions/confere.html', context) 
