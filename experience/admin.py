from django.contrib import admin
from .models import Experience,Comments
## Register your models here.
class InlineExp(admin.StackedInline):
		model=Comments
		extra=1
class CustomExperince(admin.ModelAdmin):
	fieldsets=(
	['message info',{'fields':['message','rate']}],
	['about message',{'fields':['city_id','user_id']}]
	)
	Inlines=[InlineExp]
	list_display=('user_id','city_id','message','rate')
	list_filter=['city_id']
	search_fields =['message']
class Customcomment(admin.ModelAdmin):
	fieldsets=(
	['comment',{'fields':['comment']}],
	['about commnet',{'fields':['experience_id','user_id']}]
	)
	list_display=('experience_id','comment')

admin.site.register(Experience,CustomExperince)
admin.site.register(Comments,Customcomment)
