# Query: 
# ContextLines: 1

from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
collection = db["students"]

# ---------------- CREATE ----------------
student1 = {"roll": 1, "name": "Amit", "dept": "CS", "age": 20}
student2 = {"roll": 2, "name": "Riya", "dept": "IT", "age": 21}

collection.insert_one(student1)
collection.insert_one(student2)

print("Records Inserted Successfully")

# ---------------- READ ----------------
print("\nAll Student Records:")
for student in collection.find():
    print(student)

# ---------------- UPDATE ----------------
collection.update_one(
    {"roll": 1},
    {"$set": {"age": 22}}
)

print("\nAfter Update:")
for student in collection.find():
    print(student)

# ---------------- DELETE ----------------
collection.delete_one({"roll": 2})

print("\nAfter Deletion:")
for student in collection.find():
    print(student)
