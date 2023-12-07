import csv
import datetime

ruta_archivo_turnos='modelos/turnos.csv'


def CargarTurnos():
    turnos = []
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

def TurnosPorIdMedico(id_medico):
    try:
        id_medico = int(id_medico)
    except ValueError:
        return

    turnos = CargarTurnos()
    turnosFiltrados = []
    for turno in turnos:
        turno_id_medico = int(turno['id_medico'])
        if turno_id_medico == id_medico:
            turnosFiltrados.append(turno)
    return turnosFiltrados
