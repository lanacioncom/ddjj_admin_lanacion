# coding: utf-8
import re
import csv
from django.contrib import admin
from django.contrib.admin.models import LogEntry, ContentType
from django.conf import settings
from django.db.models import Count
from django.conf.urls import url
from django.template.response import TemplateResponse, HttpResponse
from django.utils.encoding import smart_str
from admin_ddjj_app.models import *
from .forms import BienAdminForm, DdjjAdminForm, ExportForm
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


FIELDSETS_BIEN = [
		("", {'fields': ['vinculo', 'persona', 'ddjj', 'tipo_bien', 'nombre_bien', 'valor_fiscal', 'm_valor_fiscal_id', 'porcentaje', 'fecha_desde', 'fecha_hasta', 'pais', 'descripcion', 'origen', 'destino', 'obs']}),
		("Datos para rodados", {'fields': ['modelo'], 'classes': ['grp-collapse bien-datos', 'tipobien-{0}'.format(TipoBien.CLASIFICACION[0][0])]}),
		("Datos para bonos, títulos y acciones", {'fields': ['cant_acciones', 'entidad', 'ramo'], 'classes': ['grp-collapse bien-datos', 'tipobien-{0}'.format(TipoBien.CLASIFICACION[1][0])]}),
		("Datos para imuebles", {'fields': ['superficie', 'unidad_medida_id', 'valor_adq', 'm_valor_adq_id', 'mejoras', 'direccion', 'barrio', 'localidad', 'provincia'], 'classes': ['grp-collapse bien-datos', 'tipobien-{0}'.format(TipoBien.CLASIFICACION[2][0])]}),
	]

FIELDSETS_DDJJ = [
		("DDJJ",			{'fields': ['persona', 'poder_id', 'ano', 'tipo_ddjj_id', 'persona_cargo', 'url', 'flag_presenta', 'obs', 'obs_privadas']})
		# ("DATOS OPCIONALES",{'fields': []})
	]

class DdjjInline(NestedStackedInline):
	classes = ('grp-collapse grp-closed',)
	model= Ddjj
	extra=0
	fieldsets = FIELDSETS_DDJJ


class BienPersonaInline(NestedTabularInline):
	model= Bien.titulares.through
	extra=1
	raw_id_fields = ('persona',)

class BienInline(NestedStackedInline):
	model= Bien
	extra=0
	fieldsets = FIELDSETS_BIEN
	inlines = [BienPersonaInline]
	form = BienAdminForm

	raw_id_fields = ('persona', 'nombre_bien')
	related_lookup_fields = {
		# 'pk' : ['persona'],
	}
	autocomplete_lookup_fields = {
		'fk': ['persona','nombre_bien']
    }

	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		"""setting default owner of Bien"""
		if db_field.name == "persona":
                    db_field.default = None
		    if re.search(r"[0-9]", request.path.split('/')[4]):
			try:
			    persona = Ddjj.objects.get(id = request.path.split('/')[4]).persona
			    if persona:
				db_field.default = persona.id
                                
			except ValueError:
			    pass
		return super(BienInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class PersonaCargoInline(NestedTabularInline):
	model = PersonaCargo
	extra=1
	verbose_name = "Datos del cargo"
	verbose_name_plural = "cargos relacionados con este funcionario"

        def get_fields(self, request, obj=None):
                fields = ('ingreso', 'egreso', 'cargo', 'jurisdiccion')

                if request.user.is_superuser:
                        fields = ('flag_ingreso',) + fields

                return fields


class FamiliaresTabularInline(NestedTabularInline):
	model = Ddjj.familiares.through
	extra=1
	raw_id_fields = ('persona',)
	autocomplete_lookup_fields = {
        'fk': ['persona']
    }


class PersonaAdmin(NestedModelAdmin):
	list_display = ['apellido', 'nombre', 'documento']

	search_fields = ['apellido', 'nombre']
	list_filter = ['cargos__poder_id']

	# inlines=[PersonaCargoInline, DdjjInline]
	inlines=[PersonaCargoInline]

        class Media:
                css = {
                        'all': ("{0}{1}".format(settings.STATIC_URL, 'css/persona.css'),)
                }
                js = ["{0}{1}".format(settings.STATIC_URL, 'js/jquery.ui.datepicker-es.js'),]

        def get_fieldsets(self, request, obj=None):
                user = request.user

	        fieldsets = [
		        ('Datos principales',	{'fields': ['apellido', 'nombre', 'tipo_documento_id', 'documento', 'cuit_cuil', 'sexo_id',]}),
		        ('Datos optativos', 	{'fields': ['nacimento', 'estado_civil_id', 'legajo',], 'classes': ['grp-collapse grp-closed']}),
		        ('Datos social media',	{'fields': ['sitio_oficial', 'facebook', 'twitter', ], 'classes': ['grp-collapse grp-closed']}),                        
                ]

                if user.is_superuser:
                        links_fields = ('Links varios',{'fields': ['tag_id', 'tag_img_id', 'tag_descripcion', 'ficha_d_l'], 'classes': ['grp-collapse grp-closed']})
                        fieldsets.append(links_fields)

                return fieldsets


class DdjjAdmin(NestedModelAdmin):
	form = DdjjAdminForm
	inlines=[FamiliaresTabularInline, BienInline]
	list_filter=['persona', 'poder_id', 'tipo_ddjj_id', 'status']
	list_display = ('ano', 'persona', 'tipo_ddjj_id', 'status', 'created_at', 'updated_at',)
	search_fields=['persona__nombre', 'persona__apellido']
	
	# popup para elegir legislador
	raw_id_fields = ('persona','persona_cargo')
	related_lookup_fields = {
		# 'pk' : ['persona_cargo']
		# 'm2m' : ['persona_cargo']
	}    
	autocomplete_lookup_fields = {
		'fk': ['persona', 'persona_cargo'],
	}        
        
	class Media:
		js = [
			"{0}{1}".format(settings.STATIC_URL, 'js/jquery.ui.datepicker-es.js'),
			"{0}{1}".format(settings.STATIC_URL, 'js/ddjj__persona_cargo.js'),
			"{0}{1}".format(settings.STATIC_URL, 'js/ddjj__bienes.js')
		]
                css = {
                        'all': ("{0}{1}".format(settings.STATIC_URL, 'css/ddjj.css'),)
                }


	def get_fieldsets(self, request, obj=None):
		fieldsets = FIELDSETS_DDJJ

		user = request.user
		if user.is_superuser:
		        superuser_fieldsets = [("Revisión", {'fields': ['status', ]})]
		        return fieldsets + superuser_fieldsets

		return fieldsets

        def get_urls(self):
            urls = super(DdjjAdmin, self).get_urls()
            my_urls = [
                url(r'^export/$', self.admin_site.admin_view(self.export))
            ]
            return my_urls + urls

        def export(self, request):
            if not request.user.is_superuser:
                return HttpResponse(status=403)

            if request.method == 'POST':
                form = ExportForm(request.POST)
                if form.is_valid():
                    backend_url = settings.BACKEND_BASE_URL
                    ddjj_url = backend_url + 'admin/admin_ddjj_app/ddjj/'
                    
                    date_from = form.cleaned_data['date_from']
                    date_to = form.cleaned_data['date_to']
                    
                    # http://djangotricks.blogspot.com.ar/2013/12/how-to-export-data-as-excel.html
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename=ddjj_{0}_{1}.csv'.format(date_from, date_to)
                    response['Cache-Control'] = 'no-cache'
                    import sys
                    reload(sys)
                    sys.setdefaultencoding("utf-8")
                    import unicodecsv
                    writer = unicodecsv.writer(response, csv.excel, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL, encoding='utf-8')
                    writer.writerow([
                        smart_str(u"DDJJ ID"),
                        smart_str(u"DDJJ Admin"),
                        smart_str(u"DDJJ Status"),
                        smart_str(u"DDJJ Tipo"),
                        smart_str(u"DDJJ Funcionario Nombre"),
                        smart_str(u"DDJJ Funcionario Cargo"),
                        smart_str(u"DDJJ Funcionario Jurisdiccion"),
                        smart_str(u"DDJJ Poder"),
                        smart_str(u"DDJJ Presenta"),
                        smart_str(u"DDJJ Carta URL"),
                        smart_str(u"DDJJ Observaciones Publicas"),
                        smart_str(u"DDJJ Observaciones Privadas"),

                        smart_str(u"Bien ID"),
                        smart_str(u"Bien Vinculo"),
                        smart_str(u"Bien Persona"),
                        smart_str(u"Bien Tipo"),
                        smart_str(u"Bien Nombre"),
                        smart_str(u"Bien Moneda Valor Fiscal"),
                        smart_str(u"Bien Valor Fiscal"),
                        smart_str(u"Bien Porcentaje"),
                        smart_str(u"Bien Fecha Desde"),
                        smart_str(u"Bien Fecha Hasta"),
                        smart_str(u"Bien Pais"),
                        smart_str(u"Bien Origen"),
                        smart_str(u"Bien Destino"),
                        smart_str(u"Bien Descripcion"),
                        smart_str(u"Bien Observaciones"),
                        
                        smart_str(u"Usuario Username"),
                        smart_str(u"Usuario Nombre"),
                        smart_str(u"Organizaciones"),
                        smart_str(u"DDJJ Fecha Creacion"),
                        smart_str(u"DDJJ Fecha Modificacion")
                    ])

                    from django.db import connection
                    ddjj_content_type = ContentType.objects.get(model = 'ddjj').id
                    cursor = connection.cursor()
                    query = """
                        SELECT d.id, 
                          CONCAT(%s, d.id), 
                          CASE WHEN d.status=0 THEN 'No publicada'
                               ELSE 'Publicada'
                          END,
                          CASE WHEN d.tipo_ddjj_id=0 THEN 'Alta'
                               WHEN d.tipo_ddjj_id=1 THEN 'Baja'
                               WHEN d.tipo_ddjj_id=2 THEN 'Inicial'
                               ELSE 'Anual'
                          END,
                          CONCAT(p.nombre, ' ', p.apellido),
                          c.cargo,
                          j.nombre,
                          CASE WHEN j.poder_id=0 THEN 'Ejecutivo'
                               WHEN j.poder_id=1 THEN 'Legislativo'
                               WHEN j.poder_id=2 THEN 'Judicial'
                               ELSE 'Otro'
                          END,
                          d.flag_presenta, 
                          d.url, 
                          REPLACE(REPLACE(d.obs, '\n', ' '), '\r', ''),
                          REPLACE(REPLACE(d.obs_privadas, '\n', ' '), '\r', ''),
                          b.id,
                          b.vinculo,
                          CONCAT(pb.nombre, ' ', pb.apellido),
                          tb.nombre,
                          nb.nombre,
                          CASE WHEN b.m_valor_fiscal_id=0 THEN '$'
                               WHEN b.m_valor_fiscal_id=1 THEN 'us$'
                               WHEN b.m_valor_fiscal_id=2 THEN 'E'
                               WHEN b.m_valor_fiscal_id=3 THEN 'Uruguayos'
                               WHEN b.m_valor_fiscal_id=4 THEN '£'
                               WHEN b.m_valor_fiscal_id=5 THEN 'A'
                               WHEN b.m_valor_fiscal_id=6 THEN 'A$'
                               WHEN b.m_valor_fiscal_id=7 THEN '$L'
                               ELSE 'No especifica'
                          END,
                          b.valor_fiscal,
                          b.porcentaje,
                          b.fecha_desde,
                          b.fecha_hasta,
                          b.pais,
                          b.origen,
                          b.destino,
                          REPLACE(REPLACE(b.descripcion, '\n', ' '), '\r', ''),
                          REPLACE(REPLACE(b.obs, '\n', ' '), '\r', ''),
                          au.username,
                          g.groups,
                          CONCAT(au.first_name, ' ', au.last_name),
                          d.created_at, 
                          d.updated_at 
                        FROM ddjjs d, 
                             personas p,
                             persona_cargos pc,
                             cargos c,
                             jurisdiccions j,
                             (SELECT dl.user_id as user_id,
                                     dl.object_id as ddjj_id
                               FROM django_admin_log dl, 
                                 (SELECT MAX(action_time) as action_time, content_type_id, object_id  
                                    FROM django_admin_log  
                                    GROUP by content_type_id, object_id) dl_max 
                               WHERE dl_max.action_time = dl.action_time 
                                AND dl_max.content_type_id = dl.content_type_id 
                                AND dl_max.object_id = dl.object_id) logentry,
                             auth_user au,
                             biens b,
                             personas pb,
                             tipo_biens tb,
                             (SELECT GROUP_CONCAT(ag.name) as groups, 
                                     aug.user_id as user_id
                                  FROM auth_group ag, 
                                       auth_user_groups aug 
                                  WHERE aug.group_id = ag.id  
                                  GROUP by aug.user_id) g,
                             nombre_biens nb
                        WHERE d.persona_id = p.id
                           AND d.persona_cargo_id = pc.id
                           AND c.id = pc.cargo_id
                           AND pc.jurisdiccion_id = j.id
                           AND logentry.ddjj_id = d.id
                           AND logentry.user_id = au.id
                           AND b.ddjj_id = d.id
                           AND b.persona_id = pb.id
                           AND b.nombre_bien_id = nb.id
                           AND b.tipo_bien_id = tb.id
                           AND g.user_id = au.id
                           AND d.created_at >= %s
                           AND d.created_at <= %s
                        ORDER BY d.created_at
                        """
                    cursor.execute(query, [ddjj_url, date_from, date_to])
                    writer.writerows(cursor)

                    return response
            else:
                form = ExportForm()

            context = dict(
                self.admin_site.each_context(),
                form = form
            )
            
            return TemplateResponse(request, "admin/export.html", context) 

class BienAdmin(NestedModelAdmin):
	inlines = [BienPersonaInline]
	form = BienAdminForm
	list_display = [ 'tipo_bien', 'nombre_bien']
	list_filter=['tipo_bien', 'nombre_bien', 'origen']
	fieldsets = FIELDSETS_BIEN





class CargoAdmin(NestedModelAdmin):
	list_display = ['__unicode__', 'poder_id']
	list_filter=['poder_id']
	search_fields=['cargo']
	fieldsets = [(None, {'fields': ['cargo', 'poder_id']},)]

        class Media:
                js = ["{0}{1}".format(settings.STATIC_URL, 'js/jquery.ui.datepicker-es.js')]        
	# list_display = ('cargo_personas',) 


class PersonaCargoAdmin(NestedModelAdmin):
	list_filter=['cargo__poder_id', 'cargo', 'persona']
	search_fields=['cargo__cargo', 'persona__apellido']

        def get_fieldsets(self, request, obj=None):
                user = request.user
                fields = ['ingreso', 'egreso', 'persona', 'cargo', 'jurisdiccion']

                if user.is_superuser:
                        fields.insert(0, 'flag_ingreso')

                fieldsets = ((None, {'fields': fields}),)

                return fieldsets

        class Media:
                js = ["{0}{1}".format(settings.STATIC_URL, 'js/jquery.ui.datepicker-es.js')]        

class TipoBienAdmin(NestedModelAdmin):
	list_filter=['clasificacion']
        list_display = ('nombre', 'clasificacion',)
        list_editable = ('clasificacion',)

class NombreBienAdmin(NestedModelAdmin):

	list_filter=['tipo_bien']
	list_display = ('nombre', 'tipo_bien', 'cantidad_de_bienes')
	list_editable = ('tipo_bien',)
        search_fields = ['nombre']

	def cantidad_de_bienes(self, inst):
		return '{0} veces usado'.format(inst.bienes.count())

class JurisdiccionAdmin(admin.ModelAdmin):
	list_filter=['poder_id']
	list_display = ('nombre', 'poder_id')
        search_fields = ['nombre']
        
admin.site.register(Ddjj, DdjjAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(PersonaCargo, PersonaCargoAdmin)
admin.site.register(Bien, BienAdmin)
admin.site.register(TipoBien, TipoBienAdmin)
admin.site.register(NombreBien, NombreBienAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Jurisdiccion, JurisdiccionAdmin)
