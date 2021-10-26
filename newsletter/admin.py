from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirmed', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('email', 'confirmed')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fields = ('email', 'created_at')
    readonly_fields = ('created_at',)
    list_per_page = 100
    list_max_show_all = 200

    def has_delete_permission(self, request, obj=None):
        '''
        Remove the delete button from the admin panel
        '''
        return False

    def has_add_permission(self, request):
        '''
        Remove the add button from the admin panel
        '''
        return False

    def has_edit_permission(self, request, obj=None):
        '''
        Remove the edit button from the admin panel
        '''
        return False

    def has_change_permission(self, request, obj=None):
        '''
        Remove the change button from the admin panel
        '''
        return False
