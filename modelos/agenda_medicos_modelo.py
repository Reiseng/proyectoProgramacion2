import csv
agenda={}
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
llenarAgenda()