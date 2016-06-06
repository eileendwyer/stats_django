from django.contrib import admin

# Register your models here.
import nwsl_app.models

#from nwsl_app.models import GoalieStats
admin.site.register(nwsl_app.models.GoalieStats)
