import requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjMxNzQzLCJpYXQiOjE3NDI2MzE0NDMsImp0aSI6IjY5NjliMGVkZDI4YjQ0MDJiN2NkY2JiNDJlNmNjYTNmIiwidXNlcl9pZCI6Nn0.nJ4Pk5LWnkAEJ8IA7kT3Nc4xVIyNwUHQT36_E64nPPs"  # Add your authentication token here

# GET all books
response = requests.get(f"{BASE_URL}/api/books/")
print(response.json())

# POST create a book
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {"name": " Book", "author": "yashaswini", "price": 99.99}  # Updated fields
response = requests.post(f"{BASE_URL}/books/create/", json=data, headers=headers)
print(response.json())

# PUT update a book (Replace '3' with the correct book ID)
data = {"name": "Updated Book", "author": "manas", "price": 120.50}  # Updated fields
response = requests.put(f"{BASE_URL}/books/update/3/", json=data, headers=headers)
print(response.json())

# DELETE a book (Replace '2' with the correct book ID)
response = requests.delete(f"{BASE_URL}/books/delete/6/", headers=headers)

# Check if response has content before calling .json()
if response.status_code == 204:
    print("Book deleted successfully.")
else:
    print(response.json())  # This works if there's an error message
