from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    embed_code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default= 0)



    def __str__(self):
        return self.title
