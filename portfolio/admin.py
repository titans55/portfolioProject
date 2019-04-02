from django.contrib import admin
from .models import Hit, Experience, PlAndTech, Workflow, Interest, Education, About

# Now register the new UserAdmin...
# admin.site.register(Profile, UserAdmin)

class HitAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Hit, HitAdmin)
admin.site.register(Experience)
admin.site.register(PlAndTech)
admin.site.register(Workflow)
admin.site.register(Interest)
admin.site.register(Education)
admin.site.register(About)