# Healthcare Management System (HMS) API

**Author:** Duc Minh Nguyen

## Overview
This is a demo Healthcare Management System (HMS) API built using the FastAPI framework. It is designed to provide a secure and scalable solution for managing healthcare data, including user management, patient records, appointment scheduling, and medical prescriptions. The project follows Clean Architecture to ensure modularity and maintainability.

## Features
- **User Management:** Registration, login, and role-based access control (patients, healthcare providers, administrators).
- **Patient Management:** CRUD operations for patient records, medical history, and contact information.
- **Appointment Scheduling:** Schedule, view, update, and cancel appointments with notifications.
- **Medical Prescriptions:** Manage prescriptions with secure access for patients.
- **Healthcare Provider Management:** Manage profiles and availability for healthcare providers.
- **Administrative Functions:** User management and system monitoring for administrators.

## Endpoints
- `/api/v1/create_claims`: Generate JWT claims for users.
- `/api/v1/create_access_token`: Create a JWT access token using provided claims.
- `/api/v1/verify_token`: Verify and validate an access token.

## Installation
Clone the repository:
```bash
# 1. Clone the repository
git clone <repository-url>
cd healthcare-management-system

# 2. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt
```

## Project Structure .
```bash
├── app
│   ├── api
│   │   └── v1
│   │       ├── token_routes.py
│   ├── core
│   │   └── token_service.py
│   ├── domain
│   │   └── models
│   │       ├── user_claims.py
│   ├── infrastructure
│   │   ├── db
│   │   └── repositories
│   │       └── sql_token_repository.py
│   └── main.py
├── requirements.txt
└── README.md
```
## Sample Claims - Future will be developed based on client's requirement
```bash
{
    "userId": 123,
    "iss": "healthcare_system",
    "sub": "subject_of_token",
    "aud": "healthcare_users",
    "exp": 1726532650.693284,
    "nbf": 1726532589,
    "iat": 1726532589,
    "jti": "unique_jwt_id_123",
    "roles": [
        "admin",
        "user"
    ]
}
```
