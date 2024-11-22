import sqlite3

try:
    # Connect to SQLite database
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Check SQLite version
    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Create Employee table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Employee (
        First_Name CHAR(20) NOT NULL,
        Last_Name CHAR(20),
        Age INT,
        Gender CHAR(1),
        Department CHAR(20),
        Income FLOAT
    );
    '''
    cursor.execute(create_table_query)
    print('Employee table created successfully.')

    # Insert data into Employee table
    insert_query = '''
    INSERT INTO Employee (First_Name, Last_Name, Age, Gender, Department, Income)
    VALUES 
        ('John', 'Doe', 28, 'M', 'Engineering', 60000.50),
        ('Jane', 'Smith', 32, 'F', 'Marketing', 75000.00),
        ('Sam', 'Brown', 45, 'M', 'HR', 50000.00),
        ('Lisa', 'Taylor', 30, 'F', 'Finance', 72000.00),
        ('Mike', 'Wilson', 25, 'M', 'IT', 45000.00);
    '''
    cursor.execute(insert_query)
    sqliteConnection.commit()
    print('Data inserted successfully.')

    # Retrieve and display data
    select_query = 'SELECT * FROM Employee;'
    cursor.execute(select_query)
    records = cursor.fetchall()
    print('Employee Records:')
    for row in records:
        print(row)

    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
