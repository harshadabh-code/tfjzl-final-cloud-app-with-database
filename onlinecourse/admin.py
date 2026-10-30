from django.contrib import admin
# Seven imported classes from .models
from .models import Course, Instructor, Lesson, Learner, Question, Choice, Submission


# <HINT> Create QuestionInline and ChoiceInline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# <HINT> Create QuestionAdmin and LessonAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']
    search_fields = ['question_text']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# <HINT> Register models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

