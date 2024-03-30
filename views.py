from django.shortcuts import render
from .models import Reader

def reader_info(request):
    if request.method == 'POST':
        # Assuming you have a form to collect reader's data
        name = request.POST.get('name')
        email = request.POST.get('email')
        reader = Reader.objects.create(name=name, email=email)
        return render(request, 'reader/info_success.html', {'reader': reader})
    return render(request, 'reader/info_form.html')