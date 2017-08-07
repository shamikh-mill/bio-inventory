from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    make_and_model = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    notes = models.TextField()
    checked_out = models.BooleanField()

    def __str__(self):
    	return self.make_and_model

    # def get_absolute_url(self):
    #     return reverse('inventory:detail', kwargs = {'pk' : self.pk})


class Loaner(models.Model): 
	item = models.ForeignKey(Item)
	net_id = models.CharField(max_length=200)

	def __str__(self):
		return self.net_id