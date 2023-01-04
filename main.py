import pymysql
from my_sql_1 import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 80,
        user = user,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" *20)
    try:
        # create table
        with connection.cursor() as cursor:
            create_table_querty = "CREATE TABLE 'users' (id int AUTO_INCREMENT,"\
                                  "name varchar(32),"\
                                  "password varchar(32),"\
                                  "email varchar(32),"\
                                  "PRIMARY KEY (id));"
            cursor.execute(create_table_querty)
            print("Table created successfilly")
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              database='db',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         create_table_querty = "CREATE TABLE 'users' (id int AUTO_INCREMENT,"\
#                               "name varchar(32),"\
#                               "password varchar(32),"\
#                               "email varchar(32),"\
#                               "PRIMARY KEY (id));"
#         cursor.execute(create_table_querty)
#         # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         create_table_querty
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)