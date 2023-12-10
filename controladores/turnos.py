from flask import Blueprint, jsonify, request
from modelos.turnos_modelo import get_turnos_pendientes_por_id,turnos,se_puede_agregar_turno

turnos_bp= Blueprint('turnos',__name__)

@turnos_bp.route('/getTurnos', methods=['GET'])
def getTurnosJson():
    return jsonify(turnos), 200

@turnos_bp.route('/getTurnosPendientes/<int:id_medico>', methods=['GET'])
def getTurnosPendientesPorIdMedico(id_medico):
    return jsonify(get_turnos_pendientes_por_id(id_medico)), 200

@turnos_bp.route('/agregarTurno/',methods=['POST'])
def addTurno():
    turno= request.get_json()
    keys_requeridas=[
        'id_medico',
        'id_paciente',
        'hora_turno',
        'fecha_solicitud']
    for llave in keys_requeridas:
        if llave not in turno:
            return jsonify({"error": f"La llave '{llave}' es requerida en el JSON recibido."}
            ), 400
    if se_puede_agregar_turno(turno['id_medico'],turno['id_paciente'],turno['hora_turno'],turno['fecha_solicitud']):
        return {"response":"todo piola"}
    else:
        return {"response":"F"}
    
