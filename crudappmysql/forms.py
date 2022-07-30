from django import forms
from crudappmysql.models import crudmysqldb

# Create your models here.
class crudformadd(forms.ModelForm):
    class Meta:
        model = crudmysqldb
        fields = '__all__'
