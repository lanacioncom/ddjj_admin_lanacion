# coding: utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.conf import settings

from django.db import models
import time
import json

SEXO = ((0,"M"), (1,"F"),)
TIPO_DOCUMENTO  = ((0, "DNI"), (1, "LE"), (2, "LC"), (3, "PASAPORTE"),)
# se saltea el 1, era: (1, "Cónyugue"), no corresponde
ESTADO_CIVIL  = ((0, "Casado/a"), (2, "Divorciado/a"), (3, "Separado"), (4, "Soltero/a"), (5, "U. Hecho"), (6, "Viudo/a"),)
TIPO_DDJJ = ((0, "Alta"), (1, "Baja"), (2, "Inicial"), (3, "Anual"),)
PODER = ((0, "Ejecutivo"), (1, "Legislativo"), (2, "Judicial"), (3, "Otro"),)
UNIDAD_MEDIDA = ((0, "m2"), (1, "ha"),)
TIPO_MONEDA = ((0, "$"), (1, "us$"), (2, "E"), (3, " Uruguayos"), (4, "£"), (5, "A"), (6, "A$"), (7, "$L"), (8, "No especifica"))
VINCULO_BASE = (('Conviviente', 'Conviviente'), ('Cónyuge', 'Cónyuge'), ('Hijo/a', 'Hijo/a'), )
VINCULO_FAMILIAR= VINCULO_BASE + (('Otro', 'Otro'),)
VINCULO= VINCULO_BASE + (('Titular', 'Titular'), ('Otro', 'Otro'))


class Persona(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    apellido = models.CharField(max_length=255, blank=False, verbose_name=u"apellido/s")
    nombre = models.CharField(max_length=255, blank=False, verbose_name=u"nombre/s")
    legajo = models.CharField(max_length=255, blank=True)
    tipo_documento_id = models.IntegerField(blank=True, null=True, choices=TIPO_DOCUMENTO, verbose_name="tipo de documento")
    documento = models.IntegerField(blank=True, null=True, verbose_name=u"número")
    cuit_cuil = models.CharField(max_length=255, blank=True)
    nacimento = models.DateField(blank=True, null=True, verbose_name=u"fecha de nacimiento")
    sexo_id = models.IntegerField(choices=SEXO, verbose_name = "sexo", default = 0)
    estado_civil_id = models.IntegerField(blank=True, null=True, choices=ESTADO_CIVIL, verbose_name="Estado civil")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag_id = models.CharField(max_length=255, blank=True, help_text="ID del tag en el diario La Nación")
    tag_img_id = models.CharField(max_length=255, blank=True, help_text="ID de la img del tag")
    tag_descripcion = models.CharField(max_length=255, blank=True, help_text="Descripcion del tag Nacion")
    ficha_d_l = models.CharField(max_length=255, blank=True, null = True, default = None, help_text = "Url ficha de Directorio Legislativo") # link a la web de directorio legislativo


    sitio_oficial = models.CharField(max_length=255, blank=True, null = True, help_text="Sitio Oficial")
    facebook = models.CharField(max_length=255, blank=True, null = True, help_text="Facebook")
    twitter = models.CharField(max_length=255, blank=True, null = True, help_text="Twitter")

    def get_nombre(self):
        return "%s %s" % (self.apellido, self.nombre)

    def get_nombre_apellido(self):
        return "%s, %s" % (self.apellido, self.nombre)


    def related_label(self):
        return u"%s, %s (%s)" % (self.nombre, self.apellido, self.id)

    def get_ddjjs_total(self):
        return self.ddjjs.count()

    def get_cargo_publico_desde(self):
        cargos = self.personacargo_set.order_by('ingreso')
        if cargos.count() > 0:
            return cargos[0].ingreso
            
        return None

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nombre__icontains", "apellido__icontains")
    
    class Meta:
        ordering = ['apellido', 'nombre']
        db_table = 'personas'

    def __unicode__(self):
        return self.get_nombre()


class Ddjj(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    ano = models.IntegerField(blank=False, null=False, verbose_name=u"año")
    tipo_ddjj_id = models.IntegerField(blank=False, null=False, choices=TIPO_DDJJ, verbose_name="tipo DDJJ")
    funcionario = models.CharField(max_length=255, blank=True, help_text="Este campo lo completa el sistema.")
    url = models.CharField(max_length=255, blank=True, help_text="Url DocumentCloud", verbose_name="link al documento original")
    key = models.IntegerField(blank=True, null=True, help_text="Este campo lo completa el sistema.")
    clave = models.CharField(max_length=255, blank=True, help_text="Este campo lo completa el sistema.")
    flag_presenta = models.IntegerField("carta de DDJJ", choices=((0, "Si"), (1, "No"),),
                                        default = 1,
                                        help_text="<strong style='color:blue'>'Solo el PDF'</strong> Presentó carta o documento distinto al formulario de DDJJ del Poder")
    obs = models.TextField(u"observaciones públicas", blank=True)
    obs_privadas = models.TextField(max_length=255, blank=True, null=True, verbose_name="observaciones privadas")
    flag_search = models.CharField(max_length=255, blank=True, help_text="Este campo lo completa el sistema.")
    visitas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.IntegerField(blank=False, null=False,
                                choices=((0, "NO"), (1, "SI"),),
                                help_text="Indica si puede ser publicada",
                                default=0,
                                verbose_name="publicada?") 
    poder_id = models.IntegerField(choices=PODER, verbose_name="poder", default = 0)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificación")

    # persona_id = models.IntegerField(blank=True, null=True)
    # persona_cargo_id = models.IntegerField(blank=True, null=True)
    persona = models.ForeignKey("Persona", related_name="ddjjs")
    persona_cargo = models.ForeignKey("PersonaCargo", related_name="ddjjs", help_text="Indique el cargo que ocupa para esta DDJJ")
    familiares = models.ManyToManyField("Persona", through="DdjjFamiliar", verbose_name="familiares")

    def get_flag_search(self):
        return "%s %s %s %s" % (self.persona.apellido.strip(), self.persona.nombre.strip(), self.ano, TIPO_DDJJ[self.tipo_ddjj_id][1],)

    class Meta:
        db_table = 'ddjjs'
        ordering = ['persona']
        verbose_name = 'Declaración Jurada'        
        verbose_name_plural = 'Declaraciones Juradas'        
    
    def save(self, *args, **kwargs):
        self.funcionario = "".join(self.get_flag_search().split(" "))
        self.clave = "".join(self.get_flag_search().split(" "))
        self.flag_search = "-".join(self.get_flag_search().split(" ")).lower()
        self.key = time.time() # lo usa la app rails
        super(Ddjj, self).save(*args, **kwargs)


    def __unicode__(self):
        return "%s  %s - %s" % (self.ano, TIPO_DDJJ[self.tipo_ddjj_id][1], self.persona.get_nombre())

    def get_frontend_slug(self):
        persona_nombre = "%s %s" % (self.persona.apellido.strip(), self.persona.nombre.strip())
        frontend_slug =  "{0}-{1}-{2}".format(persona_nombre, self.ano, TIPO_DDJJ[self.tipo_ddjj_id][1])
        frontend_slug = frontend_slug.replace (" ", "-").lower()

        return frontend_slug

    def get_frontend_url(self):
        import time
        slug = self.get_frontend_slug()
        return "{0}/ddjj/{1}?{2}".format( settings.FRONTEND_BASE_URL, slug, time.time())

    def get_tipo_ddjj(self):
        return TIPO_DDJJ[self.tipo_ddjj_id][1]

    def get_poder(self):
        return PODER[self.poder_id][1]

    def get_flag_presenta(self):
        if self.flag_presenta == 0:
            return True
        else:
            return False

    def get_cargo(self):
        return self.persona_cargo.cargo.cargo


class DdjjFamiliar(models.Model):
    ddjj = models.ForeignKey("Ddjj")
    persona = models.ForeignKey("Persona", verbose_name="familiar", blank = True, null = True)
    vinculo = models.CharField(max_length=255, blank=True, choices=VINCULO_FAMILIAR, help_text="Indica la relacion con el titular de la DDJJ", verbose_name=u"vínculo con el declarante")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['persona__apellido']
        verbose_name_plural = 'Familiares mencionados en esta ddjj'  


class TipoBien(models.Model):
    CLASIFICACION  = ((0, "Rodados"),
                      (1, u"Bonos, títulos y acciones"),
                      (2, "Inmuebles"),)
    
    # id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    clasificacion = models.IntegerField(blank=True, null=True, choices=CLASIFICACION)

    class Meta:
        db_table = 'tipo_biens'
        ordering = ['nombre']
        verbose_name_plural = 'Tipo Bienes'
        
    def __unicode__(self):
        return "%s" % (self.nombre)

    def get_clasificacion(self):
        if self.clasificacion != None:
            return self.CLASIFICACION[self.clasificacion][1]
        else:
            return None


class NombreBien(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255, blank=True)
    # tipo_bien_id = models.IntegerField(blank=True, null=True)
    tipo_bien = models.ForeignKey("TipoBien",db_column="tipo_bien_id", related_name="nombre_bienes", verbose_name="tipo de bien", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nombre_biens'
        ordering = ['-nombre']
        verbose_name_plural = 'Nombre Bienes'    
        managed = False    

    def __unicode__(self):
        return "%s" % (self.nombre)

    def related_label(self):
        return u"%s (%s)" % (self.nombre, self.id)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nombre__icontains")


class Bien(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True, verbose_name=u"Dirección")
    barrio = models.CharField(max_length=255, blank=True)
    localidad = models.CharField(max_length=255, blank=True)
    provincia = models.CharField(max_length=255, blank=True)
    pais = models.CharField(max_length=255, blank=True, verbose_name=u"País")
    modelo = models.IntegerField(blank=True, null=True)
    entidad = models.CharField(max_length=255, blank=True)
    ramo = models.CharField(max_length=255, blank=True)
    cant_acciones = models.CharField(max_length=255, blank=True)
    fecha_desde = models.DateField(blank=True, null=True)
    destino = models.CharField(max_length=255, blank=True)
    origen = models.CharField(max_length=255, blank=True)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Superficie de la propiedad <br> Si ingresa un número decimal use '.' (punto) como delimitador")
    unidad_medida_id = models.IntegerField(blank=True, null=True, choices=UNIDAD_MEDIDA, help_text="Unidad de medida usada para la superficie", verbose_name="Unidad de medida")
    m_mejoras_id = models.IntegerField(blank=True, null=True, choices=TIPO_MONEDA)
    mejoras = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m_valor_fiscal_id = models.IntegerField(blank=True, null=True, choices=TIPO_MONEDA, verbose_name="Moneda valor fiscal")
    valor_fiscal = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    m_valor_adq_id = models.IntegerField(blank=True, null=True, choices=TIPO_MONEDA, verbose_name=u"Moneda valor adquisición")
    valor_adq = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)
    titular_dominio = models.CharField(max_length=255, blank=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="<strong>NO</strong> incluir el signo '%'.<br> Si ingresa un número decimal use '.' (punto) como delimitador")
    vinculo = models.CharField(max_length=255, choices=VINCULO, help_text="Indica la relacion con el titular de la DDJJ", default='Titular', verbose_name=u"vínculo con el declarante")
    periodo = models.CharField(max_length=255, blank=True)
    obs = models.CharField(max_length=255, blank=True, verbose_name="observaciones")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # tipo_bien_id = models.IntegerField(blank=True, null=True)
    # nombre_bien_id = models.IntegerField(blank=True, null=True)
    tipo_bien = models.ForeignKey(TipoBien, related_name="bienes", verbose_name="tipo de bien")
    nombre_bien = models.ForeignKey(NombreBien, related_name="bienes", verbose_name="nombre del bien")
    tipo_bien_s = models.CharField(max_length=255, blank=True)
    nombre_bien_s = models.CharField(max_length=255, blank=True)
    
    # ddjj_id = models.IntegerField(blank=True, null=True)
    # persona_id = models.IntegerField(blank=True, null=True)
    ddjj = models.ForeignKey(Ddjj, related_name="bienes", help_text="Indica la DDJJ a la cual pertenece este bien")
    persona = models.ForeignKey(Persona, help_text="Es el titular del bien, este puede ser distinto al titular de la DDJJ", verbose_name="Titular del bien", blank=True, null=True)
    titulares = models.ManyToManyField(Persona, through='BienPersona', related_name="bienese")
    

    # def get_moneda(self):
    #     return TIPO_MONEDA[self[]]

    def get_unidad_medida(self):
        if self.unidad_medida_id != None:
            return UNIDAD_MEDIDA[self.unidad_medida_id][1]
        else:
            return None

    def get_mejoras_moneda_tipo(self):
        if self.m_mejoras_id != None:
            return TIPO_MONEDA[self.m_mejoras_id][1]
        else:
            return None

    def get_valor_fiscal_moneda_tipo(self):
        if self.m_valor_fiscal_id != None:
            return TIPO_MONEDA[self.m_valor_fiscal_id][1]
        else:
            return None

    def get_valor_adq_moneda_tipo(self):
        if self.m_valor_adq_id != None:
            return TIPO_MONEDA[self.m_valor_adq_id][1]
        else:
            return None

    def get_json(self):
        bien_json = {
            'vinculo': self.vinculo,
            'tipo': self.tipo_bien.nombre,
            'nombre': self.nombre_bien.nombre
        }

        if self.persona:
            bien_json['persona'] = self.persona.get_nombre()
            
        if self.valor_fiscal:
            bien_json['valor_fiscal'] = str(self.valor_fiscal)
            
        if self.m_valor_fiscal_id != None:
            bien_json['moneda_valor_fiscal'] = TIPO_MONEDA[self.m_valor_fiscal_id][1]

        if self.porcentaje:
            bien_json['porcentaje'] = str(self.porcentaje)

        if self.fecha_desde:
            bien_json['fecha_desde'] = self.fecha_desde.strftime("%d/%m/%y")

        if self.fecha_hasta:
            bien_json['fecha_hasta'] = self.fecha_hasta.strftime("%d/%m/%y")

        if self.pais:
            bien_json['pais'] = self.pais

        if self.descripcion:
            bien_json['descripcion'] = self.descripcion

        if self.origen:
            bien_json['origen'] = self.origen

        if self.destino:
            bien_json['destino'] = self.destino
                                
        if self.obs:
            bien_json['observaciones'] = self.obs

        if self.tipo_bien:
            bien_json['tipo_bien'] = self.tipo_bien.nombre

            if self.tipo_bien.clasificacion != None:
                # Rodados
                if self.tipo_bien.clasificacion == 0:
                    if self.modelo:
                        bien_json['modelo'] = self.modelo
            
                # Bonos, títulos y acciones
                if self.tipo_bien.clasificacion == 1:
                    if self.cant_acciones:
                        bien_json['cant_acciones'] = self.cant_acciones

                    if self.entidad:
                        bien_json['entidad'] = self.entidad

                    if self.ramo:
                        bien_json['ramo'] = self.ramo
            
                # Inmuebles
                if self.tipo_bien.clasificacion == 2:
                    if self.superficie:
                        bien_json['superficie'] = str(self.superficie)

                    if self.unidad_medida_id:
                        bien_json['unidad_medida'] = UNIDAD_MEDIDA[self.unidad_medida_id][1]

                    if self.valor_adq:
                        bien_json['valor_adq'] = str(self.valor_adq)

                    if self.m_valor_adq_id:
                        bien_json['moneda_valor_adq'] = TIPO_MONEDA[self.m_valor_adq_id][1]

                    if self.mejoras:
                        bien_json['mejoras'] = str(self.mejoras)

                    if self.direccion:
                        bien_json['direccion'] = self.direccion

                    if self.barrio:
                        bien_json['barrio'] = self.barrio

                    if self.localidad:
                        bien_json['localidad'] = self.localidad

                    if self.provincia:
                        bien_json['provincia'] = self.provincia
                        
        return json.dumps(bien_json, ensure_ascii=False).encode('utf8')
    
    def save(self, *args, **kwargs):
        self.nombre_bien_s = self.nombre_bien.nombre # lo usa la app rails pare evitar el join
        self.tipo_bien_s = self.tipo_bien.nombre # lo usa la app rails pare evitar el join
        super(Bien, self).save(*args, **kwargs)

    class Meta:
        db_table = 'biens'
        ordering = ['tipo_bien', 'nombre_bien']
        verbose_name_plural = 'bienes'
        verbose_name = 'bien'

    def __unicode__(self):
        if self.m_valor_fiscal_id:
            return "%s - %s - valor_fiscal: %s %s" % (self.tipo_bien, self.nombre_bien, TIPO_MONEDA[self.m_valor_fiscal_id][1], self.valor_fiscal)
        elif self.m_valor_adq_id:
            return "%s - %s - valor_adq: %s %s" % (self.tipo_bien, self.nombre_bien, TIPO_MONEDA[self.m_valor_adq_id][1], self.valor_adq)
        else:
            return "%s - %s" % (self.tipo_bien, self.nombre_bien)

class BienPersona(models.Model):
    """extra owners bien"""
    persona = models.ForeignKey("Persona", blank=True, null=True,)
    bien = models.ForeignKey("Bien")
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="<strong>NO</strong> incluir el signo '%'.<br> Si ingresa un número decimal use '.' (punto) como delimitador")
    vinculo = models.CharField(max_length=255, blank=True, choices=VINCULO, help_text="Indica la relacion con el titular de la DDJJ", default='Titular', verbose_name=u"vínculo con el declarante")
    class Meta:
        ordering = ['persona__apellido']
        verbose_name_plural = 'Titulares extras para este bien'

class Cargo(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    jurisdiccion = models.CharField(max_length=255, blank=True)
    cargo = models.CharField(max_length=255, blank=False, help_text="Nombre del cargo")
    poder_id = models.IntegerField(blank=False, null=True, choices=PODER, verbose_name="poder")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    personas = models.ManyToManyField(Persona, through='PersonaCargo', related_name="cargos")
    
    # def cargo_personas(self):
    #     return ', '.join([p.apellido for p in self.personas.all()])
    # cargo_personas.short_description = "Cargo Personas"

    class Meta:
        db_table = 'cargos'
        ordering = ['cargo']

    def __unicode__(self):
        return ("%s %s" % (self.cargo, PODER[self.poder_id][1] if self.poder_id else "")).title()


class Jurisdiccion(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255, blank=False, null=False)
    poder_id = models.IntegerField(blank=False, null=True , choices=PODER, verbose_name="poder")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'jurisdiccions'
        ordering = ['nombre']
        verbose_name_plural = 'Jurisdicciones'

    def __unicode__(self):
        return "%s" % self.nombre


class PersonaCargo(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    flag_ingreso = models.IntegerField(blank=True, null=True)
    ingreso = models.DateField(blank=True, null=True, help_text="DD/MM/AAAA")
    egreso = models.DateField(blank=True, null=True, help_text="DD/MM/AAAA")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # persona_id = models.IntegerField(blank=True, null=True)
    # cargo_id = models.IntegerField(blank=True, null=True)
    # jurisdiccion_id = models.IntegerField(blank=True, null=True)
    persona = models.ForeignKey("Persona")
    cargo = models.ForeignKey("Cargo")
    jurisdiccion = models.ForeignKey("Jurisdiccion", blank=True, null=True, verbose_name=u"organismo")
    
    class Meta:
        db_table = 'persona_cargos'
        ordering = ['cargo']
        verbose_name_plural = 'Persona Cargos'
    
    def __unicode__(self):
        return "%s - %s | ingreso: %s" % (self.persona, self.cargo, self.ingreso)
    
    def related_label(self):
        return u"%s - %s | ingreso: %s (%s)" % (self.persona, self.cargo, self.ingreso, self.id)
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "persona__id__iexact", "cargo__id__iexact", "persona__nombre__icontains", "persona__apellido__icontains", "cargo__cargo__icontains")


# hasta aca _______________________________________________________________



class TiempoControls(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dias = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tiempo_controls'


class ContenidoDdjjs(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    ddjj_id = models.IntegerField(blank=True, null=True)
    ddjj_ano = models.CharField(max_length=255, blank=True)
    ddjj_tipo = models.CharField(max_length=255, blank=True)
    poder_id = models.IntegerField(blank=True, null=True)
    persona_str = models.CharField(max_length=255, blank=True)
    persona_id = models.IntegerField(blank=True, null=True)
    cargo_str = models.CharField(max_length=255, blank=True)
    cargo_id = models.IntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contenido_ddjjs'


# class Vinculos(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     nombre = models.CharField(max_length=255, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         managed = False
#         db_table = 'vinculos'


# class Buscador(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     poder = models.IntegerField(blank=True, null=True)
#     nombre_bienes = models.TextField(blank=True)
#     personas = models.TextField(blank=True)
#     cargos = models.TextField(blank=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'buscadors'


# class DjVista(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     ddjj_id = models.IntegerField(blank=True, null=True)
#     visitas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'dj_vista'
