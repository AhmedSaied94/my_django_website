from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mywebsite.models import Skill, Project, Gallery, Image

# Register your models here.


class CustomAdmin(ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = []
        self.list_filter = []
        if "name" in self.list_display:
            self.search_fields.append("name")
        if "title" in self.list_display:
            self.search_fields.append("title")
        if "gallery" in self.list_display:
            self.list_filter.append("gallery")
        if "skill" in self.list_display:
            self.list_filter.append("skill")
        ###

        super(CustomAdmin, self).__init__(model, admin_site)


admin.site.register(Skill, CustomAdmin)
admin.site.register(Project, CustomAdmin)
admin.site.register(Gallery, CustomAdmin)
admin.site.register(Image, CustomAdmin)
