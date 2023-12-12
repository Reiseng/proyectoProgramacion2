import csv
import os
from modelos.randomUser import getRandomUsers

ruta_archivo_medicos="modelos/medicos.csv"

medicos=[]
id_medico = 1

def inicializar_medicos():
    global id_medico
    if os.path.exists(ruta_archivo_medicos):
        importar_datos_desde_csv()

def obtener_medicos():
    return medicos

def obtener_medicos_por_id(id):
    return medicos[id-1]

def crear_medico_manual(dni:int, nombre:str, apellido:str, matricula:int, telefono:str, email:str):
    global id_medico
    medicos.append({
        "id": id_medico,
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "matricula": matricula,
        "telefono": telefono,
        "email": email,
        "habilitado": True,
    })
    id_medico += 1
    exportar_a_csv()
    return medicos[-1]

def crear_medicos_randomuserme(cantidad):
    lista_de_medicos_random= getRandomUsers('medico',cantidad)
    if(not lista_de_medicos_random):
       print("Ha ocurrido un error, por favor intente nuevamente")
       return False
    global id_medico
    global medicos
    for i in range(cantidad):
        medicos.append({
        "id": id_medico,
        "dni": lista_de_medicos_random[i]["dni"],
        "nombre": lista_de_medicos_random[i]['nombre'],
        "apellido": lista_de_medicos_random[i]['apellido'],
        "matricula": lista_de_medicos_random[i]['matricula'],
        "telefono": lista_de_medicos_random[i]['telefono'],
        "email": lista_de_medicos_random[i]['email'],
        "habilitado": True,
        })
        id_medico+=1
    exportar_a_csv()
    return medicos[-cantidad:]

def inhabilitar_medico(id):
    if id<1 or id>len(medicos)+1:
        return {"Respuesta":"Indice Invalido"}
    medicos[id-1]["habilitado"]=False
    exportar_a_csv()
    return medicos[id-1]

def habilitar_medico(id):
    if id<1 or id>len(medicos)+1:
        return {"Respuesta":"Indice Invalido"}
    medicos[id-1]["habilitado"]=True
    exportar_a_csv()
    return medicos[id-1]

def editar_medico(id,dni:str,nombre:str,apellido:str,matricula:str,telefono:str,email:str,habilitado:bool):
    if id<1 or id>len(medicos)+1:
        return {"Respuesta":"Indice Invalido"}
    medicos[id-1]["dni"]=dni
    medicos[id-1]["nombre"]=nombre
    medicos[id-1]["apellido"]=apellido
    medicos[id-1]["matricula"]=matricula
    medicos[id-1]["telefono"]=telefono
    medicos[id-1]["email"]=email
    medicos[id-1]["habilitado"]=habilitado
    exportar_a_csv()
    return medicos[id-1]

def es_medico_habilitado(id)->bool:
    try:
        id=int(id)
        medicos[id-1]
        if medicos[id-1]["habilitado"]=='True':
            return True
        else:
            return False
    except:
        return False

def importar_datos_desde_csv():
    """
    Importa los datos de medicos desde un archivo CSV.
    """
    global medicos
    global id_medico
    medicos = []

    with open(ruta_archivo_medicos, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            medicos.append(row) 
    if len(medicos)>0:
        id_medico= medicos[-1]["id"]+1
    else:
        id_medico = 1

def exportar_a_csv():
    """
    Exporta los datos de los medicos a un archivo CSV.
    """
    with open(ruta_archivo_medicos, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'dni', 'nombre', 'apellido', 'matricula', 'telefono', 'email','habilitado']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for medico in medicos:
            writer.writerow(medico)

inicializar_medicos()