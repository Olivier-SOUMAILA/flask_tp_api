from flask import Flask, jsonify
app = Flask(__name__)

hostname = {{ ansible_hostname }}
prenom = 'Olivier'

@app.route("/")
def hello():
    return '<h1> Hello there !!</h1>'

@app.route("/timestamp")
def timestamp():
    date = datetime.now()
    return str(date)

@app.route("/host")
def host():
    return "<ul><li>Nom de la machine sur laquelle l'API est exectué --> {}</li><li>Prénom de l'étudiant -->  {}</li></ul>".format(hostname , prenom)


if __name__ == "__main__":
    app.run(host='0.0.0.0') 
