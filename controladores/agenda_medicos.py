# controladores/agenda_medicos.py
from flask import Blueprint, jsonify, request
from modelos.agenda_medicos_modelo import agenda, editar_agenda,agregar_agenda, eliminar_agenda

agenda_bp= Blueprint('agenda',__name__)

@agenda_bp.route('/agenda',methods=['GET'])
def getAgenda():
    return jsonify(agenda)

@agenda_bp.route('/agenda/<int:id_medico>',methods=['GET'])
def getAgenda_por_medico(id_medico):
    id_medico=str(id_medico)
    return jsonify(agenda[id_medico])

@agenda_bp.route('/agregaragenda', methods=['POST'])
def agregaragenda():
    data = request.get_json()
    keys_requeridas = ['id_medico', 'dia_numero', 'hora_inicio', 'hora_fin']
    for llave in keys_requeridas:
        if llave not in data:
            return jsonify({"error": f"La llave '{llave}' es requerida en el JSON recibido."}), 400
    agenda_agregada = agregar_agenda(
       data['id_medico'],
       data['dia_numero'],
       data['hora_inicio'],
       data['hora_fin']
       )
    return jsonify(agenda_agregada),201

#Hay que ver para que se puedan editar varios dias a la ves
# "modificar los horarios de atención de un médico (PUT). (Por ejemplo, puede recibir los días que 
# modifica el horario de atención de la forma 
# [{"dia":1, "hora_inicio" : "10:00", "hora_fin":"17:00"},{"dia":3, "hora_inicio" : "8:00", "hora_fin":"12:00"}]
#  para indicar que se modifican los horarios de atención de lunes y miercoles"
@agenda_bp.route('/editaragenda/<int:id_medico>', methods=['PUT'])
def editagenda(id_medico):
    data = request.get_json()
    keys_requeridas = ['dia_numero', 'hora_inicio', 'hora_fin']
    for llave in keys_requeridas:
        if llave not in data:
            return jsonify({"error": f"La llave '{llave}' es requerida en el JSON recibido."}), 400

    agenda_editada = editar_agenda(
        id_medico,
        data['dia_numero'],
        data['hora_inicio'],
        data['hora_fin']
    )
    return jsonify(agenda_editada)

@agenda_bp.route('/eliminaragenda/<int:id_medico>/<int:dia_numero>', methods=['DELETE'])
def eliminaragenda(id_medico, dia_numero):
    eliminar_agenda(id_medico, dia_numero)
    return jsonify({"mensaje": f"Se ha eliminado la agenda del medico {id_medico} el dia {dia_numero}"}),200