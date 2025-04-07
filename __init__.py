from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    for i in range(1, valeur + 1):
        ligne = ' ' * (valeur - i)  # Ajoute les espaces au début
        ligne += ''.join(str(j) for j in range(1, i + 1))  # Partie croissante
        ligne += ''.join(str(j) for j in range(i - 1, 0, -1))  # Partie décroissante
        print(ligne)


if __name__ == "__main__":
  app.run(debug=True)
