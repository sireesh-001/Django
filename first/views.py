from django.shortcuts import render,redirect
from .models import first
from django.views.decorators.http import require_POST
from .forms import firstform
# Create your views here.
def index(request):
    items_1=first.objects.order_by('id')
    form=firstform
    context={"text_values":items_1,'form':form}
    return render(request, 'first/index.html',context)

@require_POST
def form_view(request):
    form_input=firstform(request.POST)
    if form_input.is_valid():
        first_list=first(text=request.POST['text'])
        first_list.save()
    return redirect('index')

def completed(request,first_id):
    items=first.objects.get(pk=first_id)
    items.completed=True
    items.save()

    return redirect('index')

def deleted(request):
    first.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteall(request):
    first.objects.all().delete()
    return redirect('index')
