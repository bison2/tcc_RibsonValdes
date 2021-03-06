from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import GabForm, QuestionForm
from .models import Gab, GabManager

User = get_user_model()
def question(request):
#    form = QuestionForm(request.POST or None)
 #   resposta=  '?'
  #  gabarito='?'
   # if form.is_valid():
    #    print(form.cleaned_data, form.cleaned_data.get("resposta"), form.cleaned_data.get("gabarito"))
     #   resposta = form.cleaned_data["resposta"].lower()
      #  gabarito = form.cleaned_data["gabarito"].lower()

          
    #g1= Gab.objects.all()[0]
    #form_gab = GabaritoForm(request.POST or None)
    #gabarito='?'
    #if form_gab.is_valid():
     #   print(form.cleaned_data, form.clean_data.get("gabarito"))
#        gabarito = form.cleaned_data["gabarito"]

    gab = Gab.objects.all()
            
    user=request.user
    
    alternativa='?alternativa?'
    alternativa2='?alternativa2?'
    resposta ='?resposta?'
    #gabarito= str(gab.first()).lower()


    form = GabForm(request.POST or None)
   # gabarito=' ?'
    if form.is_valid():
        resposta = str(form.cleaned_data["resposta"]).upper()
        alternativa = str(form.cleaned_data["alternativa"]).upper()
        alternativa2 = str(form.cleaned_data["alternativa2"]).upper()
               
    #msg=''
    #
    #if resposta == gabarito: 
     #   msg='parabens.Vc acertou :-)'
        #return render(request,'app_questions/questions.html',{'msg':msg})
    #else:
     #   msg='não desista.Tente de novo :-|  '       
        #return render(request,'app_questions/questions.html',{'msg':msg})
    print(request.user)
    print(type(resposta), resposta)
    
    #print(type(gabarito), gabarito)    
    #print(msg)
    print(type(alternativa), alternativa)
    print(type(alternativa2), alternativa2)
    context = {
              "title": "Form Page",
              "content": "Formulário ",
              "form": form,
              "alternativa":alternativa,
              "alternativa2":alternativa2,
              "resposta":resposta,
    
     #         "gabarito":gabarito,
      #        "msg":msg,
              "gab":gab
                }
    return render(request, 'app_questions/questions.html', context )
        
        


def gabarito(request, id):
    #gab = Gab.objects.filter(id=1).values_list('gabarito', flat=True)
    #total = Cart.objects.all().filter(id=pk).values_list('total', flat=True)
    gab = Gab.objects.all()
    campos_gab = gab.filter(id=id)
    for x in campos_gab:
        print(x.id, x.gabarito)
        gabarito= str(x.gabarito).upper()
        pergunta= x.pergunta.upper()
        
            #gabarito = Gab.objects.get(gabarito='gabarito')
    
    #for dado in gab:
   #     if dado.id > 115:
     #   print(dado.id, dado.pergunta)        
      #  num = dado.id
       # per = dado.pergunta
        #gabarito = dado.gabarito
    
        
    user=request.user
    alternativa='?alt?'
    resposta ='?'
    alternativa2='?alt2?'
    id=x.id
    #gabarito= str(gab.first()).lower()
    
    if request.method== 'GET':
        form = GabForm()
        msg='envie sua resposta:)'
        id=x.id
        context={
            'form':form,
            'msg':msg,
            'id':id,
            "resposta":resposta,
            "gabarito":gabarito,
            "campos":campos_gab
                        }
        return render(request, 'app_questions/resposta.html', context)

    elif request.method =='POST':    
        form = GabForm(request.POST or None)
    # gabarito=' ?'
        if form.is_valid():
            #form.save()
            #form = GabForm()
            #print(form.cleaned_data, form.cleaned_data.get('pergunta'), form.cleaned_data.get('gabarito'))
        #    gabarito = form.cleaned_data["gabarito"]


    #     pergunta = form.cleaned_data["pergunta"].lower()
            resposta = str(form.cleaned_data["resposta"]).upper()
        # alternativa = form.cleaned_data["alternativa"]
            #alternativa2 = form.cleaned_data["alternativa2"]
            
        msg=''
            
        #if resposta == gabarito: 
        if resposta == gabarito: 
            msg='parabens.Vc acertou :-)'
            context={
                'msg':msg ,
                "resposta":resposta,
                "gabarito":gabarito,
                "gab":gab,
                "user":user,
                "campos":campos_gab
        #        "num":num,
        #       "per":per
            }
            #return confere(request, resposta, gabarito, msg)
            #return redirect('questions:confere', resposta, gabarito, msg)
    #       return HttpResponseRedirect(reverse('questions:confere', args=[msg]))
            return render(request, 'app_questions/confere.html', context )
            #<a href="{% url 'questions:confere' gabarito resposta msg %}"><button class="btn btn-primary py-3">confere ?</button></a>
        else:
            msg='não desista.Tente de novo :-|'       
            context={
                    "resposta":resposta,
                    "gabarito":gabarito,
                    'msg':msg,
                    "gab":gab,
                    "user":user,
                    "campos":campos_gab
            #      "num":num,
            #     "per":per
                }
            
            #return confere(request, resposta, gabarito, msg)
            return render(request, 'app_questions/confere.html', context )
    #      return HttpResponseRedirect(reverse('questions:confere', args=[msg]))
            #return redirect('questions:confere', resposta, gabarito, msg)
        
    print(type(pergunta),pergunta)
    
    print(type(gabarito),gabarito)
    print(request.user)
    print(type(resposta), resposta)    
    print(msg)
    #print(type(alternativa), alternativa)    
    #print(type(alternativa2), alternativa2)
       # return render(request,'app_questions/confere.html',{'gabarito2':gabarito})
    context = {
                    "title": "resposta Page",
                    "content": "Formulário ",
                    "form": form,
                    "resposta":resposta,
                    "gabarito":gabarito,
                    "msg":msg,
                    "gab":gab,
                    "user":user,
                    "campos":campos_gab,
    
                    #"num":num,
                    #"per":per
              
              }
   
    #return confere(request)
    return render(request, 'app_questions/resposta.html', context )
    

def confere(request, gabarito, resposta, msg):
    #gab = Gab.objectss.all()
    
    #gabarito= str(gab.first()).lower()      
    

    context = {
                    "title": "confere Page",
                    "content": "verificação com o gabarito ",
    #                "form":form,
     #               "form2":form2,
                    "resposta":resposta,
                    "gabarito":gabarito,
                    "msg":msg,
              
              }        
    return render(request,'app_questions/confere.html', context) 


def radio(request):
    
    msg='???'
    resposta='??'
    gabarito='?'
    context={'context':msg}
    
#    if request.method == 'POST':
    form = QuestionForm(request.POST or None)
    if form.is_valid():
            print(form.cleaned_data)
    resposta = form.cleaned_data["resposta22"].lower()
    gabarito = form.cleaned_data["gabarito"].lower()
        #    form.cleaned_data
    print(form.cleaned_data)
            
    if resposta == gabarito: 
        msg='parabens.Vc acertou :-)'
                    #return render(request,'app_questions/questions.html',{'msg':msg})
        context = {
                        "title": "Form Page",
                        "content": "Formulário ",
                        "form":form,
                        # "form_gab": form_gab,
                        "resposta":resposta,
                        "gabarito":gabarito,
                        "msg":msg,
                        #"gab":gab
                            }
    else:
        msg='não desista.Tente de novo :-|  '       
                    #return render(request,'app_questions/questions.html',{'msg':msg})
        context = {
                        "title": "Form Page",
                        "content": "Formulário ",
                        "form":form,
                        # "form_gab": form_gab,
                        "resposta":resposta,
                        "gabarito":gabarito,
                        "msg":msg,
                        #"gab":gab
                            }
    print(type(resposta), resposta)
    print(type(gabarito), gabarito)    
    print(msg)

    return render(request, 'app_questions/question22.html', context )
            
    #        print('não captura os dados do formulario')    
        