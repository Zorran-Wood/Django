from django.contrib import admin
from .models import Post#the . in .models is accessed because its in the same directory or project and we can import it via a dotnotation like style

admin.site.register(Post)#adds post option in admin page

# Register your models here.
