from django.contrib import admin
from crudappmysql.models import crudmysqldb
# Register your models here.

class crudadmin(admin.ModelAdmin):
    crud_details = ['sno','sname','semail']

admin.site.register(crudmysqldb,crudadmin)
