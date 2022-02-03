from django.http import HttpResponse
from django.shortcuts import render,redirect
import mysql.connector as mysql
def login(req):
    return render(req,"login.html")
def registration(req):
    return render(req,"registration.html")
def register(req):

    name = req.GET.get("name")
    email = req.GET.get("email")
    password = req.GET.get("pass")
    cpassword = req.GET.get("cpass")

    con = mysql.connect(host="localhost", user="root",
                        password="root", database="marriage")
    q = "insert into register values ('{0}','{1}','{2}','{3}')".format(
        name, email, password, cpassword)

    cr = con.cursor()
    cr.execute(q)
    con.commit()

    return redirect("/login")
def fetch_login(req):
    # global email1
    # global pass1
    email1 = req.GET.get("email")
    pass1 = req.GET.get("pass")
    
    global rec

    con = mysql.connect(host="localhost", user="root",
                        password="root", database="marriage")
    q1 = "select * from register where email='{0}' and password='{1}'".format(email1, pass1)
    cr = con.cursor()
    cr.execute(q1)
    rec = cr.fetchone()
    # em = rec.get("email")
    # pw = rec.get("password")
    
    if rec is None:
        return redirect("/login")
    else:
        return render(req,"home.html",{"name": rec})
    

def logout(req):
    return redirect("/login")
# def profile(req):

#     con = mysql.connect(host="localhost", user="root",
#                         password="root", database="marriage")
#     q1 = "select * from register where email='{0}' and password=''{1}".format(email1,pass1)
#     cr = con.cursor()
#     cr.execute(q1)
#     rec = cr.fetchone()
#     if rec is None:
#         return HttpResponse("hello............")
#     else:
#         return render(req,"profile.html",{"name":rec,"gmail":rec,"password":rec,"cpass":rec})
# def edit(req):
#     return render(req,"edit.html")




# def update(req):
#     nn = req.GET.get("nname")
#     ne = req.GET.get("nemail")
#     np = req.GET.get("npass")
#     ncp = req.GET.get("ncpass")

#     con = mysql.connect(host="localhost", user="root",
#                         password="root", database="marriage")
#     q2 = ""
#     nn = rec.get("name")
#     ne = rec.get("email")
def contact(req):
    return render(req,"contact.html")
    # return HttpResponse("<h1>Hello everyone</h1>")