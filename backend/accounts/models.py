from django.db import models


# Create your models here.    
class UserBodyInfo(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    general = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class BodyInfoRecord(models.Model):
    user_body_info = models.ForeignKey(UserBodyInfo, on_delete=models.CASCADE, related_name="records")
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    general = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
