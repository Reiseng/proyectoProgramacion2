import csv
import os
from modelos.randomUser import getRandomUsers

ruta_archivo_pacientes="modelos/pacientes.csv"

pacientes=[]
id_paciente = 1

def inicializar_pacientes():
    global id_paciente
    if os.path.exists(ruta_archivo_pacientes):
        importar_datos_desde_csv()

def obtener_pacientes():
    return pacientes

def obtener_pacientes_por_id(id):
    global pacientes
    if 1 <= id <= len(pacientes):
        return pacientes[id - 1]
    else:
        return None

def crear_paciente_manual(dni:int, nombre:str, apellido:str, telefono:str, email:str,direccion_calle:str,direccion_numero:str):
    global id_paciente
    pacientes.append({
        "id": id_paciente,
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion_calle": direccion_calle,
        "direccion_numero":direccion_numero
    })
    id_paciente += 1
    exportar_a_csv()
    return pacientes[-1]

def crear_pacientes_randomuserme(cantidad):
    lista_de_pacientes_random= getRandomUsers('paciente',cantidad)
    if(not lista_de_pacientes_random):
       print("Ha ocurrido un error, por favor intente nuevamente")
       return False
    global id_paciente
    global pacientes
    for i in range(cantidad):
        pacientes.append({
        "id": id_paciente,
        "dni": lista_de_pacientes_random[i]["dni"],
        "nombre": lista_de_pacientes_random[i]['nombre'],
        "apellido": lista_de_pacientes_random[i]['apellido'],
        "telefono": lista_de_pacientes_random[i]['telefono'],
        "email": lista_de_pacientes_random[i]['email'],
        'direccion_calle':lista_de_pacientes_random[i]['direccion_calle'],
        'direccion_numero':lista_de_pacientes_random[i]['direccion_numero']
        })
        id_paciente+=1
    exportar_a_csv()
    return pacientes[-cantidad:]

def editar_paciente(id,dni:str,nombre:str,apellido:str,matricula:str,telefono:str,email:str,direccion_calle:str,direccion_numero:str):
    if id<1 or id>len(pacientes)+1:
        return {"Respuesta":"Indice Invalido"}
    pacientes[id-1]["dni"]=dni
    pacientes[id-1]["nombre"]=nombre
    pacientes[id-1]["apellido"]=apellido
    pacientes[id-1]["telefono"]=telefono
    pacientes[id-1]["email"]=email
    pacientes[id-1]["direccion_calle"]=direccion_calle
    pacientes[id-1]["direccion_numero"]=direccion_numero
    exportar_a_csv()
    return pacientes[id-1]

def eliminar_paciente_por_id(id_paciente):
    global pacientes
    paciente_a_eliminar = None
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            paciente_a_eliminar = paciente
            break
    pacientes = [paciente for paciente in pacientes if paciente['id'] != id_paciente]
    exportar_a_csv()
    return paciente_a_eliminar

def es_paciente_en_lista(id) -> bool:
    try:
        id = int(id)
    except:
        return False
    return 0 <= id-1 < len(pacientes)

def importar_datos_desde_csv():
    """
    Importa los datos de pacientes desde un archivo CSV.
    """
    global pacientes
    global id_paciente
    pacientes = []

    with open(ruta_archivo_pacientes, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            pacientes.append(row) 
    if len(pacientes)>0:
        id_paciente= pacientes[-1]["id"]+1
    else:
        id_paciente = 1

def exportar_a_csv():
    """
    Exporta los datos de los pacientes a un archivo CSV.
    """
    with open(ruta_archivo_pacientes, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'dni', 'nombre', 'apellido', 'telefono', 'email','direccion_calle','direccion_numero']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for paciente in pacientes:
            writer.writerow(paciente)
inicializar_pacientes()