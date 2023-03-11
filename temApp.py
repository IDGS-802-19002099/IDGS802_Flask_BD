from db import get_connection

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumnos()')
#         resulset=cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as ex:
#     print('ERROR')


#try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consultar_alumno(%s)',(1))
#         resulset=cursor.fetchall()
#         for row in resulset:
#             print(row)
#except Exception as ex:
#     print('ERROR')

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumnos(%s)',(2,))
#         resulset=cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as ex:
#     print('ERROR')




#try:
#    connection=get_connection()
#    with connection.cursor() as cursor:
#        cursor.execute('call agrega_alumnos(%s, %s, %s)',('Arturo','Alba', 'alba@gmail.com')) 
#    connection.commit()
#    connection.close()
#except Exception as ex:
#    print('ERROR')