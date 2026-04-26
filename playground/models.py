from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Create your models here.
class Product(models.Model):
    
    title  = models.CharField(max_length=255) #text 
    slug  = models.SlugField(unique=True , blank = True)
    
    price = models.DecimalField(max_digits = 6 ,decimal_places =2) #number
    description = models.TextField() #unlimited text
    created_at = models.DateTimeField(auto_now_add=True) #date time
    tags = models.ManyToManyField(Tag , blank=True)
    SIZE_CHOICES = [
        
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    #cascasde is defined to say that if category is dleted then delet all its products tooo

    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    inventory = models.IntegerField(default=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category ,on_delete= models.CASCADE , null= True)
   
    updated_at = models.DateTimeField(auto_now=True)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args , **kwargs)
    


    def __str__(self): #shows how your object looks
        return self.title
    

    # we use migrartions in django to make relations to the dtatabse 
    #django doesnt even touch databas3e until you use migration


