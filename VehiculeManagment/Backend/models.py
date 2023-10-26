from django.db import models

# Create your models here.

class Vehicule(models.Model):
    """Model definition for Vehicule."""
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    number_plate = models.CharField(max_length=10)

    class Meta:
        """Meta definition for Vehicule."""

        verbose_name = 'Vehicule'
        verbose_name_plural = 'Vehicules'

    def __str__(self):
        """Unicode representation of Vehicule."""
        return self.model + " " + self.brand + " " + self.number_plate
    

class FullTank(models.Model):
    """Model definition for FullTank."""
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()
    liters = models.FloatField()
    kilometers = models.IntegerField()
    profile = models.CharField(max_length=50)

    class Meta:
        """Meta definition for FullTank."""

        verbose_name = 'FullTank'
        verbose_name_plural = 'FullTanks'

    def __str__(self):
        """Unicode representation of FullTank."""
        return str(self.vehicule) + " " + str(self.date) + " " + str(self.price) + " " + str(self.liters)
    

class Intervention(models.Model):
    """Model definition for Intervention."""
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()
    kilometers = models.IntegerField()
    profile = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Intervention."""

        verbose_name = 'Intervention'
        verbose_name_plural = 'Interventions'

    def __str__(self):
        """Unicode representation of Intervention."""
        return str(self.vehicule) + " " + str(self.date) + " " + str(self.price) + " " + str(self.kilometers)