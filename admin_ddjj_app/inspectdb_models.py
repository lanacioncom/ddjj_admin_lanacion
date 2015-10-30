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

from django.db import models


# class Biens(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    # tipo_bien_id = models.IntegerField(blank=True, null=True)
    # nombre_bien_id = models.IntegerField(blank=True, null=True)
    # tipo_bien_s = models.CharField(max_length=255, blank=True)
    # nombre_bien_s = models.CharField(max_length=255, blank=True)
    # descripcion = models.CharField(max_length=255, blank=True)
    # direccion = models.CharField(max_length=255, blank=True)
    # barrio = models.CharField(max_length=255, blank=True)
    # localidad = models.CharField(max_length=255, blank=True)
    # provincia = models.CharField(max_length=255, blank=True)
    # pais = models.CharField(max_length=255, blank=True)
    # modelo = models.IntegerField(blank=True, null=True)
    # entidad = models.CharField(max_length=255, blank=True)
    # ramo = models.CharField(max_length=255, blank=True)
    # cant_acciones = models.CharField(max_length=255, blank=True)
    # fecha_desde = models.DateField(blank=True, null=True)
    # destino = models.CharField(max_length=255, blank=True)
    # origen = models.CharField(max_length=255, blank=True)
    # superficie = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # unidad_medida_id = models.IntegerField(blank=True, null=True)
    # m_mejoras_id = models.IntegerField(blank=True, null=True)
    # mejoras = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # m_valor_fiscal_id = models.IntegerField(blank=True, null=True)
    # valor_fiscal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # m_valor_adq_id = models.IntegerField(blank=True, null=True)
    # valor_adq = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # fecha_hasta = models.DateField(blank=True, null=True)
    # titular_dominio = models.CharField(max_length=255, blank=True)
    # porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # vinculo = models.CharField(max_length=255, blank=True)
    # periodo = models.CharField(max_length=255, blank=True)
    # obs = models.CharField(max_length=255, blank=True)
    # persona_id = models.IntegerField(blank=True, null=True)
    # ddjj_id = models.IntegerField(blank=True, null=True)
    # created_at = models.DateTimeField()
    # # updated_at = models.DateTimeField()

    # class Meta:
    #     managed = False
    #     db_table = 'biens'


# class Buscadors(models.Model):
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


# class Cargos(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     jurisdiccion = models.CharField(max_length=255, blank=True)
#     cargo = models.CharField(max_length=255, blank=True)
#     poder_id = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'cargos'


class ContenidoDdjjs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ddjj_id = models.IntegerField(blank=True, null=True)
    ddjj_ano = models.CharField(max_length=255, blank=True)
    ddjj_tipo = models.CharField(max_length=255, blank=True)
    poder_id = models.IntegerField(blank=True, null=True)
    persona_str = models.CharField(max_length=255, blank=True)
    persona_id = models.IntegerField(blank=True, null=True)
    cargo_str = models.CharField(max_length=255, blank=True)
    cargo_id = models.IntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contenido_ddjjs'


# class Ddjjs(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     ano = models.IntegerField(blank=True, null=True)
#     tipo_ddjj_id = models.IntegerField(blank=True, null=True)
#     funcionario = models.CharField(max_length=255, blank=True)
#     url = models.CharField(max_length=255, blank=True)
#     persona_cargo_id = models.IntegerField(blank=True, null=True)
#     persona_id = models.IntegerField(blank=True, null=True)
#     key = models.IntegerField(blank=True, null=True)
#     poder_id = models.IntegerField(blank=True, null=True)
#     clave = models.CharField(max_length=255, blank=True)
#     flag_presenta = models.IntegerField(blank=True, null=True)
#     obs = models.TextField(blank=True)
#     flag_search = models.CharField(max_length=255, blank=True)
#     visitas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'ddjjs'


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


# class Jurisdiccions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     nombre = models.CharField(max_length=255, blank=True)
#     poder_id = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'jurisdiccions'


# class NombreBiens(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     nombre = models.CharField(max_length=255, blank=True)
#     tipo_bien_id = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'nombre_biens'


# class PersonaCargos(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     persona_id = models.IntegerField(blank=True, null=True)
#     cargo_id = models.IntegerField(blank=True, null=True)
#     jurisdiccion_id = models.IntegerField(blank=True, null=True)
#     flag_ingreso = models.IntegerField(blank=True, null=True)
#     ingreso = models.DateField(blank=True, null=True)
#     egreso = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'persona_cargos'


# class Personas(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     apellido = models.CharField(max_length=255, blank=True)
#     nombre = models.CharField(max_length=255, blank=True)
#     legajo = models.CharField(max_length=255, blank=True)
#     tipo_documento_id = models.IntegerField(blank=True, null=True)
#     documento = models.IntegerField(blank=True, null=True)
#     cuit_cuil = models.CharField(max_length=255, blank=True)
#     nacimento = models.DateField(blank=True, null=True)
#     sexo_id = models.IntegerField(blank=True, null=True)
#     estado_civil_id = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     tag_id = models.CharField(max_length=255, blank=True)
#     tag_img_id = models.CharField(max_length=255, blank=True)
#     tag_descripcion = models.CharField(max_length=255, blank=True)
#     ficha_d_l = models.CharField(max_length=255, blank=True)

#     class Meta:
#         managed = False
#         db_table = 'personas'


# class SchemaMigrations(models.Model):
#     version = models.CharField(unique=True, max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'schema_migrations'


# class TiempoControls(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     dias = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'tiempo_controls'


# class TipoBiens(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     nombre = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_biens'


# class Vinculos(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     nombre = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'vinculos'
