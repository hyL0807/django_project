from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def page1(request):
    return render(request,'page1.html')

def page2(request):
    if request.method == 'POST':
        text_data = request.POST.get('text_data')
        return HttpResponse(f"입력된 텍스트 : {text_data}")
    else:
        return render(request,'page2.html')
    