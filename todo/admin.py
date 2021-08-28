from django.contrib import admin

from todo.models import TodoText


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'text')


admin.site.register(TodoText, ToDoAdmin)
