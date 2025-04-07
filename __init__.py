from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def somme(n):
    total = 0

    # Boucle pour parcourir les nombres de 1 à n
    for i in range(1, n + 1):
        # Vérification si divisible par 5 ou 7 mais pas par 11
        if (i % 5 == 0 or i % 7 == 0) and i % 11 != 0:
            total += i
        
        # Si la somme dépasse 5000, on arrête la boucle
        if total > 5000:
            break
    
    return f"La somme finale est : {total}"

if __name__ == "__main__":
    app.run(debug=True)
