from django.shortcuts import render,redirect
from django.db import connection
from crudappmysql.models import crudmysqldb
from crudappmysql.forms import crudformadd

# Create your views here.
def crudview(request):
    crudDetail = crudmysqldb.objects.all()
    return render(request, 'crudappmysql/sample.html',  {'crudDetail' : crudDetail})

def crudviewjoin(request):
    cursor = connection.cursor()
    cursor.execute("select * from crudappmysql_crudmysqldb as c join crudappmysql_crudtb2 as d on d.id = c.id")
    crudjoin = cursor.fetchall()
    return render(request, 'crudappmysql/sample_join.html', {'crudjoin' : crudjoin})

def crudinsert(request):
    form = crudformadd()
    if request.method == 'POST':
        form = crudformadd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cruddetail')
    return render(request, 'crudappmysql/createform.html', {'form' : form})

def cruddelete(request,id):
   crudDelete = crudmysqldb.objects.get(id=id)
   crudDelete.delete()
   return redirect('/cruddetail')

def crudupdate(request,id):
    crudUpdate = crudmysqldb.objects.get(id=id)
    if request.method == 'POST':
            form = crudformadd(request.POST,instance=crudUpdate)
            if form.is_valid():
                form.save()
                return redirect('/cruddetail')
    return render(request, 'crudappmysql/updateform.html', {'crudUpdate' : crudUpdate})
   
