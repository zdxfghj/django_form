from django.shortcuts import render
from .models import Artiles
from .forms import ArticleForm
from django.core.mail import send_mail
from django.conf import settings

def forms_create(request):
    error = ""
    if request.method == 'POST':
        message = 'Ваша форма находится в обработке'
        email = request.POST['email']
        name = request.POST['first_name']
        send_mail(name, message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Форма была неверной"

    form = ArticleForm()
    return render(request, 'form/form.html', {'form': form, 'error': error})


def forms_view(request):
    form = Artiles.objects.all()
    # ...object.order_by('-date')[:1]
    return render(request, 'form/form_view.html', {'forms': form})