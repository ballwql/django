from django.contrib import admin
from .models import *

admin.site.register(Manager)
admin.site.register(Dba)
admin.site.register(State)
admin.site.register(Database)
admin.site.register(Task)
# Register your models here.
