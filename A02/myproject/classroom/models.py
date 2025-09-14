from django.db import models

# Create your models here.
class RoomData(models.Model):
    room_code = models.CharField(max_length=6)
    room_name = models.CharField(max_length=10)
    room_capacity = models.IntegerField()
    room_hour = models.IntegerField()
    room_available = models.BooleanField()

    #String repretentation of the tour
    def __str__(self):
        return (f"ID:{self.id} Room name : {self.room_name} code : {self.room_code} Capacity : {self.room_capacity} hours : {self.room_hour} Available : {self.room_available}" )