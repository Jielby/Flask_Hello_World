from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    
    for j in range(1, valeur + 1):
        etoiles += '&nbsp' * (valeur - j)
        for i in range(1, j + 1):
            etoiles += str(i)
        for i in range(j - 1, 0, -1):
            etoiles += str(i)
        
        etoiles += '<br>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
