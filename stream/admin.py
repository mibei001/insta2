from django.contrib import admin
from .models import Post,Profile,Comment
'''
    >>>filter_horizontal property allows ordering of many to many fields<<<
    >>>since we don't have many to many relations in the models. We will not use filter_horizontal<<<
    class HyperAdmin(admin.ModelAdmin):
        filter_horizontal = ('',) 
'''

# Register your models here.
admin.site.register(Post),
admin.site.register(Profile),
admin.site.register(Comment),
