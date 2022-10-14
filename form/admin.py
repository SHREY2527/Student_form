from django.contrib import admin
from .models import user
admin.site.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('id','Student_name','Class','roll_no')
