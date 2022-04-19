from django.contrib import admin
from .models import ArchitectureAccount, ClientAccount, Project , User
# Register your models here.
admin.site.register(ClientAccount)
admin.site.register(User)
admin.site.register(ArchitectureAccount)
admin.site.register(Project)