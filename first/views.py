from django.shortcuts import render
from .models import first

# Create your views here.
def index(request):
    items_1=first.objects.order_by('id')
    context={"text_values":items_1}
    return render(request, 'first/index.html',context)