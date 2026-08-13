from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('tarea/editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('tarea/eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    
    # --- NUEVAS RUTAS PARA EQUIPOS ---
    path('equipos/', views.gestionar_equipos, name='gestionar_equipos'),
    path('equipos/nuevo-grupo/', views.crear_grupo, name='crear_grupo'),
    path('equipos/nuevo-integrante/', views.crear_integrante, name='crear_integrante'),
]