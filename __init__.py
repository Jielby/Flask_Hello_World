from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    result = []

    result.append(a)
    if n > 1:
        result.append(b)

    # Calcul des autres termes
    for i in range(2, n):
        a, b = b, a + b
        result.append(b)

    # Affichage de la suite sous forme de texte
    return ', '.join(str(x) for x in result)
        
if __name__ == "__main__":
    app.run(debug=True)

