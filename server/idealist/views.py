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

def idea_detail(request, idea_id):
    '''
    Read(R)
    특정 아이디어를 불러와서 상세정보를 보여준다
    '''
    idea = Idea.objects.get(id=idea_id)
    ctx = {'idea': idea}

    return render(request, template_name='idealist/detail.html', context=ctx)