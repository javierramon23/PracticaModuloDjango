from django.contrib import admin
from posts.models import Category, Post
from django.utils.safestring import mark_safe

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'url', 'summary', 'publish_date')

    list_filter = ('category',)

    def get_image_html(self, post):

        if post.url is not None:
            return mark_safe('<img src="{0}" alt="{1}" height="150">'.format(post.url, post.title))
        else:
            return 'No Image'

    get_image_html.short_description = 'Post Image'

    readonly_fields = ('create_at', 'get_image_html')

    fieldsets = (
        ('Main Info:', {
            'fields': ('owner', 'title', 'summary'),
            'classes': ('collapse',)
        }),
        ('Main Content:', {
            'fields': ('body',),
            'classes': ('collapse',)
        }),
        ('Image:', {
            'fields': ('get_image_html', 'url',),
            'description': 'This field is optional',
            'classes': ('collapse',)
        }),
        ('Categories:', {
            'fields': ('category',),
            'classes': ('collapse',)
        }),
        ('Dates Info:', {
            'fields': ('publish_date', 'create_at'),
            'classes': ('collapse',)
        })
    )
