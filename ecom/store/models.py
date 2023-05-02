from django.db import models

# Create your models here.
class cata(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    images=models.ImageField(upload_to="imagess",null=False,blank=False)
    staus=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trend=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    def __str__(self):
        return self.name
    
class prod(models.Model):
    category=models.ForeignKey(cata,on_delete=models.CASCADE)
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    product_images=models.ImageField(upload_to="imagess",null=False,blank=False)
    description=models.CharField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    staus=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trend=models.BooleanField(default=False,help_text="0=default,1=Trending")
    
    def __str__(self):
        return self.name