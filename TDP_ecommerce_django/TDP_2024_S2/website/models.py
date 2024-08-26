from django.db import models
import itertools

class ClientRequest(models.Model):
    client_id = models.CharField(max_length=10, unique=True, editable=False)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    current_date = models.DateField()
    product_type = models.CharField(max_length=50)
    product_details = models.TextField()
    key_words = models.TextField()
    most_views = models.BooleanField(default=False)
    newest = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.client_id:
            #this will genarate a new client id
            last_client = ClientRequest.objects.order_by('id').last()
            if last_client:
                last_id = int(last_client.client_id.replace('Client ', ''))
                new_id = last_id + 1
            else:
                new_id = 1
            self.client_id = f"Client {new_id}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.client_id} - {self.product_type} request on {self.current_date}"
    
class Seller(models.Model):
    image = models.ImageField(upload_to='images/')

