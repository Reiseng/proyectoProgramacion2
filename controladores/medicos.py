from flask import Blueprint, jsonify, request
from modelos.medicos_modelo import obtener_medicos,obtener_medicos_por_id,crear_medico_manual,crear_medicos_randomuserme,inhabilitar_medico,habilitar_medico,editar_medico

medicos_bp = Blueprint('medicos', __name__)

@medicos_bp.route('/getMedicos',methods=['GET'])
def getMedicosJson():
    return jsonify(obtener_medicos()),200

@medicos_bp.route('/getMedicos/<int:id_medico>',methods=['GET'])
def getMedicoPorID(id_medico):
    return jsonify(obtener_medicos_por_id(id_medico)),200
    
@medicos_bp.route('/agregarMedicoManual',methods=['POST'])
def agregarMedicoManual():
    medico = request.get_json()
    medico_creado=crear_medico_manual(medico["dni"], 
                                      medico["nombre"], 
                                      medico["apellido"],
                                      medico["matricula"],
                                      medico["telefono"],
                                      medico["email"],
                                      )
    return jsonify(medico_creado),201

@medicos_bp.route('/agregarMedicosRandom/<int:cantidad>',methods=['POST'])
def agregarMedicoRandom(cantidad):
    #retorna 201 incluso en error, corregir
    medicos_creados=crear_medicos_randomuserme(cantidad)
    return jsonify(medicos_creados),201

@medicos_bp.route('/inhabilitarMedico/<int:id_medico>',methods=['PUT'])
def desactivarMedico(id_medico):
    medico_inhabilitado=inhabilitar_medico(id_medico)
    if medico_inhabilitado==False:
        return {"Respuesta: El medico solicitado no fue encontrado"},404
    return jsonify(medico_inhabilitado),200

@medicos_bp.route('/habilitarMedico/<int:id_medico>',methods=['PUT'])
def activarMedico(id_medico):
    medico_habilitado=habilitar_medico(id_medico)
    if medico_habilitado==False:
        return {"Respuesta: El medico solicitado no fue encontrado"},404
    return jsonify(medico_habilitado),200

@medicos_bp.route('/editarMedico/<int:id_medico>',methods=['PUT'])
def editMedico(id_medico):
    medico= request.get_json()
    keys_requeridas = ['dni', 
                       'nombre', 
                       'apellido', 
                       'matricula', 
                       'telefono', 
                       'email', 
                       'habilitado']
    for llave in keys_requeridas:
        if llave not in medico:
            return jsonify({"error": f"La llave '{llave}' es requerida en el JSON recibido."}
            ), 400
    
    medico_editado=editar_medico(
        id_medico,medico['dni'],
        medico['nombre'],
        medico['apellido'],
        medico['matricula'],
        medico['telefono'],
        medico['email'],
        medico['habilitado']
        )
    return jsonify(medico_editado),200