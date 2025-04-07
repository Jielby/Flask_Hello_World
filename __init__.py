from flask import Flask
from flask import render_template
from flask import json 
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    resultat = ""
    for i in range(1, valeur + 1):
        # Espaces
        ligne = " " * (valeur - i)
        # Nombres qui montent
        for j in range(1, i + 1):
            ligne += str(j)
        # Nombres qui descendent
        for j in range(i - 1, 0, -1):
            ligne += str(j)
        # Ajouter la ligne à la pyramide + saut de ligne HTML
        resultat += ligne + "<br>"
    return resultat

if __name__ == "__main__":
    app.run(debug=True)
