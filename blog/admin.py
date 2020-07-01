from django.contrib import admin
from .models import Post,Education,Skill,Work

# Register your models here.
admin.site.register(Post)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Work)