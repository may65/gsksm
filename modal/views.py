from django.shortcuts import render
def modal(request):
    # gsk='gsk text'
    # menu = menuitem()
    # return HttpResponse('hello world')
    return render(request,'modal.html')#, {'menu':menu,'gsk':gsk})#,{'td':td,'th':th})
    # return HttpResponse('mbr')
