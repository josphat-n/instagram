from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('insta.urls')),
    url(r'^accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]