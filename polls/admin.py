from django.contrib import admin
from .models import Question, Choice, Vote

admin.site.site_header = 'Control Panel'
admin.site.site_title = 'Polls and Polls'
admin.site.index_title = 'Poll and Voting Management'

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
