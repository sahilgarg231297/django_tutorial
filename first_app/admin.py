from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
