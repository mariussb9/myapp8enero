from flask import Flask
import os

app = Flask(__name__)

PORT=os.environ.get("PORT", 5000)
#PORT=os.environ["PORT"]

@app.route('/hello')
def hello_world():
    NOMBRE=os.environ.get("NOMBRE", "Sin nombre")
    return f"Hola Mundo, soy Ronladinho, el balon de oro de 2006!, y mi variable NOMBRE={NOMBRE}"

@app.route('/bye')
def bye_world():
    return ("Neymar Jr. tambien es balon de oro, adios :D")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
