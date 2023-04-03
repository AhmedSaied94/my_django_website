from django.contrib import admin

import mywebsite.models as mo

# Register your models here.

admin.site.register(mo.Skill)
admin.site.register(mo.Project)
admin.site.register(mo.Gallery)
admin.site.register(mo.Image)
