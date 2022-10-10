from pickle import TRUE
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

class Studentdetail(models.Model):
    Student_name = models.CharField(max_length=20)
    Class = models.CharField(max_length=10)
    roll_no = models.IntegerField(primary_key=TRUE)


    def __str__(self):
        return self.Student_name

