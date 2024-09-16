Healthcare Management System (HMS) API
Author: Duc Minh Nguyen
Overview
This is a demo Healthcare Management System (HMS) API built using the FastAPI framework. It is designed to provide a secure and scalable solution for managing healthcare data, including user management, patient records, appointment scheduling, and medical prescriptions. The project follows Clean Architecture to ensure modularity and maintainability.

Features
User Management: Registration, login, and role-based access control (patients, healthcare providers, administrators).
Patient Management: CRUD operations for patient records, medical history, and contact information.
Appointment Scheduling: Schedule, view, update, and cancel appointments with notifications.
Medical Prescriptions: Manage prescriptions with secure access for patients.
Healthcare Provider Management: Manage profiles and availability for healthcare providers.
Administrative Functions: User management and system monitoring for administrators.
Endpoints
/api/v1/create_claims: Generate JWT claims for users.
/api/v1/create_access_token: Create a JWT access token using provided claims.
/api/v1/verify_token: Verify and validate an access token.
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd healthcare-management-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the FastAPI application:

bash
Copy code
uvicorn app.main:app --reload
Requirements
Python 3.8+
FastAPI
Uvicorn
Passlib (for password hashing)
SQLAlchemy (for future database integration)
Project Structure
css
Copy code
.
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
Future Work
Database Integration: Integration with a database (e.g., PostgreSQL, MySQL) to store user and healthcare data securely.
OAuth2 Authentication: Implement OAuth2 for secure user authentication and authorization.
Extended Functionality: Add support for notifications, prescription management, and healthcare provider availability.
