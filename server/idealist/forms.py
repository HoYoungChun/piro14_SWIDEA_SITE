from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):

    # 해당 모델 자체의 정보를 담는 네임스페이스 클래스
    # https://stackoverflow.com/questions/57241617/what-is-exactly-meta-in-django
    class Meta:
        model = Idea
        fields = '__all__'
