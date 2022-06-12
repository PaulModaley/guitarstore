from django.shortcuts import render


def error_404(request, exception):
    """This method handles 404 errors"""
    data = {}
    return render(request,'404.html', data)



def error_500(request):
    """This method handles 500 errors"""
    data = {}
    return render(request,'500.html', data)