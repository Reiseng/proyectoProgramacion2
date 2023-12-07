# modelos/agenda_medicos_modelo.py
import csv
import datetime

'''
agenda
primera dimension:id medico
segunda dimension:dia_numero
tercera dimension: array con [hora_inicio,hora_fin,fecha_actualizacion]
'''
ruta_archivo_agenda='modelos/agenda_medicos.csv'
hoy = datetime.datetime.now()
fecha = hoy.strftime("%d/%m/%Y")


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

def agregar_agenda(id, dia_numero, hora_inici, hora_fin):
    global agenda
    if str(id) not in agenda:
        agenda[str(id)]={}
    agenda[str(id)][dia_numero]=[hora_inici,hora_fin,fecha]
    escribir_csv()
    return agenda[str(id)][dia_numero]

def editar_agenda(id, dia_numero, hora_inicio, hora_fin):
    global agenda
    if str(id) not in agenda:
        return {"Respuesta": "ID de médico no encontrado"}
    if dia_numero not in agenda[str(id)]:
        return {"Respuesta": "Día no encontrado para el médico"}

    agenda[str(id)][dia_numero] = [hora_inicio, hora_fin, fecha]
    escribir_csv()
    return agenda[str(id)][dia_numero]

def eliminar_agenda(id_medico, dia_numero):
    # Lee el contenido actual del archivo CSV
    with open(ruta_archivo_agenda, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        filas = list(reader)

    # Encuentra y elimina la línea con los parametros especificados
    nuevas_filas = [fila for fila in filas if not (int(fila['id_medico']) == id_medico and int(fila['dia_numero']) == dia_numero)]

    # Escribe el contenido actualizado al archivo CSV
    with open(ruta_archivo_agenda, 'w', newline='') as csvfile:
        first_row = ['id_medico', 'dia_numero', 'hora_inicio', 'hora_fin', 'fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=first_row)
        writer.writeheader()
        for fila in nuevas_filas:
            writer.writerow(fila)

llenarAgenda()
escribir_csv()