# Healthcare Appointment and Blog API

A robust backend API built with Django and Django REST Framework (DRF) for managing healthcare services. This API supports user authentication with JWT tokens, role-based access for patients and doctors, appointment scheduling, and blog management. Doctors can create and manage their profiles, appointments, and blogs, while patients can book appointments and view doctor profiles and blogs.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**
  - Custom user model with email-based authentication and roles (doctor, patient)
  - Registration and login endpoints using JWT (via djangorestframework-simplejwt)
  
- **Doctor Management**
  - Doctors can create and update their profiles with details like name, specialty, bio, and availability.
  - Public endpoint to list and search for doctors by name or specialty.

- **Appointment Management**
  - Patients can book appointments with doctors.
  - Doctors can view and update the status of appointments (pending, accepted, declined).
  - Patients can cancel their appointments (status updated to "cancelled" rather than deletion).

- **Blog Management**
  - Doctors can create, update, and delete blog posts.
  - Blogs can include an optional image.
  - All users (patients and doctors) can view the blogs.

- **Robust and Secure API**
  - Role-based permissions ensure only authorized users can perform certain actions.
  - JWT token-based authentication for secure API access.

## Tech Stack

- **Backend Framework:** Django 4.x
- **API Framework:** Django REST Framework (DRF)
- **Authentication:** djangorestframework-simplejwt
- **Database:** PostgreSQL (recommended for production) or SQLite (for local development)
- **Image Handling:** Django's ImageField (with media file configuration)
- **Server:** Gunicorn (for production deployment)
- **Deployment:** Render (or similar hosting platforms)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/healthcare-api.git
   cd healthcare-api
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   For local development (SQLite):

   ```bash
   python manage.py migrate
   ```

   For PostgreSQL, update your `DATABASES` settings in `settings.py` or use environment variables with `dj_database_url`.

5. **Collect Static Files**

   ```bash
   python manage.py collectstatic --noinput
   ```

## Configuration

### Environment Variables

Create a `.env` file in your project root with the following variables (adjust values as needed):

```env
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@host:port/dbname  # If using PostgreSQL
```

### Settings Changes

- **Static & Media Files**

  In `settings.py`, set:

  ```python
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

- **JWT Authentication**

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
  }
  ```

## API Endpoints

### User Endpoints

- **Register:** `POST /auth/register/`
  - **Body:**
    ```json
    {
      "email": "doctor@example.com",
      "password": "securepassword",
      "role": "doctor"
    }
    ```
  - **Response:** Confirmation message

- **Login:** `POST /auth/login/`
  - **Body:**
    ```json
    {
      "email": "doctor@example.com",
      "password": "securepassword"
    }
    ```
  - **Response:**
    ```json
    {
      "access": "JWT_ACCESS_TOKEN",
      "refresh": "JWT_REFRESH_TOKEN",
      "email": "doctor@example.com",
      "role": "doctor"
    }
    ```

### Doctor Management Endpoints

- **Create/Update Profile:** `POST/PATCH /doctors/<pk>/`
  - **Requires Authentication:** Only users with role "doctor"
  - **Body (example):**
    ```json
    {
      "name": "Dr. John Doe",
      "specialty": "Cardiology",
      "bio": "Expert in heart health.",
      "availability": true
    }
    ```
- **List/Search Doctors:** `GET /doctors/?search=cardiology`

### Appointment Management Endpoints

- **Create Appointment (Patient Only):** `POST /appointments/create/`
  - **Body (example):**
    ```json
    {
      "doctor": 1,
      "date": "2025-02-01",
      "time": "14:30:00",
      "reason": "General consultation"
    }
    ```
- **List Appointments:** `GET /appointments/`
  - **Behavior:** Returns appointments based on whether the logged-in user is a doctor or a patient.
- **Update Appointment Status (Doctor Only):** `PATCH /appointments/<id>/update-status/`
  - **Body (example):**
    ```json
    {
      "status": "accepted"
    }
    ```
- **Cancel Appointment (Patient Only):** `PATCH /appointments/<id>/cancel/`
  - **No Body Required:** Automatically sets status to "cancelled"

### Blog Management Endpoints

- **Create/List Blogs:** `GET/POST /blogs/`
  - **Create (Doctor Only):** Requires authentication with role "doctor"
  - **Body (example):**
    ```json
    {
      "title": "5 Tips for a Healthy Lifestyle",
      "content": "Eat healthy, exercise regularly, and get enough sleep.",
      "image": <file>  // Optional image upload
    }
    ```
- **Retrieve/Update/Delete Blog:** `GET/PATCH/DELETE /blogs/<id>/`
  - **Update/Delete:** Only the blog's author can update or delete the blog.

## Testing

- **Automated Tests:**
  - Run tests using Django's test framework:
    ```bash
    python manage.py test
    ```
  - For coverage:
    ```bash
    coverage run --source='.' manage.py test
    coverage report
    ```

- **Manual Testing:**
  - Use Postman or cURL to test the endpoints.
  - Verify authentication, role-based permissions, and error handling.

## Deployment

### Deploying on Render

1. **Push Code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Configure Render:**
   - Create a new web service on Render and link your GitHub repository.
   - Set the build command:
     ```bash
     pip install -r requirements.txt && python manage.py migrate
     ```
   - Set the start command:
     ```bash
     gunicorn healthcare_api.wsgi:application
     ```
     *(Replace `healthcare_api` with your actual project name.)*
   - Add environment variables (e.g., `DJANGO_SECRET_KEY`, `DATABASE_URL`, `DEBUG=False`, `ALLOWED_HOSTS`).

3. **Static Files:**
   - Ensure `collectstatic` runs during deployment.
   - Consider using Whitenoise or an external CDN for serving static files.

## Project Structure

A typical structure for the project might look like:

```
healthcare-api/
├── healthcare_api/            # Django project directory (settings, wsgi, urls)
├── users/                     # Custom user app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── doctor/                    # Doctor management app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── appointments/              # Appointment management app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── blogs/                     # Blog management app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── media/                     # Uploaded media files (images, etc.)
├── staticfiles/               # Collected static files
├── requirements.txt           # Python dependencies
├── Procfile                   # For deployment (e.g., Render, Heroku)
└── README.md                  # This file
```

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
