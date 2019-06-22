from django.shortcuts import render,HttpResponse
import requests
import smtplib
import json
url = "https://www.fast2sms.com/dev/bulk"

# Create your views here.
def index(request):
    return render(request,'send/index.html')

def sms(request):
    return render(request, 'send/sms.html')

def smsm(request):
    if request.method=='POST':
        tel=request.POST.get('tel')
        text=request.POST.get('text')
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {
            "authorization": "PQqMgW25Y0EGh3n4t8adZCSkBmUwTV9yosX6Jx7pcOuIvbLlifZxwNlieXv2bhc7sku0YdJq9ozrf4I5",
            "sender_id": "FSTSMS",
            "message": text, "language": "english", "route": "p",
            "numbers": tel}
        headers = {
            'cache-control': "no-cache"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text['return'])
    return render(request,'send/smsm.html')



def bulksms(request):
    return render(request,'send/bulksms.html')

def bulksmsm(request):
    if request.method=='POST':
        tel = request.POST.get('tel')
        text = request.POST.get('text')
        answer = request.POST['sel']
        for i in range(1,int(answer)+1):
            globals()['par%s' % i]=request.POST.get(str(i))

            querystring = {
                "authorization": "PQqMgW25Y0EGh3n4t8adZCSkBmUwTV9yosX6Jx7pcOuIvbLlifZxwNlieXv2bhc7sku0YdJq9ozrf4I5",
                "sender_id": "FSTSMS",
                "message":text , "language": "english", "route": "p",
                "numbers": globals()["par%s" % i]}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            print(globals()['par%s' % i])
    return render(request,'send/bulksmsm.html')

    return render(request,'send/bulksms.html')

def email(request):
    return render(request,'send/email.html')

def bulkemail(request):
    return render(request,'send/bulkemail.html')

def emailm(request):
    if request.method == 'POST':
        remail = request.POST.get('email')
        msg = request.POST.get('text')
        print(remail,msg)

        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.ehlo()
        connection.starttls()
        connection.login('sagarguptasargam@gmail.com', 'Pass@123')
        connection.sendmail('sagarguptasargam@gmail.com', remail, msg)
        connection.quit()
        print(remail, msg)

    return render(request,'send/emailm.html')

def bulkemailm(request):
    if request.method=='POST':
        text = request.POST.get('text')
        answer = request.POST['sel']
        for i in range(1,int(answer)+1):
            globals()['par%s' % i]=request.POST.get(str(i))

            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.ehlo()
            connection.starttls()
            connection.login('sagarguptasargam@gmail.com', 'Pass@123')
            connection.sendmail('sagarguptasargam@gmail.com',globals()['par%s' % i], text)
            connection.quit()
            print(text)

    return render(request,'send/bulkemailm.html')
