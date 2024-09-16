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
git clone <repository-url>
