from django.db import models
from django.contrib.auth.models import User

class BaitType(models.Model):
    bait_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    fresh = models.BooleanField(default=False)
    salt = models.BooleanField(default=False)
    def __str__(self):
        return f"Bait {self.bait_id}"

class BodyOfWater(models.Model):
    bow_id = models.AutoField(primary_key=True, unique=True)
    lng = models.FloatField()
    lat = models.FloatField()
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f"Water {self.bow_id}"
    
    
class FishType(models.Model):
    fish_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    fresh = models.BooleanField(default = False)
    salt = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Type of Fish: {self.name} Fresh Water? {self.fresh} Salt Water {self.salt}"
    
class FishingLog(models.Model):
    catch_id = models.AutoField(primary_key=True)
    fish_id = models.ForeignKey(FishType, on_delete=models.CASCADE)
    bait_id = models.ForeignKey(BaitType, on_delete=models.CASCADE)
    bow_id = models.ForeignKey(BodyOfWater, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caught_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Catch {self.catch_id} by {self.uid}"