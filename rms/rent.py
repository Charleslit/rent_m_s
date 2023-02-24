from rms import app, db 
from models import User,Post
from flask import math
def rent():
 rooms = input("input the no of rooms occupied:")
 
 
 tenants = input("input the names of tenants:")
 
 
 
 rent  = input(  "enter rent payaple per room :")
 ammount = input( )
 x=rent
 y= ammount
 balance=x-y 
 
 balance = int("rent") - int("ammount")
 
 if (balance > 0):
 
     print("you have a balance of " 
           "kindly pay up to finish your rent ")
 
 elif (balance < 0):
       print("you have paid extra"    " rent for this month ")
 elif (balance == 0):
       print("you have cleared rent for this month  ")

from flask import Flask, render_template, request



@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)
