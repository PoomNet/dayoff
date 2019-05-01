from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from dayoff.models import Profile


class pageAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user','reason','date_start','date_end','approve_status']
    list_filter = ['user_id','date_start', 'date_end','type']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user', 'reason', 'type', 'date_start', 'date_end', ]
        else:
            return ['approve_status', ]


admin.site.register(Profile,pageAdmin)