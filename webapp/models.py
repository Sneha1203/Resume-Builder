from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Skill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    s_name  = models.CharField(max_length=500)
    s_level  = models.CharField(max_length=500)

    def __str__(self):
        return self.user.s_name


class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    e_office  = models.CharField(max_length=500)
    e_position  = models.CharField(max_length=500)
    e_duration  = models.CharField(max_length=500)

    def __str__(self):
        return self.user.s_name


class Academic(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    a_institution  = models.CharField(max_length=500)
    e_year  = models.IntegerField(max_length=500)
    e_award  = models.CharField(max_length=500)

    def __str__(self):
        return self.user.a_institution
    

class Referees(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    r_name  = models.CharField(max_length=500)
    r_email  = models.EmailField(max_length=500)
    r_phone  = models.IntegerField(max_length=500)

    def __str__(self):
        return self.user.r_name
    

class Profile(models.Model):
    GENDER_CHOICES = [
        
    ]
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    fname  = models.CharField(max_length=500)
    lname  = models.CharField(max_length=500)
    mname  = models.CharField(max_length=500)
    gender  = models.CharField(max_length=500)
    age  = models.IntegerField(max_length=100)
    country  = models.CharField(max_length=500)
    street  = models.CharField(max_length=500)
    email  = models.EmailField(max_length=500)
    phone  = models.IntegerField(max_length=10)
    occupation  = models.CharField(max_length=500)
    dob  = models.DateField(default='None')
    bio  = models.TextField()
    avatar = models.ImageField(upload_to='profile/', default='profile/avatar.png', null=True)

    def __str__(self):
        return self.user.fname
    
    def delete(self, *args, **kwargs):
        self.avatar.delete()
        super().delete(*args, **kwargs)
