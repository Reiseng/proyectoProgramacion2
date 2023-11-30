from flask import Blueprint, jsonify, request
from modelos.pacientes_modelo import obtener_pacientes,obtener_pacientes_por_id,crear_paciente_manual,crear_pacientes_randomuserme,editar_paciente,eliminar_paciente_por_id
pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/getpacientes',methods=['GET'])
def getpacientesJson():
    return jsonify(obtener_pacientes()),200

@pacientes_bp.route('/getpacientes/<int:id_paciente>',methods=['GET'])
def getpacientePorID(id_paciente):
    return jsonify(obtener_pacientes_por_id(id_paciente)),200
    
@pacientes_bp.route('/agregarpacienteManual',methods=['POST'])
def agregarpacienteManual():
    paciente = request.get_json()
    paciente_creado=crear_paciente_manual(paciente["dni"], 
                                      paciente["nombre"], 
                                      paciente["apellido"],
                                      paciente["telefono"],
                                      paciente["email"],
                                      paciente['direccion_calle'],
                                      paciente['direccion_numero']
                                      )
    return jsonify(paciente_creado),201

@pacientes_bp.route('/agregarpacientesRandom/<int:cantidad>',methods=['POST'])
def agregarpacienteRandom(cantidad):
    pacientes_creados=crear_pacientes_randomuserme(cantidad)
    return jsonify(pacientes_creados),201

@pacientes_bp.route('/editarpaciente/<int:id_paciente>',methods=['PUT'])
def editpaciente(id_paciente):
    paciente= request.get_json()
    keys_requeridas = ['dni', 
                       'nombre', 
                       'apellido', 
                       'telefono', 
                       'email', 
                       'direccion_calle',
                       'direccion_numero'
                       ]
    for llave in keys_requeridas:
        if llave not in paciente:
            return jsonify({"error": f"La llave '{llave}' es requerida en el JSON recibido."}
            ), 400
    
    paciente_editado=editar_paciente(
        id_paciente,
        paciente['dni'],
        paciente['nombre'],
        paciente['apellido'],
        paciente['telefono'],
        paciente['email'],
        paciente['direccion_calle'],
        paciente['direccion_numero']
        )
    return jsonify(paciente_editado)

@pacientes_bp.route('/eliminarPaciente/<int:id_paciente>', methods=["DELETE"])
def eliminar_paciente_json(id_paciente):
    ##FALTA VERIFICAR SI TIENE TURNOS##
    ##FALTA VERIFICAR SI TIENE TURNOS##
    eliminar_paciente_por_id(id_paciente)
    return jsonify({"mensaje": "Paciente eliminado correctamente"}), 200