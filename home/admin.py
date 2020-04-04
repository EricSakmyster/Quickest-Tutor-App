from django.contrib import admin
from . import models

# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name",)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("year",)
class TutorAdmin(admin.ModelAdmin):
    list_display = ("year",)

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Tutor, TutorAdmin)
