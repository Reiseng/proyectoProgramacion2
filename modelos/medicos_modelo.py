import csv
import os
from randomUser import getRandomUsers
ruta_archivo_medicos="modelos/medicos.csv"

medicos=[]
id_medico = 1

def inicializar_medicos():
    global id_medico
    if os.path.exists(ruta_archivo_medicos):
        importar_datos_desde_csv()

def obtener_medicos():
    return medicos

def obtener_medicos_por_id(id_medico):
    return medicos[id_medico]

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

def importar_datos_desde_csv():
    """
    Importa los datos de medicos desde un archivo CSV.
    """
    global medicos
    global id_medico
    medicos = []  # Limpiamos la lista de medicos antes de importar desde el archivo CSV

    with open(ruta_archivo_medicos, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
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