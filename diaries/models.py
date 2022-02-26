import imp
from statistics import mode
from unicodedata import category
from django.db import models
from django.utils import timezone
from numpy import mintypecode

# Create your models here.
class Diary(models.Model):
    category = models.CharField('カテゴリ', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return 'カテゴリ:{} 本文:{}'.format(self.category, self.text[:10])