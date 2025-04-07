from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    suite = [a, b]

    for _ in range(2, n):
    a, b = b, a + b
    suite.append(b)

    return ', '.join(str(nombre) for nombre in suite)



if __name__ == "__main__":
    app.run(debug=True)
