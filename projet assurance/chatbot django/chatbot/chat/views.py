import json
from django.http import JsonResponse
from django.shortcuts import render
from .chatboot import get_response,predict_class


def index_get(request):  # put application's code here
    return  render(request,"base.html")

def predict(request):
    if request.method=='POST':
        # text=request.get_json().get("message")
        text=json.load(request)['message']
        ints=predict_class(text)
        intents = json.loads(open('/chatbot/chat/intents.json').read())
        response =get_response(ints,intents)
        message={"answer":response}
        return JsonResponse(message)

