#Integrantes: Emiliano Correa, Facundo Reiseng
from flask import Flask
from controladores.medicos import medicos_bp
from controladores.pacientes import pacientes_bp
from controladores.agenda_medicos import agenda_bp
from controladores.turnos import turnos_bp

app = Flask(__name__)

app.register_blueprint(medicos_bp)
app.register_blueprint(pacientes_bp)
app.register_blueprint(agenda_bp)
app.register_blueprint(turnos_bp)

if __name__=="__main__":
    app.run(debug=True)