from django.contrib import admin

# Register your models here.
from .models import movies,userinput,userinputs
admin.site.register(movies)
admin.site.register(userinput)
admin.site.register(userinputs)

