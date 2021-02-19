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
    image = models.ImageField(upload_to='events', blank=True, default=None)
    brochure = models.FileField(upload_to='brochure', blank=True, default=None, null = True)
    def __str__(self):
        return str(self.title)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image_url

# department 
program_type = (
    (1, 'Under Graduate'),
    (2, 'Post Graduate'),
   
)

dept = (
    (1, 'Physiology'),
    (2, 'Anatomy'),
    (3, 'Community Medicine'),
    (4, 'Tb & Chest Diseases'),
    (5, 'Paediatrics'),
    (6, 'Orthopaedics'),
    (7, 'Opthalmology'),
    (8, 'Psychiatry'),
    (9, 'Obstetrics & Gynaecology'),
    (10, 'General Surgery'),
    (11, 'Forensic Medicine'),
    (12, 'ENT'),
    (13, 'Dermatology'),
    (14, 'Dentistry'),
    (15, 'Anaesthesiology'),
    (16, 'Pharmacology'),
    (17, 'Bio Chemistry'),
    (18, 'Pathology'),
    (19, 'Micro Biology'),
    (20, 'Radio Diagnosis'),
    (21, 'General Medicine'),

   
)

class Department(models.Model):
    Name = models.PositiveIntegerField(
    choices=dept,
    default='1',
    )
    background_image= models.ImageField(upload_to='department', blank=False, default=None)
    vision= models.TextField(default=None)
    mission= models.TextField(default=None)
    program_type = models.PositiveIntegerField(
    choices=program_type,
    default='1',
    )
    duration = models.IntegerField(default=None, help_text='No of years')
    brochure = models.FileField(upload_to='department/brochure', blank=True, default=None)
    department_description= models.TextField(default=None)
    # achievement = models.ManyToManyField(Achieve, through='AttributeValue')
    def __str__(self):
        return str(self.Name)
        


class best_moments(models.Model):
    best_moment= models.ImageField(upload_to='department/best-moments', blank=False, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Best Moment'
        verbose_name_plural = 'Best Moments'

    def __str__(self):
        return str(self.pk)

class Achievement(models.Model):
    achievement = models.TextField(default=None, max_length=100)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return str(self.pk)

class Awards(models.Model):
    awards = models.TextField(default=None, max_length=100)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
    
    def __str__(self):
        return str(self.pk)

class HOD(models.Model):
    name = models.CharField(max_length=50, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='department/HOD', blank=False, default=None)
    Qualification_And_Specification = models.CharField(max_length=50, default=None)
    AreaOfIntrest = models.CharField(max_length=50, default=None)
    experience = models.IntegerField( default=None, null=True)
    email = models.EmailField()
    Phone = models.IntegerField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Head of the department'
        verbose_name_plural = 'Head of the department'

class Professor(models.Model):
    name = models.CharField(max_length=50, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    Qualification_And_Specification = models.CharField(max_length=50, default=None)
    AreaOfIntrest = models.CharField(max_length=50, default=None)
    email = models.EmailField()
    experience = models.IntegerField( default=None)
    Phone = models.IntegerField()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

class Facility(models.Model):
    name=models.CharField(max_length=50, default=None)
    quantity = models.IntegerField(default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
   


class Gallery(models.Model):
    image = models.ImageField(upload_to='department/gallery', blank=False, default=None)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return str(self.pk)



  
  

