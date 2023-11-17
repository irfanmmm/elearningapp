from django.contrib import admin
from main.models import User, Subject, SubjectViseVideo, Course,UserProfile


admin.site.register(User)

class SubjectViseVideoAdmin(admin.TabularInline):
    list_display = ['subject','video','title',]
    model = SubjectViseVideo




class SubjectAdmin(admin.ModelAdmin):
    # Admin Panalil Display Cheyyenda list
    list_display = ['subject','image']

    # Connect Cheyyunnu
    inlines = [SubjectViseVideoAdmin]

admin.site.register(Subject, SubjectAdmin)



admin.site.register(Course)

admin.site.register(UserProfile)




