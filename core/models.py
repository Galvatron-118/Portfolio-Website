from django.db import models

# Create your models here.
# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
    
#Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")
    image = models.ImageField(upload_to='clients',null=True,blank=True)

    
    def __str__(self):
        return self.name

#Recent Work Model
class RecentWork(models.Model):
    num = models.CharField(max_length=100, null=True, verbose_name="Work Number")
    title = models.CharField(max_length=100, verbose_name="Work Title")
    image = models.ImageField(upload_to="clients", default="default.png")
    url = models.CharField(max_length=100, null=True, verbose_name="Work url")
    
    def __str__(self):
        return self.title

#blogs model  
class Blog(models.Model):
    name = models.TextField(max_length=1000, verbose_name="Blog Title")
    author = models.CharField(max_length=100, verbose_name="Author Name")
    time = models.DateTimeField()
    description = models.TextField(verbose_name="Blog Description")
    image = models.ImageField(upload_to="blogs", default="default.png")
    
    def __str__(self):
        return self.name

#Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact Name")
    email = models.EmailField(verbose_name="Contact Email")
    message = models.TextField(max_length=1000, verbose_name="Conatact Message")
   
    def __str__(self):
        return self.name
