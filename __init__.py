from flask import Flask, abort

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    try:
        liste_nombres = [int(n) for n in valeurs.split('/')]

        # Initialiser le maximum avec le premier élément
        maximum = liste_nombres[0]
        for n in liste_nombres:
            if n > maximum:
                maximum = n

        return f"Le maximum est : {maximum}"

    except (ValueError, IndexError):
        abort(400, description="Assurez-vous de saisir uniquement des entiers dans l'URL.")

@app.route('/')
def accueil():
    return "Utilisez une URL comme /10/25/7 pour trouver le nombre maximum."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
