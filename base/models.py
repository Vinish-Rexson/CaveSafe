from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_id = models.AutoField
    image = models.ImageField(upload_to="images/user_img")
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField((""), auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=300, default="")
    phone_no = models.IntegerField()
    allergies = models.CharField(max_length=100)
    current_medications = models.CharField(max_length=100, default="")
    blood_group = models.CharField(max_length=4, default="")
    desc = models.CharField(max_length=300)
    user_id = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
