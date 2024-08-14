import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='iti',
            user='helana',
            password='1993'
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_record(table, data):
    connection = connect_db()
    if connection is None:
        return "Connection failed"
    
    cursor = connection.cursor()
    if table == 'trainee':
        query = "INSERT INTO trainee (name, age, track_id) VALUES (%s, %s, %s)"
    elif table == 'track':
        query = "INSERT INTO track (name, duration) VALUES (%s, %s)"
    else:
        return "Invalid table"
    
    try:
        cursor.execute(query, data)
        connection.commit()
        return "Record inserted successfully"
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

def update_record(table, data, condition):
    connection = connect_db()
    if connection is None:
        return "Connection failed"
    
    cursor = connection.cursor()
    if table == 'trainee':
        query = "UPDATE trainee SET name = %s, age = %s, track_id = %s WHERE " + condition
    elif table == 'track':
        query = "UPDATE track SET name = %s, duration = %s WHERE " + condition
    else:
        return "Invalid table"
    
    try:
        cursor.execute(query, data)
        connection.commit()
        return "Record updated successfully"
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

def select_records(table, condition=None):
    connection = connect_db()
    if connection is None:
        return "Connection failed"
    
    cursor = connection.cursor(dictionary=True)
    query = f"SELECT * FROM {table}"
    if condition:
        query += " WHERE " + condition
    
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

def delete_record(table, condition):
    connection = connect_db()
    if connection is None:
        return "Connection failed"
    
    cursor = connection.cursor()
    query = f"DELETE FROM {table} WHERE {condition}"
    
    try:
        cursor.execute(query)
        connection.commit()
        return "Record deleted successfully"
    except Error as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

import dbconnection

# Insert 
result = dbconnection.insert_record('trainee', ('John Doe', 25, 1))
print(result)

# Update
result = dbconnection.update_record('trainee', ('John Smith', 26, 1), "name = 'John Doe'")
print(result)

# Select 
records = dbconnection.select_records('trainee')
print(records)

# Delete 
result = dbconnection.delete_record('trainee', "name = 'John Smith'")
print(result)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////(2)//////////////////////////////////////////////////////////////////////

# create class human--->defin classvar,instnacevar,method
class Human:    
    def __init__(self, name, age, gender):
        self.name = name  
        self.age = age    
        self.gender = gender  
    
    def introduce_self(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


# create class employee-->defin classvar,instnacevar,methods

class Employee(Human):
    
    def __init__(self, name, age, gender, employee_id, position, salary):
        super().__init__(name, age, gender)  
        self.employee_id = employee_id  
        self.position = position  
        self.salary = salary  
    
    def work(self):
        print(f"{self.name} is working as a {self.position}.")
    
    def promote(self, new_position, raise_amount):
        self.position = new_position
        self.salary += raise_amount
        print(f"Congratulations {self.name}! You have been promoted to {self.position} with a new salary of {self.salary}.")
    
    def get_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}")

        
#////////////////////////////////////// (3)////////////////////////////////////