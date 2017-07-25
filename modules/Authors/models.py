from django.db import models

GENDER = (
    ("M","Masculino"),
    ("F","Femenino")
)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    gender = models.CharField(max_length=20,choices=GENDER)
    age = models.IntegerField()
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return "Author: %s %s" % (self.name,self.last_name)

