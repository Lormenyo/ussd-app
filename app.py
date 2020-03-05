from flask import Flask, request, make_response, render_template
import random
import string


app = Flask(__name__)

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
    '''

    merchantMenu = '''CON Hello Merchant,

    1. Register a farmer
    2. Make Sale
    3. Check Merchant score 
    4. Ask for assistance
    '''

    secondMenu = '''CON Hackathon Company

    4. Other thing to do
    5. Even more thing to do
    6. Last thing to do
    0. BACK
    '''
    # More menu screens ...

    error     = "END Invalid input"

    # Session logic
    if userResponse == 0  or userResponse == '':
        menu = firstMenu
    elif userResponse == '1':
        menu = farmerMenu
    elif userResponse == '2':
        menu = merchantMenu
    #  More logic

    
    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
