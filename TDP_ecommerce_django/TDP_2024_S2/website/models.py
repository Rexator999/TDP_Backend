from django.db import models
import itertools
import datetime

class Client(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class ClientRequest(models.Model):
    request_id = models.CharField(max_length=10, unique=True, editable=False)
    client = models.CharField(max_length=100)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    request_date = models.DateField( default=datetime.date.today)
    end_date = models.CharField(max_length=11)
    product_type = models.CharField(max_length=50)
    product_details = models.TextField()
    key_words = models.TextField()
    most_views = models.BooleanField(default=False)
    newest = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.request_id:
            #this will genarate a new client id
            last_client = ClientRequest.objects.order_by('id').last()
            if last_client:
                last_id = int(last_client.request_id.replace('Request ', ''))
                new_id = last_id + 1
            else:
                new_id = 1
            self.request_id = f"Request {new_id}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.request_id} - {self.product_type} request on {self.request_date}"
    
class Seller(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    
    
class SellerProduct(models.Model):
    seller = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    product_id = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.product_id:
            #this will genarate a new client id
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

