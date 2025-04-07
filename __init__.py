from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def somme(n):
    total = 0

    # Boucle pour parcourir les nombres de 1 à n
    for i in range(1, n + 1):
        # Vérification si divisible par 5 ou 7, mais pas par 11
        if i % 11 != 0:
            continue
        if (i % 5 == 0 or i % 7 == 0):
            if total + i > 5000:
                break
            total += i
            
    
    return f'<pre>La somme finale est : {total}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
