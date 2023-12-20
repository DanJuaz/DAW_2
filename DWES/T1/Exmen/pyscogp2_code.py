import psycopg2
import json

DB_USER = 'julio'
DB_PASSWORD = 'Nazaret23+'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

# Create a connection using psycopg2
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Create a cursor for executing SQL statements
cursor = conn.cursor()

# Raw SQL statements for table creation and data insertion
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255),
        edad INTEGER,
        direccion VARCHAR(255)
    );
'''

insert_data_sql = '''
    INSERT INTO usuarios (nombre, edad, direccion) VALUES
        ('Julio', 23, 'Calle 1'),
        ('Maria', 30, 'Avenida 2'),
        ('Carlos', 25, 'Plaza 3'),
        ('Luisa', 28, 'Calle 4'),
        ('Pedro', 35, 'Avenida 5');
'''

select_data_sql = 'SELECT * FROM usuarios'

try:
    # Create the table
    cursor.execute(create_table_sql)
    conn.commit()

    # Insert data
    #cursor.execute(insert_data_sql)
    conn.commit()

    # Execute the SELECT query
    cursor.execute(select_data_sql)

    # Fetch all rows
    result = cursor.fetchall()

    # Convert result to a list of dictionaries
    rows = []
    for row in result:
        rows.append({
            'ID': row[0],
            'Nombre': row[1],
            'Edad': row[2],
            'Dirección': row[3]
        })

    # Write the result to a JSON file
    with open('usuarios.json', 'w') as json_file:
        json.dump(rows, json_file, indent=2)

    # Print data
    for row in rows:
        print(f"ID: {row['ID']}, Nombre: {row['Nombre']}, Edad: {row['Edad']}, Dirección: {row['Dirección']}")
except Exception as e:
    print(e)
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
