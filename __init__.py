from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def somme(n):
    total = 0

    for i in range(1, n + 1):
        if (i % 5 == 0 or i % 7 == 0) and i % 11 != 0:
            total += i
        
        if total > 5000:
            total = 5000
            break
    
    return f"La somme finale est : {total}"

if __name__ == "__main__":
    app.run(debug=True)
