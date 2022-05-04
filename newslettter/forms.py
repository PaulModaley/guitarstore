# import form class from django
from django import forms
from .models import Newsletter

# create a ModelForm
class Add_Subscriber(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Newsletter
		fields = "__all__"
