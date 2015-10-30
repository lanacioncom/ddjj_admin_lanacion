# coding: utf-8
from django.forms import widgets
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import  format_html
from .models import TipoBien, PersonaCargo

# https://github.com/django/django/blob/master/django/forms/widgets.py
class TipoBienSelectWidget(widgets.Select):

    class Media:
                js = [ "{0}{1}".format(settings.STATIC_URL, 'js/tipobien.widget.js') ]
                css =  {
                    'all' : ('styles/tipobien.widget.css',)
                }


    def render_option(self, selected_choices, option_value, option_label):
        tipo_bien_clasificacion = ''
        if option_value is None:
                option_value = ''
        elif option_value != '':
                try:
                        tipo_bien = TipoBien.objects.get(id = option_value)
                except TipoBien.DoesNotExists:
                        pass
                else:
                        if tipo_bien.clasificacion != None:
                                tipo_bien_clasificacion = tipo_bien.clasificacion
                
        option_value = force_text(option_value)

        if option_value in selected_choices:
                selected_html = mark_safe(' selected="selected"')
                if not self.allow_multiple_selected:
                        # Only allow for a single selection.
                        selected_choices.remove(option_value)
        else:
                selected_html = ''

        return format_html(u'<option value="{}"{} data-clasificacion="{}">{}</option>',
                           option_value,
                           selected_html,
                           tipo_bien_clasificacion,
                           force_text(option_label))


class PersonaCargoSelectWidget(widgets.Select):

    class Media:
         js = [ "{0}{1}".format(settings.STATIC_URL, 'js/personacargo.widget.js') ]
    
    def render_option(self, selected_choices, option_value, option_label):
        persona_id = ''
        if option_value is None:
            option_value = ''
        elif option_value != '':
            try:
                persona_cargo = PersonaCargo.objects.get(id = option_value)
            except PersonaCargo.DoesNotExists:
                pass
            else:
                persona_id = persona_cargo.persona.id
            
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html(u'<option value="{}"{} data-persona="{}">{}</option>',
                           option_value,
                           selected_html,
                           persona_id,
                           force_text(option_label))
