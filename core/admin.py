from django.contrib import admin

# Register your models here.

from .views import*

admin.site.register(About)


admin.site.register(Service)


admin.site.register(RecentWork)


admin.site.register(Blog)


admin.site.register(Contact)