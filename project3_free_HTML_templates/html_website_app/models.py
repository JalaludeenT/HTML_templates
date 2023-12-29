from django.db import models


# Create your models here.
class News(models.Model):
    News_Title = models.CharField(max_length=250)
    News_Date = models.DateField()
    News_Description = models.TextField()
    News_Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.News_Title
