from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
from .utils import ejecutar_consulta_raw

# READ Y CREATE DJANGO
def lista_tareas(request):
    tareas = Tarea.objects.all()
    form = TareaForm()
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    return render(request, 'todolist/lista_tareas.html', {'tareas': tareas, 'form': form})

# DELETE DJANGO
def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')

# UPDATE DJANGO
def completar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('lista_tareas')

# READ SQL
def ejecutar_consulta(request):
    consulta = "SELECT * FROM todolist_tarea WHERE completada = '1';"
    resultados = ejecutar_consulta_raw(consulta)
    return render(request, 'todolist/consulta_resultados.html', {'resultados': resultados})