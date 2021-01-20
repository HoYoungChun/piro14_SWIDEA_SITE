from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea,DevTool
from .forms import IdeaForm,DevToolForm

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

def create_idea(request):
    '''
    Create(C)
    포스트를 새로 생성한다
    request method ==> GET(url입력), POST(저장하기) 생활코딩 보기
    '''
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idealist')
    else:
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, template_name='idealist/idea_form.html', context=ctx)

def devtool_list(request):
    '''
    Read(R)
    아이디어들을 불러와서 리스트형태로 보여준다
    '''
    tools = DevTool.objects.all()  # 이 부분이 READ
    ctx = {'tools': tools}
    return render(request, template_name='idealist/tool_list.html', context=ctx)

def create_tool(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST, request.FILES)
        if form.is_valid():
            devtool = form.save()
            return redirect('ideas:devtoollist')
    else:
        form = DevToolForm()
        ctx = {'form': form}
        return render(request, template_name='idealist/tool_form.html', context=ctx)