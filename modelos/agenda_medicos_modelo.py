# modelos/agenda_medicos_modelo.py
import csv
import datetime
import re

'''
agenda
primera dimension:id medico
segunda dimension:dia_numero
tercera dimension: array con [hora_inicio,hora_fin,fecha_actualizacion]
'''
ruta_archivo_agenda='modelos/agenda_medicos.csv'

def llenarAgenda()->None:
    global agenda
    agenda={}
    with open(ruta_archivo_agenda, newline='') as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
            if agenda.get(row['id_medico']) is not None: #si existe
                agenda[row['id_medico']][row['dia_numero']]=[row['hora_inicio'],row['hora_fin'],row['fecha_actualizacion']]
            else:
                agenda[row['id_medico']]={} #si no existe
                agenda[row['id_medico']][row['dia_numero']]=[row['hora_inicio'],row['hora_fin'],row['fecha_actualizacion']]

def escribir_csv()->None:
    csvlist=convertir_agenda_a_lista()

    with open(ruta_archivo_agenda, 'w', newline='') as csvfile:
        first_row = ['id_medico','dia_numero','hora_inicio','hora_fin','fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=first_row)
        writer.writeheader()
        for string in csvlist:
            csvfile.write(string + '\n')


def convertir_agenda_a_lista():
    csv_list=[]
    for medic_id,dias_dict in agenda.items():
        for dias,lista in dias_dict.items():
            hora_inicio=lista[0]
            hora_fin=lista[1]
            fecha_actualizacion=lista[2]
            line=medic_id+","+dias+","+hora_inicio+","+hora_fin+","+fecha_actualizacion
            csv_list.append(line)
    return csv_list

def agregar_agenda(id, dia_numero, hora_inicio, hora_fin):
    global agenda
    if str(id) not in agenda:
        agenda[str(id)]={}
    agenda[str(id)][dia_numero]=[hora_inicio,hora_fin,getDate()]
    escribir_csv()
    return agenda[str(id)][dia_numero]

def editar_agenda(id, dia_numero, hora_inicio, hora_fin):
    global agenda
    if str(id) not in agenda:
        return {"Respuesta": "ID de médico no encontrado"}
    if dia_numero not in agenda[str(id)]:
        return {"Respuesta": "Día no encontrado para el médico"}

    agenda[str(id)][dia_numero] = [hora_inicio, hora_fin, getDate()]
    escribir_csv()
    return agenda[str(id)][dia_numero]

def eliminar_agenda(id_medico, dia_numero):
    id_medico=str(id_medico)
    dia_numero=str(dia_numero)
    if id_medico in agenda and dia_numero in agenda[id_medico]:
        agenda[id_medico].pop(dia_numero)
        escribir_csv()
        return {"message": "Elemento eliminado correctamente"}, 200
    else:
        return {"message": "No se ha encontrado el elemento a eliminar"}, 404

def es_dia_valido(dia_str:str)->bool:
    # Expresión regular para el formato "d/m/yyyy"
    patron = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$')
    if patron.match(dia_str):
        return True
    else:
        return False

def es_hora_valida(hora_str:str)->bool:
    # Expresión regular para el formato "HH:MM"
    patron = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
    if patron.match(hora_str):
        return True
    else:
        return False

def getDate():
    hoy = datetime.datetime.now()
    fecha = hoy.strftime("%d/%m/%Y")
    return fecha

llenarAgenda()