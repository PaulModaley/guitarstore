from django.shortcuts import render, HttpResponse, redirect

def subscribe(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    messages.success(
    request, 'Thank you for joining our newsletter mailing list')

    context = {
        'form' : form
    }
    return render(request, template, context)