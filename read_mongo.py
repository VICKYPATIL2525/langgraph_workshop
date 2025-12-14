from pymongo import MongoClient
from pprint import pprint

# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient("mongodb://localhost:27017")
db = client["langgraph_db"]

students_col = db["students"]
faculty_col = db["faculty"]
attendance_col = db["attendance"]

print("🔄 Connected to MongoDB\n")

# -----------------------------
# Display Students
# -----------------------------
print("📌 STUDENTS COLLECTION")
for doc in students_col.find({}, {"_id": 0}):
    pprint(doc)

# -----------------------------
# Display Faculty
# -----------------------------
print("\n📌 FACULTY COLLECTION")
for doc in faculty_col.find({}, {"_id": 0}):
    pprint(doc)

# -----------------------------
# Display Attendance
# -----------------------------
print("\n📌 ATTENDANCE COLLECTION")
for doc in attendance_col.find({}, {"_id": 0}):
    pprint(doc)

print("\n✅ All MongoDB records displayed successfully")
