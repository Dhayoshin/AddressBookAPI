# Address Book API

A modern REST API for managing address contacts with geolocation capabilities. Built with FastAPI and SQLAlchemy, providing fast, efficient address management with nearby location search functionality.

## ✨ Features

- **CRUD Operations**: Create, read, update, and delete address entries
- **Geolocation Search**: Find nearby addresses within a specified radius using latitude/longitude
- **Data Validation**: Comprehensive input validation using Pydantic models
- **SQLAlchemy ORM**: Robust database operations with SQLite
- **Auto-Reload Development**: Hot-reload support for faster development
- **Error Handling**: Structured error responses with proper HTTP status codes
- **Logging**: Built-in logging for debugging and monitoring
- **API Documentation**: Auto-generated interactive Swagger documentation

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI web server
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type hints
- **Geopy** - Geolocation library for distance calculations
- **SQLite** - Lightweight embedded database
- **Python 3.8+**

## 📋 Requirements

```
fastapi
uvicorn
sqlalchemy
pydantic
geopy
python-dotenv
```

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Dhayoshin/TechExamforEastAdvantage.git
cd AddressBookAPI
```

### 2. Create a virtual environment

#### Windows
```powershell
python -m venv venv
# If you get a script execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```
DATABASE_URL=sqlite:///./addresses.db
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Endpoints

### Base URL
```
http://localhost:8000/api/v1/addresses
```

### Endpoints

#### 1. Create Address
```
POST /
```
**Request Body:**
```json
{
  "name": "Home",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Home",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

#### 2. Get All Addresses
```
GET /
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Home",
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  {
    "id": 2,
    "name": "Office",
    "latitude": 40.7580,
    "longitude": -73.9855
  }
]
```

#### 3. Update Address
```
PUT /{address_id}
```

**Path Parameter:**
- `address_id` (integer) - The ID of the address to update

**Request Body:**
```json
{
  "name": "New Home",
  "latitude": 40.7580,
  "longitude": -73.9855
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "New Home",
  "latitude": 40.7580,
  "longitude": -73.9855
}
```

#### 4. Delete Address
```
DELETE /{address_id}
```

**Path Parameter:**
- `address_id` (integer) - The ID of the address to delete

**Response (200 OK):**
```json
{
  "message": "Deleted successfully"
}
```

#### 5. Find Nearby Addresses
```
GET /nearby
```

**Query Parameters:**
- `lat` (float, required) - Latitude (-90 to 90)
- `lon` (float, required) - Longitude (-180 to 180)
- `distance_km` (float, required) - Search radius in kilometers (> 0)

**Example:**
```
GET /nearby?lat=40.7128&lon=-74.0060&distance_km=5
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Home",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "distance_km": 0.0
  },
  {
    "id": 2,
    "name": "Office",
    "latitude": 40.7580,
    "longitude": -73.9855,
    "distance_km": 5.15
  }
]
```

## 📖 Validation Rules

### Address Fields

| Field | Rules |
|-------|-------|
| `name` | • Required<br/>• Min length: 1 character<br/>• Max length: 100 characters |
| `latitude` | • Required<br/>• Range: -90 to 90 |
| `longitude` | • Required<br/>• Range: -180 to 180 |

### Nearby Search Parameters

| Parameter | Rules |
|-----------|-------|
| `lat` | • Required<br/>• Range: -90 to 90 |
| `lon` | • Required<br/>• Range: -180 to 180 |
| `distance_km` | • Required<br/>• Must be greater than 0 |

## 🏗️ Project Structure

```
AddressBookAPI/
├── app/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── config.py         # Configuration settings
│   ├── database.py       # Database setup
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   ├── routes.py         # API endpoints
│   └── logger.py         # Logging configuration
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 📝 Usage Examples

### Using cURL

**Create an address:**
```bash
curl -X POST "http://localhost:8000/api/v1/addresses/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Home",
    "latitude": 40.7128,
    "longitude": -74.0060
  }'
```

**Get all addresses:**
```bash
curl -X GET "http://localhost:8000/api/v1/addresses/"
```

**Find nearby addresses:**
```bash
curl -X GET "http://localhost:8000/api/v1/addresses/nearby?lat=40.7128&lon=-74.0060&distance_km=5"
```

**Update an address:**
```bash
curl -X PUT "http://localhost:8000/api/v1/addresses/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Home",
    "latitude": 40.7130,
    "longitude": -74.0062
  }'
```

**Delete an address:**
```bash
curl -X DELETE "http://localhost:8000/api/v1/addresses/1"
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api/v1/addresses"

# Create address
response = requests.post(f"{BASE_URL}/", json={
    "name": "Home",
    "latitude": 40.7128,
    "longitude": -74.0060
})
print(response.json())

# Get all addresses
response = requests.get(f"{BASE_URL}/")
print(response.json())

# Find nearby
response = requests.get(f"{BASE_URL}/nearby", params={
    "lat": 40.7128,
    "lon": -74.0060,
    "distance_km": 5
})
print(response.json())
```

## 📊 Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔍 Database

The API uses SQLite database stored at `addresses.db`. The database is automatically created when the application starts with the following schema:

**addresses table:**
- `id` (Integer, Primary Key)
- `name` (String, Not Null)
- `latitude` (Float, Not Null)
- `longitude` (Float, Not Null)

## 🛡️ Error Handling

The API returns appropriate HTTP status codes:

| Status Code | Description |
|------------|-------------|
| 200 | Success |
| 201 | Created |
| 404 | Address not found |
| 422 | Validation error |
| 500 | Internal server error |

### Error Response Format
```json
{
  "detail": "Error message describing the issue"
}
```

## 📦 Logging

The application includes a logging system that tracks:
- Address creation attempts
- Address updates
- Address deletion
- Search operations
- Error occurrences

Check the logger output in the console for debugging information.

