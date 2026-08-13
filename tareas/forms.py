from django import forms
from .models import Proyecto, Tarea, Grupo, Integrante # <-- Actualiza las importaciones

class ProyectoForm(forms.ModelForm):
    # (El código de ProyectoForm que ya tienes se queda igual)
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Migración a la nube'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles del proyecto...'}),
        }

# --- NUEVO CÓDIGO A AGREGAR ---
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'lider_responsable']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Crear base de datos'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'lider_responsable': forms.Select(attrs={'class': 'form-select'}),
        }
        
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Equipo de Desarrollo Backend'}),
        }

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['nombre', 'grupo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'grupo': forms.Select(attrs={'class': 'form-select'}),
        }