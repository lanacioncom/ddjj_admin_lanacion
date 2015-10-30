from rest_framework import serializers
from admin_ddjj_app.models import Persona, PersonaCargo, Ddjj, Bien, TipoBien

class DDJJSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='get_tipo_ddjj', read_only=True)
    flag_presenta = serializers.BooleanField(source='get_flag_presenta', read_only=True)
    poder = serializers.CharField(source='get_poder', read_only=True)
    cargo = serializers.CharField(source='get_cargo', read_only=True)
    
    class Meta:
        model = Ddjj
        fields = ('id', 'tipo', 'ano', 'url',
                  'flag_presenta', 'obs', 'visitas',
                  'poder', 'cargo', 'status')
        
class PersonaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='get_nombre_apellido', read_only=True)
    ddjjs_count = serializers.IntegerField(source='get_ddjjs_total', read_only=True)
    
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'ddjjs_count')

class PersonaDDJJSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='get_nombre_apellido', read_only=True)
    cargo_desde = serializers.CharField(source='get_cargo_publico_desde', read_only=True)
    ddjjs = DDJJSerializer(many=True, read_only=True)
    
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'legajo', 'tag_id', 'ddjjs', 'cargo_desde')

class TipoBienSerializer(serializers.ModelSerializer):
    clasificacion = serializers.CharField(source='get_clasificacion', read_only=True)
    class Meta:
        model = TipoBien
        fields = ('nombre', 'clasificacion')
    

class DDJJBienSerializer(serializers.ModelSerializer):
    unidad_medida = serializers.CharField(source='get_unidad_medida', read_only=True)
    mejoras_moneda_tipo = serializers.CharField(source='get_mejoras_moneda_tipo', read_only=True)
    valor_fiscal_moneda_tipo = serializers.CharField(source='get_valor_fiscal_moneda_tipo', read_only=True)
    valor_adq_moneda_tipo = serializers.CharField(source='get_valor_adq_moneda_tipo', read_only=True)
    tipo_bien = TipoBienSerializer(read_only=True)
    persona = PersonaSerializer(read_only = True)
    
    class Meta:
        model = Bien
        fields = ('descripcion', 'direccion', 'barrio', 'localidad', 'provincia', 'pais',
                  'modelo', 'entidad', 'ramo', 'cant_acciones', 'fecha_desde', 'destino',
                  'origen', 'superficie', 'unidad_medida', 'mejoras_moneda_tipo', 'mejoras',
                  'valor_fiscal_moneda_tipo', 'valor_fiscal', 'valor_adq_moneda_tipo', 'valor_adq',
                  'fecha_hasta', 'titular_dominio', 'porcentaje', 'vinculo', 'periodo',
                  'obs', 'tipo_bien', 'nombre_bien_s', 'persona',)
        
