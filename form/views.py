from django.shortcuts import render
from .models import FeedBack
from .forms import ArticleForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import FUND_US_CHOICES,SERVICE_CHOICES
from django.utils.safestring import SafeString


def forms_create(request):
    if request.method == 'POST':
        message = 'Ваша форма находится в обработке'
        email = request.POST['email']
        name = request.POST['first_name']
        send_mail(name, message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form/view/success')
        else:
            return render(request, 'form/form.html', {'form': form})
    else:
        pass


def forms_view(request):
    form_list = FeedBack.objects.all()

    social_media_array = []
    social_media_array.append(['Task', 'Hours per Day'])
    for fund, fund_info in FUND_US_CHOICES:
        social_current_array = [fund, form_list.filter(info=fund).count()]
        social_media_array.append(social_current_array)

    service_type_array = []
    service_type_array.append(['Task', 'Hours per Day'])
    for fund, fund_info in SERVICE_CHOICES:
        service_current_array = [fund, form_list.filter(service_type=fund).count()]
        service_type_array.append(service_current_array)

    return render(request, 'form/form_view.html', {'forms': form_list, 'social_media_array': SafeString(social_media_array),'service_type_array': SafeString(service_type_array)})


def form_view_success(request):
    return render(request, 'form/form_view_success.html')
