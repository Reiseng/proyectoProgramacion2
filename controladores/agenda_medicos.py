# controladores/agenda_medicos.py
from flask import Blueprint, jsonify, request
from modelos.agenda_medicos_modelo import agenda

agenda_bp= Blueprint('agenda',__name__)

@agenda_bp.route('/agenda',methods=['GET'])
def getAgenda():
    return jsonify(agenda)

@agenda_bp.route('/agenda/<int:id_medico>',methods=['GET'])
def getAgenda_por_medico(id_medico):
    id_medico=str(id_medico)
    return jsonify(agenda[id_medico])

