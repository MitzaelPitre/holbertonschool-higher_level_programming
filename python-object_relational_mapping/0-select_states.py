#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    # Verificar el número correcto de argumentos
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    try:
        # Conectar a la base de datos
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        
        # Ejecutar la consulta SQL
        c.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Mostrar los resultados
        for state in c.fetchall():
            print(state)
        
        # Cerrar la conexión a la base de datos
        db.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

