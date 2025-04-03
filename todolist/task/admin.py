from django.contrib import admin
from . models import Task, Customer
# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display=['id','user', 'title', 'description','completed', 'created_at', 'updated_at']
    
@admin.register(Customer)
class TaskModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name','email', 'mobile', 'city', 'address', 'image']
