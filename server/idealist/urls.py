from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', view=views.idea_list, name='idealist'),
    path('idea/<int:idea_id>/', view=views.idea_detail, name='detail'),
    path('idea/create/', view=views.create_idea, name='create'),
    path('devtool/create/', view=views.create_tool, name='create_tool'),
    path('devtool/', view=views.devtool_list, name='devtoollist'),
]