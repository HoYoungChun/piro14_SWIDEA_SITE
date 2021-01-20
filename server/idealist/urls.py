from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', view=views.idea_list, name='idealist'),
    path('idea/<int:idea_id>/', view=views.idea_detail, name='detail'),
    path('idea/create/', view=views.create_idea, name='create'),
    path('idea/update/<int:idea_id>/', view=views.idea_update, name='update'),
    path('idea/delete/<int:idea_id>/', view=views.idea_delete, name='delete'),

    path('devtool/create/', view=views.create_tool, name='create_tool'),
    path('devtool/', view=views.devtool_list, name='devtoollist'),
    path('devtool/<int:tool_id>/', view=views.devtool_detail, name='devtooldetail'),

    path('devtool/delete/<int:tool_id>/', view=views.tool_delete, name='tool_delete'),
]