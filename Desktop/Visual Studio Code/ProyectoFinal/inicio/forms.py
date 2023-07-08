from django import forms

class CrearAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    dni = forms.IntegerField()
    
class BuscarAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)