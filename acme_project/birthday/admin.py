from django.contrib import admin

from birthday.models import Tag, Birthday


admin.site.register(Birthday)
admin.site.register(Tag)
