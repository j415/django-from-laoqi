from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ('user', 'birth', 'phone','email')
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone',)

admin.site.register(UserProfile,UserProfileAdmin)
>>>>>>> add 2.5
