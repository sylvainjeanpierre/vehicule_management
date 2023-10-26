from Backend.models import Vehicule, FullTank, Intervention
from rest_framework import serializers

class VehiculeSerializer(serializers.HyperlinkedModelSerializer):

    fullTankIds = serializers.SerializerMethodField()
    interventionsIds = serializers.SerializerMethodField()

    class Meta:
        model = Vehicule
        fields = ['brand', 'model', 'year', 'number_plate', 'fullTankIds', 'interventionsIds']

    def get_fullTankIds(self, obj):
        # Get the IDs of related FullTank objects for the current vehicle
        full_tanks = FullTank.objects.filter(vehicule=obj.id)
        return [full_tank.id for full_tank in full_tanks]
    
    def get_interventionsIds(self, obj):
        # Get the IDs of related Intervention objects for the current vehicle
        interventions = Intervention.objects.filter(vehicule=obj.id)
        return [intervention.id for intervention in interventions]


class FullTankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullTank
        fields = ['vehicule', 'date', 'price', 'liters', 'kilometers', 'profile']


class InterventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intervention
        fields = ['vehicule', 'date', 'price', 'kilometers', 'profile']
