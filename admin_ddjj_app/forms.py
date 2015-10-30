# coding: utf-8
import re
import datetime
from django import forms
from grappelli_nested.forms import BaseNestedModelForm
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget 
from .widgets import TipoBienSelectWidget, PersonaCargoSelectWidget
from .models import Bien, Ddjj

class BienAdminForm(BaseNestedModelForm):
    valor_fiscal =  forms.DecimalField(max_digits=12, decimal_places=2, localize=True, help_text="Ejemplo: 12.345.567,10", required = False)
    valor_adq =  forms.DecimalField(max_digits=12, decimal_places=2, localize=True, help_text="Ejemplo: 12.345.567,10", required = False)
    porcentaje =  forms.DecimalField(max_digits=12, decimal_places=2, localize=True, help_text="<strong>NO</strong> incluir el signo '%'.<br> Si ingresa un número decimal use ',' (coma) como delimitador", required = False)
    superficie =  forms.DecimalField(max_digits=12, decimal_places=2, localize=True, help_text="Ejemplo: 12.345.567,10", required = False)

    # TODO: Refactorizar
    def clean_valor_fiscal(self):
        key = 'valor_fiscal'
        if self.prefix:
            key = self.prefix + '-' + key
            
        if self.data.has_key(key) and self.data[key]:
            input_str = self.data[key]
            pattern = '^-?([0-9]{1,3})+(\.[0-9]{3})*(\,[0-9]{1,2})?$' # http://regexr.com/3avja
            result = re.match(pattern, input_str)
            if result == None:
                raise ValidationError(u'Este campo no es un número válido.')

        return self.cleaned_data['valor_fiscal']

    def clean_valor_adq(self):
        key = 'valor_adq'
        if self.prefix:
            key = self.prefix + '-' + key
            
        if self.data.has_key(key) and self.data[key]:
            input_str = self.data[key]
            pattern = '^-?([0-9]{1,3})+(\.[0-9]{3})*(\,[0-9]{1,2})?$' # http://regexr.com/3avja
            result = re.match(pattern, input_str)
            if result == None:
                raise ValidationError(u'Este campo no es un número válido.')

        return self.cleaned_data['valor_adq']

    def clean_porcentaje(self):
        key = 'porcentaje'
        if self.prefix:
            key = self.prefix + '-' + key

        if self.data.has_key(key):
            input_str = self.data[key]
            porcentaje = self.cleaned_data['porcentaje']
            if porcentaje and ('.' in input_str or porcentaje > 100 or porcentaje < 0):
                raise ValidationError(u'Este campo no es un porcentaje valido.')

        return self.cleaned_data['porcentaje']

    def clean_superficie(self):
        key = 'superficie'
        if self.prefix:
            key = self.prefix + '-' + key
            
        if self.data.has_key(key) and self.data[key]:
            input_str = self.data[key]
            pattern = '^([0-9]{1,3})+(\.[0-9]{3})*(\,[0-9]{1,2})?$' # http://regexr.com/3avja
            result = re.match(pattern, input_str)
            if result == None:
                raise ValidationError(u'Este campo no es un número válido.')

        return self.cleaned_data['superficie']

    class Meta:
        model = Bien
        # widgets = {
        #     'tipo_bien': TipoBienSelectWidget(),
        # }


class DdjjAdminForm(BaseNestedModelForm):
    class Meta:
        model = Ddjj
        widgets = {
            'persona_cargo': PersonaCargoSelectWidget(),
        }


class ExportForm(forms.Form):
    date_from = forms.DateField(widget=AdminDateWidget, label=u"Desde fecha creación")
    date_to = forms.DateField(widget=AdminDateWidget, label=u"Hasta fecha creación", initial=datetime.date.today )
