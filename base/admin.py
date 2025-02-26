from django.contrib import admin
from .models import Blog, Comment, PracticeArea,TeamMember,Job

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(TeamMember)
admin.site.register(Job)

@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Fields to display in the admin list view
    prepopulated_fields = {'slug': ('name',)}