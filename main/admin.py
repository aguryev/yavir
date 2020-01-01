from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# Register your models here.

#class ChildInline(admin.TabularInline):
#    model = models.User.children.through
#    extra = 1

class UserAdmin(BaseUserAdmin):
    #inlines = (ChildInline,)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'children')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('children', 'groups', 'user_permissions',)


class ChildAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'birthday')}),
        ('Class', {'fields': ('class_id',)}),
        )

    list_display = ('__str__', 'class_id', 'birthday')
    ordering = ('class_id', 'last_name',)
    search_fields = ('last_name',)



admin.site.register(models.User, UserAdmin)
admin.site.register(models.Child, ChildAdmin)
admin.site.register(models.Class)
admin.site.register(models.SiteArticle)
admin.site.register(models.BlogArticle)
admin.site.register(models.ArticleComment)
admin.site.register(models.Event)
admin.site.register(models.EventComment)
admin.site.register(models.Lesson)
admin.site.register(models.KeyPerson)