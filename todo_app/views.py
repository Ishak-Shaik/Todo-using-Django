from django.shortcuts import render,redirect

from .models import TODO

def Todohtml(request):
    try:
        title=request.POST['title']
        data=TODO(Title=title,status='Pending')
        data.save()
    except:
        pass
    todoList=TODO.objects.all()
    return render(request,'index.html',{'todoList':todoList})


def deletetask(request,attr):
    task=TODO.objects.get(id=attr)
    task.delete()
    return redirect('/')


def updatetask(request,attr):
    task=TODO.objects.get(id=attr)
    if task.status=='Pending':
        TODO.objects.filter(id=attr).update(status='Finished')
    else:   
        TODO.objects.filter(id=attr).update(status='Pending')
    return redirect('/')

