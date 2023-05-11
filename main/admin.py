from django.contrib import admin
from .models import Post, Est, Estimation

# Register your models here.
admin.site.register(Post)
admin.site.register(Est)
admin.site.register(Estimation)