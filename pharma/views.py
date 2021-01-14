from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from django.shortcuts import render 
from django.contrib import messages 
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
import cv2
import numpy as np 
from django.contrib.auth  import authenticate,  login, logout
from selenium import webdriver
import os
#it is the header decleration for the programme
import webbrowser
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#import pytesseract extracting text from images and saving it into databse form.
#I am coder boy writing an application for crud data 
#def goto(request):

def music(request):
    if(request.method=="POST"):
        string=request.POST['music']
        return render(request,'pharma/register.html')
        #string=request.POST['music']
        #driver=webdriver.Chrome("C:\\Users\\Hemant\\Downloads\\chromedriver_win32\\chromedriver.exe")       driver.get("https://www.youtube.com/")
        #ele=driver.find_element_by_name("search_query")
        #print(ele.is_displayed())
# automate testing in future
        #ele.send_keys(string)
        #act=ActionChains(driver)
        #driver.maximize_window()
#act.send_keys(Keys.TAB).per    form()  
        #act.send_keys(Keys.ENTER).perform()
        #act.send_keys(Keys.ARROW_RIGHT).perform()
        #act.send_keys(Keys.ENTER).perform()
        #act.send_keys(Key.TAB).perform()
    return render(request,'pharma/register.html')

         
def home(request):
    return render(request, 'pharma/index.html')

def opencam(request):
     return render(request,'pharma/register.html')

def registerpage(request):
    form=UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request,'pharam/register.html')
def dealerform(request):
    dict = {'add': True, }
    return render(request, 'pharma/dealer.html', dict)

def dealerforminsert(request):
    try:
        dealer = Dealer()
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def dealerformupdate(request, foo):
    try:
        dealer = Dealer.objects.get(pk=foo)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        # check for errorneous input
        if (len(username)<10):
            #it is 
            messages.error(request, " Your user name must be under 10 characters")
            return render(request,'pharma/register.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request,'pharma/register.html')
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return render(request,'pharma/register.html')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        #messages.success(request, " Your coder has been successfully created")
        return render(request, 'pharma/index.html')

def dealerformview(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dict = {'dealer': dealer}
    return render(request, 'pharma/dealer.html', dict)
    
def dealerformdelete(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dealer.delete()
    return render(request, 'pharma/index.html')


def dealertable(request):
    dealer = Dealer.objects.all()
    dict = {"dealer": dealer}
    return render(request, 'pharma/dealertable.html', dict)


def empform(request):
    dict = {'add': True}
    return render(request, 'pharma/emp.html', dict)


def empforminsert(request):
    try:
        emp = Employee()
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')

#Empformda
def empformupdate(request, foo):
    try:
        emp = Employee.objects.get(pk=foo)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def empformview(request, foo):
    emp = Employee.objects.get(pk=foo)
    li=[]
    dict = {'emp': emp}
    return render(request, 'pharma/emp.html', dict)


def empformdelete(request, foo):
    emp = Employee.objects.get(pk=foo)
    emp.delete()
    return render(request, 'pharma/index.html')


def emptable(request):
    emp = Employee.objects.all()
    dict = {"emp": emp}
    return render(request, 'pharma/emptable.html', dict)


def custform(request):
    dict = {'add': True}
    return render(request, 'pharma/cust.html', dict)
    
def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')

def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    dict = {'cust': cust}
    return render(request, 'pharma/cust.html', dict)


def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return render(request, 'pharma/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'pharma/custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'pharma/med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dict = {'med': med}
    return render(request, 'pharma/med.html', dict)


def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return render(request, 'pharma/index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'pharma/medtable.html', dict)


def purchaseform(request):
    dict = {'add': True}
    return render(request, 'pharma/purchase.html', dict)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformupdate(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    dict = {'purchase': purchase}
    return render(request, 'pharma/purchase.html', dict)


def purchaseformdelete(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    purchase.delete()
    return render(request, 'pharma/index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    dict = {"purchase": purchase}
    return render(request, 'pharma/purchasetable.html', dict)

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            print('yes')
            messages.success(request, "Successfully Logged In")
            return render(request,'pharma/index.html')
        else:
            print('no')
            messages.error(request, "Invalid credentials! Please try again")
            return render(request,'pharma/register.html')

    return HttpResponse("404- Not found")