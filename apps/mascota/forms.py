from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            "nombre",
            "sexo",
            "edad_aproximada",
            "fecha_rescate",
            "persona",
            "vacuna",
            "foto"
        ]
        labels = {
            "nombre": "Nombre",
            "sexo": "Sexo",
            "edad_aproximada": "Edad Aproximada",
            "fecha_rescate": "Fecha de Rescate",
            "persona": "Persona",
            "vacuna":"Vacunas",
            "foto":"Foto"
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "sexo": forms.TextInput(attrs={"class":"form-control"}),
            "edad_aproximada": forms.TextInput(attrs={"class":"form-control"}),
            "fecha_rescate": forms.TextInput(attrs={"class": "form-control", "type": "date",},), 
            "persona": forms.Select(attrs={"class":"form-control"}),
            "vacuna": forms.CheckboxSelectMultiple(attrs={"class":"form-check-input"}),
        }