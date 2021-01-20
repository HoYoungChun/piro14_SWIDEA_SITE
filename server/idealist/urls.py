from django.urls import path
from . import views

app_name = 'idealist'

urlpatterns = [
    path('', view=views.idea_list, name='idealist'),
]