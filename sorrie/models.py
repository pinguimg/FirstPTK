import datetime

from django.db.models import ForeignKey
from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Dentist(models.Model):
    dentist_name = models.CharField(max_length=60)
    dentist_address = models.CharField(max_length=150)
    dentist_number = models.BigIntegerField(max_length=6)
    dentist_neigh = models.CharField(max_length=50)
    dentist_city = models.CharField(max_length=50)
    dentist_mobile = models.BigIntegerField(max_length=14)
    dentist_cro = models.BigIntegerField(max_length=6)
    pub_date = models.DateTimeField('date published')
    dentist_photo = models.ImageField(upload_to='sorrie/files/', null = True, blank = False)
    dentist_about = models.TextField(max_length=100, null = True)
    dentist_specialization = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.dentist_name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Post(models.Model):
    title = models.CharField(max_length=120)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True, db_index=True)
    content = models.TextField('Content')


    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('parent', 'slug',)
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
            slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
        return self.name


class Patient(models.Model):
    patient_name = models.CharField(max_length=60)
    patient_address = models.CharField(max_length=150)
    patient_number = models.BigIntegerField(max_length=6)
    patient_neigh = models.CharField(max_length=50)
    patient_city = models.CharField(max_length=50)
    patient_mobile = models.BigIntegerField(max_length=14)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.patient_name

# Create your models here.
