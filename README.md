# Hospital Management System

A comprehensive Django REST Framework-based hospital management system with features for patient management, appointments, medical records, billing, pharmacy, inventory, and more.

## Features

- **Patient Management**: Manage patient profiles, medical history, and contact information
- **Doctor Management**: Manage doctor profiles, specializations, and consultation fees
- **Appointments**: Schedule and manage patient appointments
- **Medical Records**: Store and access patient medical records
- **Billing**: Invoice generation and payment tracking
- **Pharmacy**: Manage medicines and prescriptions
- **Lab Tests**: Order and track lab tests
- **Inventory**: Track hospital inventory and equipment
- **Staff Scheduling**: Manage staff shifts and schedules
- **Ward Management**: Manage hospital wards and beds
- **Notifications**: Send notifications to patients and staff
- **Analytics**: Track hospital metrics and performance
- **Reports**: Generate various hospital reports

## Project Structure

```
hospital-management/
├── hospital_management/          # Main project folder
│   ├── apps/
│   │   ├── accounts/            # User authentication & management
│   │   ├── patients/            # Patient management
│   │   ├── doctors/             # Doctor management
│   │   ├── appointments/        # Appointment booking
│   │   ├── medical_records/     # Medical records
│   │   ├── billing/             # Billing & payments
│   │   ├── pharmacy/            # Medicines & prescriptions
│   │   ├── lab_tests/           # Lab tests
│   │   ├── inventory/           # Hospital inventory
│   │   ├── staff_scheduling/    # Staff schedules
│   │   ├── wards/               # Ward management
│   │   ├── departments/         # Departments
│   │   ├── notifications/       # Notifications
│   │   ├── analytics/           # Analytics & metrics
│   │   └── reports/             # Reports generation
│   ├── core/                    # Core utilities & base models
│   ├── middleware/              # Custom middleware
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── Dockerfile                   # Docker configuration
└── docker-compose.yml           # Docker Compose configuration
```

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Redis (optional, for caching)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd hospital-management
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from template:
```bash
cp .env.example .env
```

5. Configure database in `.env`

6. Run migrations:
```bash
python manage.py migrate
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Run development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000/api/docs/` for API documentation.

## API Endpoints

All endpoints are under `/api/v1/`:

- **Accounts**: `/api/v1/accounts/`
- **Patients**: `/api/v1/patients/`
- **Doctors**: `/api/v1/doctors/`
- **Appointments**: `/api/v1/appointments/`
- **Departments**: `/api/v1/departments/`
- **Billing**: `/api/v1/billing/`
- **Medical Records**: `/api/v1/medical-records/`
- **Lab Tests**: `/api/v1/lab-tests/`
- **Pharmacy**: `/api/v1/pharmacy/`
- **Inventory**: `/api/v1/inventory/`
- **Notifications**: `/api/v1/notifications/`
- **Staff Scheduling**: `/api/v1/staff-scheduling/`
- **Wards**: `/api/v1/wards/`
- **Analytics**: `/api/v1/analytics/`
- **Reports**: `/api/v1/reports/`

## Docker Setup

Build and run with Docker Compose:
```bash
docker-compose up -d
```

## Testing

Run tests:
```bash
python manage.py test
```

## Admin Panel

Access Django admin panel at `http://localhost:8000/admin/`

## Documentation

API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`

## Technologies

- **Framework**: Django 4.2
- **API**: Django REST Framework
- **Database**: PostgreSQL
- **Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Authentication**: Session + JWT (optional)
- **Task Queue**: Celery + Redis
- **Container**: Docker & Docker Compose

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions, please create an issue in the repository.
