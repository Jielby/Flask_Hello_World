from flask import Flask
from flask import render_template
from flask import json
app = Flask(name)


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur):
        for i in range(j+1): 
            etoiles += '*'
        etoiles += '<br>' 
        for i in range(valeur-j):
            etoiles += '$'
    return etoiles

if name == "main":
  app.run(debug=True)
