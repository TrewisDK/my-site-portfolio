from email import message
from unicodedata import name
from django.shortcuts import render
import telepot
from .models import Projects

API_TOKEN='5671596591:AAEoIh2NHhFfpxstwxczpMqp9E2bXdds8sA'

bot = telepot.Bot(token=API_TOKEN)
 
def index(request):
    return render(request, "index.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        telegram = request.POST.get("mail")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        data = f"От {name}\n\nТелеграм {telegram}\n\n{subject}\n\n{message}"
        bot.sendMessage(596651102, data)
        return render(request, "succes.html")
    else:
        return render(request, "contacts.html")

def projects(request):
    my_projects = Projects.objects.all()
    return render(request, "projects.html", {'projects' : my_projects})

