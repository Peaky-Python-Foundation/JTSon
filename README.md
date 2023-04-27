# JTSon - A simple json database.

## Introduction:
JTSON is a lightweight database that stores key-value pairs in a file. It uses JSON format to store data in the file and provides basic operations like adding, getting, deleting, and flushing data. JTSON uses hash functions to secure keys and zlib compression to reduce file size.

## Class and methods:

### Class JTSON:
Initializes a new instance of JTSON database with the specified location parameter. It expands the user path and checks if a file exists at the location. If yes, it loads data from the file into memory; otherwise, it creates a new database.

### Method load:
The method loads data from the database file into memory if the file exists. It calls the _load method to read and decompress data from the file.

### Method _load:
The method reads data from the file in hexadecimal format, decompresses it using the zlib module, and loads the data into the database. If no data is found, it initializes an empty dictionary.

### Method dumpdb:
The method writes the database's content in JSON format into the database file. It compresses the JSON data using zlib and writes it in hexadecimal format.

### Method set:
The method adds a new key-value pair to the database. It hashes the key using the SHA-256 hash function, encodes the value as a string, and saves the pair to the database. It calls the dumpdb method to write the data to the file.

### Method get:
The method returns the value associated with the specified key. It hashes the key using SHA-256 and retrieves the value from the database. If the key is not found, it returns False.

### Method get_all:
The method returns all the key-value pairs in the database.

### Method delete:
The method removes the key and its associated value from the database. It hashes the key and checks if it exists in the database. If found, it deletes the pair and calls the dumpdb method to write the updated data to the file.

### Method flush:
The method clears the entire database. It prompts the user for confirmation before executing the operation. If confirmed, it deletes all the key-value pairs and writes the updated data to the file using the dumpdb method.


## Example:
```py
# Create a new instance of JTSON database
db = JTSON("my_database.jtson")

# Add a key-value pair to the database
db.set("name", "John Doe")

# Retrieve a value from the database using the key
value = db.get("name")
print(value) # Output: John Doe

# Retrieve all the key-value pairs in the database
data = db.get_all()
print(data) # Output: {'7f1ebd7447902f18e48f8c3e68a15a0c107d77f1bc8c0a16998da19d68daa903': b'John Doe'}

# Delete a key-value pair from the database
db.delete("name")

# Clear the entire database
db.flush()
```
