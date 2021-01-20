from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea
from .forms import IdeaForm

# Create your views here.


def idea_list(request):
    '''
    Read(R)
    아이디어들을 불러와서 리스트형태로 보여준다
    '''
    ideas = Idea.objects.all()  # 이 부분이 READ
    ctx = {'ideas': ideas}
    return render(request, template_name='idealist/list.html', context=ctx)