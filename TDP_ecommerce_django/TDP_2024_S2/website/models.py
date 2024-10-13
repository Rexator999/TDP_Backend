from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime

class ClientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='client_group', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='clients_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email

class ClientRequest(models.Model):
    request_id = models.CharField(max_length=10, unique=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    request_date = models.DateField(default=datetime.date.today)
    end_date = models.CharField(max_length=11)
    product_type = models.CharField(max_length=50)
    product_details = models.TextField()
    key_words = models.TextField()
    product_con = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.request_id:
            last_request = ClientRequest.objects.order_by('id').last()
            if last_request:
                last_id = int(last_request.request_id.replace('Request ', ''))
                new_id = last_id + 1
            else:
                new_id = 1
            self.request_id = f"Request {new_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.request_id} - {self.product_type} request on {self.request_date}"

class SellerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        seller = self.model(email=email, **extra_fields)
        seller.set_password(password)
        seller.save(using=self._db)
        return seller

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Seller(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = SellerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Adding related_name to prevent clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='seller_group',  # Change this to a unique name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='sellers_permissions',  # Change this to a unique name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email

# Seller Product Model
class SellerProduct(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    key_words = models.TextField()
    product_id = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product = SellerProduct.objects.order_by('id').last()
            if last_product:
                last_id = int(last_product.product_id.replace('Product ID ', ''))
                new_id = last_id + 1
            else:
                new_id = 1
            self.product_id = f"Product ID {new_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id}"