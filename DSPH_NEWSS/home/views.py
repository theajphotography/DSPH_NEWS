from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(pass1)<5:
            messages.error(request, " Your password must be 7 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.save()
        messages.success(request, " Your DSPH Account has been successfully created plese login with this user name and password")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request): 
    return render(request, "home/about.html")



 ####################       ##################
def htnews(request):
    page = requests.get("https://www.divyabhaskar.co.in/mera-shaher/local/gujarat/vadodara")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []

    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/mera-shaher"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1

    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1

    #data=""
    return render(request, "home/about.html", {'datax': data1} )

def ht1news(request):
    page = requests.get("https://www.divyabhaskar.co.in/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/mera-shaher"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/ht1news.html", {'datax1': data1} )

    ##

def Entertaiment(request):
    page = requests.get("https://www.divyabhaskar.co.in/entertainment/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/entertainment/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/Entertaiment.html", {'datae': data1} )

def Business(request):
    page = requests.get("https://www.divyabhaskar.co.in/business/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/business/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/Business.html", {'datab': data1} )

def IPL(request):
    page = requests.get("https://www.divyabhaskar.co.in/sports/cricket/ipl/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/sports/cricket/ipl/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/IPL-2021.html", {'datai': data1} )



def World(request):
    page = requests.get("https://www.divyabhaskar.co.in/international/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/international/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/World.html", {'dataw': data1} )

def Gujarat(request):
    page = requests.get("https://www.divyabhaskar.co.in/local/gujarat//")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/local/gujarat/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/Gujarat.html", {'datag': data1} )

def Vadodara(request):
    page = requests.get("https://www.divyabhaskar.co.in/mera-shaher/local/gujarat/vadodara/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/mera-shaher/local/gujarat/vadodara/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/Vadodara.html", {'datav': data1} )

def Top(request):
    page = requests.get("https://www.divyabhaskar.co.in/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
   
    return render(request, "home/home.html", {'datat': data1} )

def IPL(request):
    page = requests.get("https://www.divyabhaskar.co.in/sports/cricket/ipl/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/sports/cricket/ipl/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/IPL-2021.html", {'datai': data1} )



def Sports(request):
    page = requests.get("https://www.divyabhaskar.co.in/sports/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/sports/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    
    return render(request, "home/Sports.html", {'datas': data1 } )

def IPL(request):
    page = requests.get("https://www.divyabhaskar.co.in/sports/cricket/ipl/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/sports/cricket/ipl/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/IPL.html", {'datai': data1} )



def Covid(request):
    page = requests.get("https://www.divyabhaskar.co.in/coronavirus/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/coronavirus/"+a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c=0
    for i in range(len(links)):
        if i == 30:
            break
        data1[links[i]]=news[i]
        i+=1
    return render(request, "home/Covid.html", {'datac': data1} )







##############copy of old project
