from django import forms
from django.forms import fields, widgets
from .models import Vehiculo

class VehiculosForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields= ('modelo','marca','matricula','asientos','descripcion')

        widgets ={
            'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Aveo'}),
            'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Chevrolet'}),
            'matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder':'AAA-AAA'}),
            'asientos': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'2'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Describa su auto'}),
        }
        labels = {
            'modelos':'Modelos',
            'marca':'Marca',
            'matricula':'Matrícula',
            'asientos':'Asientos',
            'descripcion':'Descripción'
        }

    def clean(self):
            super(VehiculosForm, self).clean()
            matricula =  self.cleaned_data.get('matricula')
            asientos = self.cleaned_data.get('asientos')

            if len(matricula) != 7:
                self._errors['matricula'] = self.error_class(['Minimo de 7 caracteres requeridos'])

            if asientos < 1:
                self._errors['asientos'] = self.error_class(['Los asientos deben ser un numero entero positivo'])    

            

