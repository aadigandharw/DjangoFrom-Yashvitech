from django.db import models

# class Registration(models.Model):
#     name = models.CharField(max_length=50)
#     user_class = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=50)


# class StudentLogin(models.Model):
#     s_name = models.CharField(max_length=50)
#     s_city = models.CharField(max_length=20)
#     s_class = models.CharField(max_length=10)
    


from django.contrib.auth.models import AbstractUser

class  MyUser(AbstractUser):
    roles=(('user','User'),('admin','Admin'))

    role = models.CharField(max_length=100,choices=roles,default='user')
    address = models.TextField()

    def save(self,*args,**Kwargs):
        if self.is_superuser == True:
            self.role = 'admin'
        super().save(*args,**Kwargs)
