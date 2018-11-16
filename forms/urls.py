from django.urls import path
from .forms import FirstForm, SecondForm, ThirdForm
from .views import FormWizard
from . import views

named_forms = (
    ('first', FirstForm),
    ('second', SecondForm),
    ('third', ThirdForm)
)

form_wizard = FormWizard.as_view(named_forms,
    url_name='form_step', done_step_name='result')

urlpatterns = [
    path('forms/<step>/', form_wizard, name='form_step'),
    path('', views.index, name='index'),
]