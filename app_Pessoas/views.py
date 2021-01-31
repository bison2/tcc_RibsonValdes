from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Pessoa, Disciplina , P_professor, P_aluno
from django.contrib.auth.models import User
# Create your views here.

def home_pessoa(request):
    pessoa_data = Pessoa.objects.tudo()
    prof_data = P_professor.objects.prof_disc()
    aluno_data = P_aluno.objects.tudo()
    disciplina_data = Disciplina.objects.disciplina()
    
    disc_prof_data = P_professor.objects.prof_disc()
    disc_aluno_data = P_aluno.objects.aluno_disc()
    

    return render(request, 'app_Pessoas/pessoas.html', {
                    'pessoas':pessoa_data,
                    'professores': prof_data,
                    'alunos': aluno_data,

                    'disciplinas': disciplina_data,
                    
                    'disc_prof': disc_prof_data,
                    'disc_aluno': disc_aluno_data,
                    }
            )


class PessoaDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    
    #queryset = Product.objects.all()
    template_name = "app_Pessoas/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(PessoaDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Pessoa.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

def pessoa_id(request, id):
    obj = Pessoa.objects.get(id=id)
    
   #person = get_object_or_404(Pessoa, id=id)
   #return HttpResponse("<h1>a pessoa é {}</h1>".format(obj.nome))
    context = {
               #'pessoa':obj,
               'pessoa':obj,
               
               }
    return render(request, 'app_Pessoas/detail.html', context)

def pessoa_detail(request, pk=None, *args, **kwargs):
    instance= Pessoa.objects.get_by_id(id)
    print(instance)
    if instance is None:
        raise Http404("pessoa não existe")
    context={'object':instance}
    return render(request, 'app_Pessoas/detail.html', context)
