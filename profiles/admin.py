from django.contrib import admin
from .models import ProfileForReceiver
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


class ProfileResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = ProfileForReceiver
        fields = ('id', 'user', 'account_number', 'company_info', 'created', 'update')
        export_order = ('account_number', 'user', 'id', 'company_info', 'created', 'update')

    def dehydrate_user(self, obj):
        return obj.user.username


class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProfileResource


admin.site.register(ProfileForReceiver, ProfileAdmin)