from django import forms
from django.forms.widgets import DateInput

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
   class Meta:
       model = Question
       fields = '__all__'
       widgets = {
           'pub_date': DateInput(attrs={'type': 'date'}),
       }
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        # fields = "__all__"
        fields = ("question", "choice_text", "votes",)
