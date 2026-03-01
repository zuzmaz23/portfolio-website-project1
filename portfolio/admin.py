from django.contrib import admin
from .models import About, Technology, Project, ContactMessage

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    fields = ['title', 'content']

    def has_add_permission(self, request):
        return not About.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(Technology)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'description']
    list_editable = ['order']
    list_filter = ['name']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']
    fields = ['name', 'icon', 'description', 'order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at', 'github_link', 'live_link']
    list_editable = ['order']
    list_filter = ['created_at', 'technologies']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    ordering = ['order', '-created_at']
    fields = ['title', 'description', 'image', 'github_link', 'live_link', 'technologies', 'order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    list_editable = ['is_read']
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False

admin.site.site_header = "Porfloio - Panel Administracyjny"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Witaj w panelu administracyjnym"
