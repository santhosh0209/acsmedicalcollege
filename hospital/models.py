from django.db import models

#news
class New(models.Model):
    news= models.TextField(default=None)
    date = models.DateField()
    image = models.ImageField(upload_to='news', blank=True, default=None)
    brochure = models.ImageField(upload_to='brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.date)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url
# events
class Event(models.Model):
    title = models.CharField(max_length=50, default=None)
    description= models.TextField(default=None)
    date = models.DateField()
    image = models.ImageField(upload_to='events', blank=False, default=None)
    brochure = models.FileField(upload_to='brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.title)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url

class indexvideo(models.Model):
    Video_Title= models.CharField(max_length=500, default=None)
    Video_Description= models.TextField(max_length=500, default=None)
    bg_file= models.ImageField(upload_to='hospital/videos', null=True, verbose_name="Background image ")
    videofile= models.FileField(upload_to='hospital/videos', null=True, verbose_name="video")

    def __str__(self):
        return str(self.Video_Title)

class gallery(models.Model):
    image = models.ImageField(upload_to='hospital/gallery', blank=False, default=None)
    title = models.CharField(max_length=50,default= None, null=False )
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Hospital Gallery'
        verbose_name_plural = 'Hospital Gallery'

