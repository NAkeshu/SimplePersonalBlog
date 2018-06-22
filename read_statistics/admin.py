from django.contrib import admin
from .models import ReadNum

# Register your models here.
@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_type')