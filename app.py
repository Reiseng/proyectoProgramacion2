from flask import Flask,blueprints
from controladores.medicos import medicos_bp
app = Flask(__name__)

app.register_blueprint(medicos_bp)

if __name__=="__main__":
    app.run(debug=True)