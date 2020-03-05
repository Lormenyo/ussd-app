from flask import Flask, request, make_response, render_template
import random
import string
import re


app = Flask(__name__)

def confirmMenu(produce,date):
    menu = '''CON Kindly confirm that %s will be ready on %s

    1. Yes
    2. No

    '''%(produce, date)
    return menu


@app.route('/')
def index():
    ussdChannel = "*384*77771#" # Your ussd channel from Africa's Talking
    return render_template('index.html', channel=ussdChannel)

@app.route('/ussd', methods=['POST'])
def ussdSession():

    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text
    print(text)
    print(textArray)
    print(userResponse)
    

    # Screens
    firstMenu = '''CON Hello,

    1. Farmer
    2. Merchant

    '''

    farmerMenu = '''CON Hello Farmer,

    1. Register produce availabilty date
    2. Sell produce immediately
    3. Check farmer score 
    4. Ask for assistance
    0. BACK
    '''

    produceMenu = '''CON Hello Farmer,
    Please Select which produce will be ready

    1. Cabbage
    2. Tomatoes
    3. Pineapple
    0. BACK
    '''

    merchantMenu = '''CON Hello Merchant,

    1. Register a farmer
    2. Make Sale
    3. Check Merchant score 
    4. Ask for assistance
    0. BACK
    '''
    dateMenu = '''CON 
    Please state the exact date(dd-mm-yy) the produce will be ready

    '''
    secondMenu = '''CON Hackathon Company

    4. Other thing to do
    5. Even more thing to do
    6. Last thing to do
    0. BACK
    '''
    # More menu screens ...

    error = "END Invalid input"

    # Session logic
    if userResponse == 0  or userResponse == '':
        menu = firstMenu
       
    elif text == '1':
        menu = farmerMenu
        
    elif text == '2':
        menu = merchantMenu
        
    elif text == '1*1' or text == '1*2' :
        menu = produceMenu
        
    elif text == '1*1*1':
        produce = 'Cabbage'
        menu = dateMenu
        
    elif text == '1*1*2':
        produce = 'Tomatoes'
        menu = dateMenu
      
    elif text == '1*1*3':
        produce = 'Pineapple'
        menu = dateMenu
        
    elif text[:3] == '1*1' and len(text) > 3:
        x=re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$", text)
        if x == None:
            menu = error
        else:
            date = x.group()
            menu = confirmMenu(produce,date)  
       
    #  More logic

    
    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
