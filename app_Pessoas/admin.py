from django.contrib import admin

# Register your models here.
from .models import Pessoa, Disciplina , P_professor, P_aluno


admin.site.register(Pessoa)
admin.site.register(Disciplina)

admin.site.register(P_professor)
admin.site.register(P_aluno)