from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=50)
    campus = models.CharField( max_length=50)
    class Meta:
        db_table="person"
    def __str__(self):
        return self.name

class Field(models.Model):
    name=models.CharField(max_length=50, primary_key=True)
    campus = models.CharField(max_length=20)
    area = models.CharField(max_length=1000)
    class Meta:
        db_table="field"
    def __str__(self):
        return self.name