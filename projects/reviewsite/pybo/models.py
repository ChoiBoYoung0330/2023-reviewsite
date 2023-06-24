from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class basic_info(models.Model):
    title = models.CharField(max_length=50)
    poster_src = models.ImageField(blank=True, null=True, upload_to='pybo')
    open_date = models.DateField()
    total_score = models.FloatField()
    
    def __str__(self):
        return self.title

class detail_info(models.Model):
    title = models.ForeignKey(basic_info, on_delete=models.CASCADE)
    synopsis = models.TextField()
    actor = models.TextField()
    #netflix_url = models.TextField()
    #youtube_url = models.TextField()
    netflix_url = EmbedVideoField()
    youtube_url = EmbedVideoField()
    
class graph(models.Model):
    title = models.ForeignKey(basic_info, on_delete=models.CASCADE)
    tf_idf_word = models.TextField()
    tf_idf_score = models.FloatField()

class review_info(models.Model):
    title = models.ForeignKey(basic_info, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    # review2 = models.TextField(null=True)
    review_score = models.FloatField()