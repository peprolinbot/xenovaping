from flask import Flask, request, render_template

from config import *

import database

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("main.html")

@app.route('/add_card')
def add_card_page():
    return render_template("add_card.html")

@app.route('/delete_card')
def delete_card_page():
    return render_template("delete_card.html")

@app.route('/api/add_card', methods=['POST'])
def add_card():
    number = request.json["number"]
    try:
        number = int(number)
    except ValueError:
        return {"error": "Use a valid card number"}
    email = request.json["email"]
    card = database.get_card(session, number)
    if card != None:
        return {"error": "Card already exists"}
    account.add_card(number, str(number))
    database.add_card(session, number, email)
    return "OK"

@app.route('/api/delete_card', methods=['POST'])
def delete_card():
    number = request.json["number"]
    try:
        number = int(number)
    except ValueError:
        return {"error": "Use a valid card number"}
    deleted = database.delete_card(session, number)
    if deleted == False: # Card doesn't exist in database
        return {"error": "Card already deleted"}
    account.delete_card(number)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
