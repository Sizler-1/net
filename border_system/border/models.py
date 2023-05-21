from django.db import models

class BorderCrossing(models.Model):
    name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=8)
    date_of_birth = models.DateField()
    crossing_date = models.DateTimeField(auto_now_add=True)
    nationality = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()



class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    date_administered = models.DateField()
    border_crossing = models.ForeignKey(BorderCrossing, on_delete=models.CASCADE)

from django.core.validators import MinValueValidator, MaxValueValidator

class VaccineRecord(models.Model):
    traveler = models.ForeignKey('border.BorderCrossing', on_delete=models.CASCADE)
    vaccine = models.ForeignKey('border.Vaccine', on_delete=models.CASCADE)
    date_administered = models.DateField()
    dose_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])

    def __str__(self):
        return f'{self.traveler.name} - {self.vaccine.name} - Dose {self.dose_number}'