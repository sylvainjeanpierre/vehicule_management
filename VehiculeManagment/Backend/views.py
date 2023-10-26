from django.shortcuts import render
from Backend.models import Vehicule, FullTank, Intervention
from Backend.serializers import VehiculeSerializer, FullTankSerializer, InterventionSerializer
from rest_framework import viewsets

# Create your views here.

class VehiculeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer


class FullTankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FullTank.objects.all()
    serializer_class = FullTankSerializer

class InterventionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer


class FullTankIDViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows full tanks to be viewed or edited by the vehicule ID.

    @param vehicule_id: the vehicule ID from GET request
    """
    serializer_class = FullTankSerializer

    def get_queryset(self):
        """
        This view should return a list of all the full tanks
        for the vehicule as determined by the vehicule ID portion of the URL.
        """
        vehicule_id = self.kwargs['vehicule_id']
        return FullTank.objects.filter(vehicule=vehicule_id)


class IntervetionIDViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interventions to be viewed or edited by the vehicule ID.

    @param vehicule_id: the vehicule ID from GET request
    """
    serializer_class = InterventionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the interventions
        for the vehicule as determined by the vehicule ID portion of the URL.
        """
        vehicule_id = self.kwargs['vehicule_id']
        return Intervention.objects.filter(vehicule=vehicule_id)
    
