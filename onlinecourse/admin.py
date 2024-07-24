from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner,Question,Choice, Enrollment,Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5




# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['content','grade']

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name','course']

class LearnerAdmin(admin.ModelAdmin):
    list_display = ['name','course']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

class Enrollment(admin.ModelAdmin):
    list_display = ['name','course']

class Submission(admin.ModelAdmin):
    list_display = ['submitted','Not_submitted']





# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question)
admin.site.register(Choice)
