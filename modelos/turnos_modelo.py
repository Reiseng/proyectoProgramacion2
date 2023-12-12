import csv,os
from datetime import datetime,timedelta
from modelos.medicos_modelo import es_medico_habilitado
from modelos.pacientes_modelo import es_paciente_en_lista
from modelos.agenda_medicos_modelo import dentro_de_horario_de_atencion

ruta_archivo_turnos='modelos/turnos.csv'

turnos = []

def CargarTurnos():
    global turnos
    with open(ruta_archivo_turnos, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_medico = row.get('id_medico')
            id_paciente = row.get('id_paciente')
            hora_turno = row.get('hora_turno')
            fecha_solicitud = row.get('fecha_solicitud')

            turno = {
                'id_medico': id_medico,
                'id_paciente': id_paciente,
                'hora_turno': hora_turno,
                'fecha_solicitud': fecha_solicitud
            }
            turnos.append(turno)
    return turnos

def get_turnos_pendientes_por_id(id_medico):
    try:
        id_medico = int(id_medico)

    except ValueError:
        return ValueError
    turnosFiltrados = []
    for turno in turnos:
        turno_id_medico = int(turno['id_medico'])
        if turno_id_medico == id_medico and es_fecha_futura(turno['fecha_solicitud']):
            turnosFiltrados.append(turno)
    return turnosFiltrados

def se_puede_agregar_turno(id_medico,id_paciente,hora_turno,fecha_solicitud)->bool:
    if es_medico_habilitado(id_medico) and es_paciente_en_lista(id_paciente) and es_fecha_mes_siguiente(fecha_solicitud) and not hay_turno_ocupado(id_medico,hora_turno,fecha_solicitud) and dentro_de_horario_de_atencion(id_medico,hora_turno,fecha_solicitud):
        return True
    else:
        #no se cumplen las condiciones para agregar el turno
        return False
    
def agregar_turno(id_medico, id_paciente, hora_turno, fecha_solicitud):
    global turnos
    nuevo_turno = {
        'id_medico': id_medico,
        'id_paciente': id_paciente,
        'hora_turno': hora_turno,
        'fecha_solicitud': fecha_solicitud
    }
    turnos.append(nuevo_turno)

    # Verificar si el archivo existe
    archivo_existente = os.path.isfile(ruta_archivo_turnos)

    with open(ruta_archivo_turnos, 'a', newline='') as csvfile:
        fieldnames = ['id_medico', 'id_paciente', 'hora_turno', 'fecha_solicitud']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir el encabezado solo si el archivo está vacío
        if not archivo_existente:
            writer.writeheader()
        else:
            # Agregar salto de línea después del encabezado
            csvfile.write('\n')

        writer.writerow(nuevo_turno)

    return nuevo_turno

def eliminar_turno(id_paciente):
    global turnos
    turnos_eliminados = [turno for turno in turnos if turno['id_paciente'] == str(id_paciente)]
    turnos = [turno for turno in turnos if turno['id_paciente'] != str(id_paciente)]

    with open(ruta_archivo_turnos, 'w', newline='') as csvfile:
        fieldnames = ['id_medico', 'id_paciente', 'hora_turno', 'fecha_solicitud']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(turnos)
    return {"turnos_eliminados": turnos_eliminados}

        
def hay_turno_ocupado(id_medico,hora_turno,fecha_solicitud)->bool:
    for turno in turnos:
        if turno['id_medico']==id_medico and turno['hora_turno']==hora_turno and turno['fecha_solicitud']==fecha_solicitud:
            return True
        else:
            continue
    return False

def es_fecha_mes_siguiente(fecha_string)->bool:
    fecha_ingresada= datetime.strptime(fecha_string, '%d/%m/%Y').date()
    fecha_actual = datetime.now().date()
    fecha_30dias= fecha_actual + timedelta(days=30)
    return fecha_ingresada>=fecha_actual and fecha_ingresada<=fecha_30dias

def es_fecha_futura(fecha_string)->bool:
    fecha_actual = datetime.now().date()
    fecha_ingresada = datetime.strptime(fecha_string, '%d/%m/%Y').date()
    return fecha_ingresada >= fecha_actual

CargarTurnos()