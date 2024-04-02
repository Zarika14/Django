from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # MYInfo = {
    #     'Name': 'Prashant',
    #     'Age': 23,
    #     'State' : 'Himacha Pradesh'
    # }
    return render(request,'index.html')

def counter(request):
    text = request.POST['text']
    totalWords = len(text.split())
    return render(request,"counter.html",{'number': totalWords })