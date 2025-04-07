from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice():
        n = 5
        lignes = []
    for i in range(1, n + 1):
        ligne = ' ' * (n - i)
        for j in range(1, i + 1):
            ligne += str(j)
        for j in range(i - 1, 0, -1):
            ligne += str(j)
        lignes.append(ligne)

if __name__ == "__main__":
  app.run(debug=True)
