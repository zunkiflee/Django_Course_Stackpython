from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


#admin.site.register(Blog)


class BlogAdmin(SummernoteModelAdmin):
	list_display = ('title', 'author',
					'date_created',
					'date_updated')
	
	summernote_fields = '__all__'



admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Contact)

