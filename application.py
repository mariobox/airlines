import json
from flask import Flask, redirect, render_template, request

# Configure app
app = Flask(__name__)

f = open('airlines.json')
data = json.load(f)  # turn json array of objects into an python list of objects
f.close()

# create an empty list to store (airline symbol, airline name) tuples
symbol_airline = []

# create each (airline symbol, airline name) tuple and append it to symbol_airline:
  # first, itereate over each object on the list and extract the object's values
  # second, use the tuple() function to create the tuples
  # third, append the tupple to our symbol_airline list
for airline in data:
  symbol_airline.append((tuple(airline.values())))

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/iata", methods=["POST"])
def iata():
    results = []
    user_input = request.form.get("airline")
    user_input_lower = user_input.lower()
    for airline in symbol_airline:
      airline_lower = airline[1].lower()
      if user_input_lower in airline_lower:
        results.append(f'{airline[1]} ({airline[0]})')
    return render_template("index.html", results=results)
