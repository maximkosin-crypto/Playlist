from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    picture = models.ImageField(upload_to="images/")
    likes = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title