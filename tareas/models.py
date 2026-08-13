from django.db import models

# 1. Entidad: Grupo
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 2. Entidad: Integrante
class Integrante(models.Model):
    nombre = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='integrantes')

    def __str__(self):
        return f"{self.nombre} (Grupo: {self.grupo.nombre})"

# 3. Entidad: Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# 4. Entidad: Tarea
class Tarea(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
    )
    titulo = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    # Aquí delegamos la tarea al líder (integrante)
    lider_responsable = models.ForeignKey(Integrante, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas_asignadas')

    def __str__(self):
        return f"{self.titulo} - {self.estado}"