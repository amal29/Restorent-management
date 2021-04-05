from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,email,profile,phone,username,password=None):
        if not email:
            raise ValueError("email is required")
        
        if not phone:
            raise ValueError("Please provide active phone number")
        if not username:
            raise ValueError("User name is required")

        user=self.model(
           email=self.normalize_email(email),
           username=username,
           phone=phone,
           profile=profile,



        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,phone,password=None):
        user=self.create_user(
            email=email,
            username=username,
            
            phone=phone,
            password=password
        )    
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser):
    profile = models.ImageField(upload_to='booking')
    username=models.CharField(verbose_name='user name',max_length=60)
    email=models.EmailField(verbose_name="email address", max_length=60,unique=True)
    phone=models.CharField(verbose_name="Mobile number",max_length=20)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","phone","profile"]
    objects=MyUserManager()
    

    def __str__(self):
        return self.username


    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True 

        
                      
class Room(models.Model):
    ROOM_CATEGORIES=(
    ('YAC','AC'),
    ('NAC','NON-AC'),
    ('DEL','DELUX'),
    ('KIN','KING'),
    ('QUE','QUEEN')

    )
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    category=models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    beds=models.IntegerField()
    capacity=models.IntegerField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f'{self.number}.{self.category} with {self.beds} beds for {self.capacity} people'







class Booking(models.Model):
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    check_in=models.DateTimeField(null=True, blank=True)
    check_out=models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='booking')


    def __str__(self):
        return f'{self.user}  has booked {self.room} Room from {self.check_in} to {self.check_out}'
