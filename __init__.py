from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
# Demander à l'utilisateur d'entrer un nombre
    n = int(input("Entrez la hauteur de la pyramide : "))

# Boucle pour chaque ligne
    for i in range(1, n + 1):
    # Affiche les espaces
        print(' ' * (n - i), end='')

    # Affiche les nombres qui montent
        for j in range(1, i + 1):
            print(j, end='')

    # Affiche les nombres qui descendent
        for j in range(i - 1, 0, -1):
            print(j, end='')

    # Aller à la ligne suivante
        print()


if __name__ == "__main__":
  app.run(debug=True)
