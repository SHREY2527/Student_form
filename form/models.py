from django.db import models

class user(models.Model):
    Student_name=models.CharField(max_length = 20)
    Class = models.CharField(max_length=10)
    roll_no = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.Student_name