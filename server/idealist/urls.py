from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', view=views.idea_list, name='idealist'),
    path('idea/<int:idea_id>/', view=views.idea_detail, name='detail'),
]