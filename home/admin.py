from django.contrib import admin
from . import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "year","phone", "tsubjects", "major", "texp", "hourlyRate")


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class AvailableAdmin(admin.ModelAdmin):
    list_display = ("available",)
admin.site.register(models.Available, AvailableAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
