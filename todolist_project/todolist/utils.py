from django.db import connection

def ejecutar_consulta_raw(consulta):
    with connection.cursor() as cursor:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
    return resultados
