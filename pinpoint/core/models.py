from django.db import models
from django.contrib import admin
from django.forms import ModelChoiceField
from django.contrib.auth.models import User

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(default='----', max_length=256)
    lat = models.FloatField(max_length=25, default=0.0,unique=True)
    long = models.FloatField(max_length=25, default=0.0,unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"Pos_id: {self.id}"
        

class Operator(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #now_lat = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='lat',related_name='now_lat', null=True, blank=True)
    #now_long = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='long',related_name='now_long', null=True, blank=True)
    n_lat = models.FloatField(max_length=25, default=0.0)
    n_long = models.FloatField(max_length=25, default=0.0)
    delivery_id = models.ForeignKey('Delivery', on_delete=models.SET_NULL, to_field='id',related_name='operator', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Operator/id: {self.user.username, self.id}"

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    operator_id = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='deliveries', null=True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='id', related_name='position_id', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(default='-Description here-')
    s_lat = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='lat', related_name='s_lat', null=True)
    s_long = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='long', related_name='s_long', null=True)
    e_lat = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='lat', related_name='e_lat', null=True)
    e_long = models.ForeignKey(Position, on_delete=models.CASCADE, to_field='long', related_name='e_long', null=True)
    def save(self, *args, **kwargs):
        if self.description == '-Description here-' or self.description == '':
            start_address = f"{self.s_lat.address}"
            end_address = f"{self.e_lat.address}"
            self.description = f"Starting address: {start_address};\n Ending address: {end_address}"
        else:
            start_address = f"{self.s_lat.address}"
            end_address = f"{self.e_lat.address}"
            self.description = f"{self.description}\n; Starting address: {start_address};\n Ending address: {end_address}"
        
        super(Delivery, self).save(*args, **kwargs)

    def __str__(self):
        return f"Delivery-id: { self.id }"