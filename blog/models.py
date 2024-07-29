from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

#blogs/1.jpeg
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=False,unique=True,db_index=True,editable=True) 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            counter = 1
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
        
    def __str__(self) :
      return f"{self.name}"
        
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=True)
    categories = models.ManyToManyField(Category)    
    
    def __str__(self) :
        return f"{self.title}" 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    #abc.com/category/elektronik/beyaz-esya
    

        