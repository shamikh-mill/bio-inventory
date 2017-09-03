from rest_framework import serializers
from .models import Item, Loaner

class ItemSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Item 
		fields = '__all__'