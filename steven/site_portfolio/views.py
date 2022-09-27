from email import message
from unicodedata import name
from django.shortcuts import render
import telepot

API_TOKEN=''

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
    project_name = "<h1>Bot x_extanger</h1>"
    project_description = "<h3>Бот для криптообмена разработанный на языке Python и асинхронной библиотеке aiogram.</h3>"
    project_image = '<img src="/static/img/bot_ex.jpg" alt="" width="100%" height="30%">'
    data = {"project_name" : project_name, "project_description" : project_description, "project_image" : project_image}
    return render(request, "projects.html", context=data)

