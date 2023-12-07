from flask import Blueprint, jsonify, request
from modelos.turnos_modelo import CargarTurnos, TurnosPorIdMedico

turnos_bp= Blueprint('turnos',__name__)

@turnos_bp.route('/getTurnos', methods=['GET'])
def getTurnosJson():
    turnos = CargarTurnos()
    return jsonify(turnos), 200

@turnos_bp.route('/getTurnos/<int:id_medico>', methods=['GET'])
def getTurnosJsonIdMedico(id_medico):
    turnos = TurnosPorIdMedico(id_medico)
    return jsonify(turnos), 200