from django.contrib import admin
from .models import ReadNum, ReadDetail

# Register your models here.
@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_type')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')