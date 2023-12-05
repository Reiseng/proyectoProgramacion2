# controladores/agenda_medicos.py
from flask import Blueprint, jsonify, request
from modelos.agenda_medicos_modelo import agenda

agenda_bp= Blueprint('agenda',__name__)