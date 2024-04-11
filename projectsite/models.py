from django.db import models
from django.db import connections

# Create your models heres


class passengerDetail(models.Model):
    name = models.CharField(db_column="name", max_length=100)
    age = models.IntegerField(db_column="age")
    gender = models.CharField(db_column="gender", max_length=6)
    mobile = models.IntegerField(db_column="mobile")
    email = models.EmailField(db_column="email", max_length=30)
    date = models.CharField(db_column="date", max_length=12)
    source = models.CharField(db_column="source", max_length=50)
    destination = models.CharField(db_column="destination", max_length=50)
    imagepath = models.CharField(db_column="imagepath", max_length=50)

    class Meta:
        db_table = "passenger_detail"

