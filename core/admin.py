from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
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

    # def has_view_permission(self, request, obj=None):
    #     '''
    #     Remove the view button from the admin panel
    #     '''
    #     return False

    # def has_view_or_change_permission(self, request, obj=None):
    #     '''
    #     Remove the view and change button from the admin panel
    #     '''
    #     return False

    def get_ordering(self, request):
        """
        Hook for specifying field ordering.
        """
        return self.ordering or ()  # otherwise we might try to *None, which is bad ;)
