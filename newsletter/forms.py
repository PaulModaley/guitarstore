# import form class from django
from django import forms
from .models import Subscribe

# create a ModelForm
class Subscribe(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Subscribe
		fields = "__all__"
