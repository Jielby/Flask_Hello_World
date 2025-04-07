from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    result = []

    result.append(a)
    if valeur > 1:
        result.append(b)

    for i in range(2, valeur):
        a, b = b, a + b
        result.append(b)

    return ', '.join(str(x) for x in result)
        
if __name__ == "__main__":
    app.run(debug=True)

