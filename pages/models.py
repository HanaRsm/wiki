from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=120)
	content = models.CharField(max_length=120)
	last_update = models.DateTimeField(auto_now=False, auto_now_add=False)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('page-detail', kwargs={"page_id":self.id})