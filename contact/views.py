from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact

from django.shortcuts import render

def contact(request):
	context ={}

	# create object of form
	form = ContactForm(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	template = 'contact/contact.html'
	context['form']= form
	return render(request, template, context)



# # Credit -> https://docs.djangoproject.com/en/4.0/topics/forms/
# def contact(request):
#     """View to render contact page"""
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             send_mail(
#                 f'Message from {name}, {email} about {subject}',
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [settings.EMAIL_HOST_USER]
#             )
#             messages.success(
#                 request, 'Your message has been sent!')
#             # redirect to contact page
#             return redirect(reverse('contact'))
#         else:
#             messages.error(
#                 request, 'There was a problem sending your message. \
#                     Please try again.')
#     else:
#         # Create a blank form
#         form = ContactForm()

#         template = 'contact/contact.html'
#         context = {
#             'form': form,
#         }
		
#     return render(request, template, context)