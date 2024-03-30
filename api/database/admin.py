from django.contrib import admin


from database.models import Company, Service, Job, User

admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(User)
