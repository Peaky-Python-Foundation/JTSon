from JTSON import JTSON
import json

def JTSONtest():
    db = JTSON('db.json')
    
    # Store some user information
    db.set("user1", {"name": "Alice", "age": 25, "email": "alice@example.com"})
    db.set("user2", {"name": "Bob", "age": 30, "email": "bob@example.com"})
    db.set("user3", {"name": "Charlie", "age": 35, "email": "charlie@example.com"})
    
    # Retrieve user information
    print("User 1:", db.get("user1"))
    print("User 2:", db.get("user2"))
    print("User 3:", db.get("user3"))
    
    # Store some product information
    db.set("product1", {"name": "Product 1", "price": 10.0, "description": "This is product 1"})
    db.set("product2", {"name": "Product 2", "price": 20.0, "description": "This is product 2"})
    db.set("product3", {"name": "Product 3", "price": 30.0, "description": "This is product 3"})
    
    # Retrieve product information
    print("Product 1:", db.get("product1"))
    print("Product 2:", db.get("product2"))
    print("Product 3:", db.get("product3"))
    
    # Retrieve all key-value pairs in database
    print("All key-value pairs:", db.get_all())

     
    # Create a dictionary with the results of the test cases
    results = {
        "user1": db.get("user1"),
        "user2": db.get("user2"),
        "user3": db.get("user3"),
        "product1": db.get("product1"),
        "product2": db.get("product2"),
        "product3": db.get("product3"),
        
    }
    
    # Save the results to a JSON file
    with open("test_results.json", "w") as f:
        json.dump(results, f)

JTSONtest()
