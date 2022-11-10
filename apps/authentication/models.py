from django.db import models

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class District(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    

    def __self__(self):
        return self.name


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150, unique=True)
    profile = models.TextField()
    # state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    # district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name 

