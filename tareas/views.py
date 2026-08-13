from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Tarea, Grupo, Integrante # <-- Actualiza esta línea
from .forms import ProyectoForm, TareaForm, GrupoForm, IntegranteForm

# Vista anterior (listar)
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'tareas/lista_proyectos.html', {'proyectos': proyectos})

# Nueva vista (crear)
def crear_proyecto(request):
    if request.method == 'POST':
        # Si el usuario envió el formulario, guardamos los datos
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos') # Redirige a la página principal tras guardar
    else:
        # Si acaba de entrar a la página, mostramos el formulario vacío
        form = ProyectoForm()
    
    return render(request, 'tareas/crear_proyecto.html', {'form': form})

def detalle_proyecto(request, proyecto_id):
    # Buscamos el proyecto por su ID, si no existe lanza error 404
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    # Traemos todas las tareas vinculadas a este proyecto
    tareas = proyecto.tareas.all() 

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False) # Pausamos el guardado
            nueva_tarea.proyecto = proyecto # Le asignamos el proyecto actual
            nueva_tarea.save() # Ahora sí la guardamos en la base de datos
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = TareaForm()

    contexto = {
        'proyecto': proyecto,
        'tareas': tareas,
        'form': form
    }
    return render(request, 'tareas/detalle_proyecto.html', contexto)

def editar_tarea(request, tarea_id):
    # Buscamos la tarea específica
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        # El parámetro 'instance=tarea' es clave: le dice a Django que no cree una nueva, sino que actualice esta
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        # Si acaba de entrar, mostramos el formulario con los datos actuales de la tarea
        form = TareaForm(instance=tarea)
        
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    proyecto_id = tarea.proyecto.id # Guardamos el ID del proyecto para saber a dónde regresar
    tarea.delete() # Borramos la tarea de la base de datos
    return redirect('detalle_proyecto', proyecto_id=proyecto_id)

def gestionar_equipos(request):
    grupos = Grupo.objects.all()
    integrantes = Integrante.objects.all()
    return render(request, 'tareas/gestionar_equipos.html', {'grupos': grupos, 'integrantes': integrantes})

def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_equipos')
    else:
        form = GrupoForm()
    
    # Reutilizaremos una misma plantilla para ambos formularios
    return render(request, 'tareas/formulario_equipo.html', {'form': form, 'titulo': 'Nuevo Grupo'})

def crear_integrante(request):
    if request.method == 'POST':
        form = IntegranteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_equipos')
    else:
        form = IntegranteForm()
        
    return render(request, 'tareas/formulario_equipo.html', {'form': form, 'titulo': 'Nuevo Integrante'})