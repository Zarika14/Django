from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Features

# Create your views here.
def index(request):
    # MYInfo = {
    #     'Name': 'Prashant',
    #     'Age': 23,
    #     'State' : 'Himacha Pradesh'
    # }
    return render(request,'index.html')

def counter(request):
    try:
        print("Chal raha hai")
        print(request.body)
        # data = json.loads(request.body)
        data = {}
        # print(request.GET)
        
        # text = request.GET.get('text')
        text = data.get('text',"23")
        print(text)
        # print(data["text"])
        # text = data["text"]
        # print(text)
        print("Mein hu hero")
        # totalWords = len(text.split())
        # print(totalWords)
    
        return JsonResponse({'number':"Prashant" },status = 200)
    except Exception as e:
        return JsonResponse({'Error': str(e) },status = 400)
    
    
def createFeature(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        details = data.get("details")
        
        feature = Features(name = "Summit",details ="Apna master hai")
        feature.save()
        
        return JsonResponse({'Message':"Feature Craeted Successfully" },status = 200)
    except Exception as e:
        return JsonResponse({'Message': "Something went wrong" },status = 400)
       
 
 