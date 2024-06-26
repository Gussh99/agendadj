from .models import Person, Reunion, Hobby
from rest_framework import serializers,pagination

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required = False)

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')

class PersonaSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default = False)
    class Meta:
        model = Person
        fields = ('__all__')

class PersonaSerializer3(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True)
    class Meta:
        model = Person
        fields = ('__all__')

class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer3()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )

class ReunionSerializer2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )

    def get_fecha_hora(self, obj):
        return str(obj.fecha)+' - '+ str(obj.hora)
    
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )
        #para generar link a cada una persona
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:detalle', 'lookup_field': 'pk'}
        }

    def get_fecha_hora(self, obj):
        return str(obj.fecha)+' - '+ str(obj.hora)


class PersonPagination (pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

class ReunionesByJobSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()