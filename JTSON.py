import os
import ujson as json
import hashlib
import zlib

class JTSON(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)    # This is the path and filename of the database file
        self.load(self.location) 

    def __repr__(self):
        return "Your JTSON database at {}".format(str(self.location))
    
    def load(self, location):
        """  Loads the database from file into memory if file exists  by calling _load(self) else, ccreates a new one"""
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        """ Loads the database file into memory using Json format"""
        with open(self.location, 'r') as f:
            data = f.read()
            if data:
                compressed_data = bytes.fromhex(data) #Create a bytes object from a string of hexadecimal numbers.
                decompressed_data = zlib.decompress(compressed_data) #The functions in this module allow compression and decompression using the zlib library, which is based on GNU zip.
                self.db = json.loads(decompressed_data.decode())
            else:
                self.db = {}

    def dumpdb(self):
        """ Writes the memory database content into a file """
        data = json.dumps(self.db).encode()
        compressed_data = zlib.compress(data)
        with open(self.location, "w+b") as f:
            f.write(compressed_data.hex().encode())
        return True

    # def set(self, key, value):
    #     """ Adds the key value pair to database """
    #     try:
    #         key_hash = hashlib.sha256(key.encode()).hexdigest()
    #         if not isinstance(value, str):
    #             value = str(value)
    #         self.db[key_hash] = value.encode()
    #         self.dumpdb()
    #         return True
    #     except Exception as e:
    #         print("[X] Error Saving Values to Database : "+str(e))
    #         return False

    def set(self, key, value):
        """ Adds the key value pair to database """
        try:
            key_hash = hashlib.sha256(key.encode()).hexdigest()
            if not isinstance(value, str):
                value = str(value)
            self.db[key_hash] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : "+str(e))
            return False

    def get(self, key):
        """ Gets the value corresponding to the key """
        try:
            key_hash = hashlib.sha256(key.encode()).hexdigest()  #Hashlib secure hashes and message digests. In this we use sha256() to create a SHA-256 hash object.
            return self.db[key_hash]
        except KeyError:
            print("No Value Can Be Found for "+ str(key))
            return False

    def get_all(self):
        """ Returns all key value pairs in database """
        return self.db
    
    def delete(self, key):
        """ removes the key and related value pair from database"""
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        if not key_hash in self.db:
            return False
        else:
            del self.db[key_hash]
            self.dumpdb()
            return True

    def flush(self):
        """ Clears entire database """
        a = input("Do you really want to do that? \n"
                  "Enter Y for yes or any other input for No")
        if not a=="Y" or a == "y":
            self.db = {}
            self.dumpdb()
            return True
        return "Flush Aborted"


