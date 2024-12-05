from django.contrib import admin

# Register your models here.
from .models import Articles
from .models import Post

admin.site.register(Post) 
admin.site.register(Articles) #на стрице администратора будут отображаться данные Articles