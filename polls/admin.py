from django.contrib import admin
from .models import Question, Choice, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', "is_open")
    date_hierarchy = 'pub_date'
    # list_filter = ('pub_date',)
    search_fields = ("question_text", )

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', "votes")
    raw_id_fields = ('choice_text',)
    search_fields = ("question_text",)
    raw_id_fields = ("question",)
    ordering = ('-votes',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question',)
    # list_filter = ('pub_date',)
    search_fields = ("question",)



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)