from django.db import models
from django.core.urlresolvers import reverse
from .python import services 


class Item(models.Model):
	make_and_model = models.CharField(max_length=200)
	label = models.CharField(max_length=200)
	notes = models.TextField()
	checked_out = models.BooleanField()

	def __str__(self):
		return self.make_and_model

	def get_absolute_url(self):
		return reverse('inventory:detail', kwargs = {'pk' : self.pk})

class Loaner(models.Model): 
	item = models.ForeignKey(Item)
	net_id = models.CharField(max_length=200)

	def get_matchname(self):
		return re.sub("\W+" , "", net_id.lower())

	def __str__(self):
		return self.net_id

	name = services.display_name(get_matchname())


	def get_absolute_url(self):
		return reverse('inventory:detail', kwargs = {'pk' : self.item.pk})
