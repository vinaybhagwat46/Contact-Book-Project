from django.contrib import admin
from .models import Contact_Group,Contact

# Register your models here.
class con_grp_admin(admin.ModelAdmin):
    list_display=['type']

admin.site.register(Contact_Group,con_grp_admin)

class contactAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','contact','email','address','category','user']

admin.site.register(Contact,contactAdmin)
