# alx_travel_app

A Django REST Framework (DRF) project for managing travel listings, bookings, and reviews.  
This project provides APIs to create, retrieve, and manage travel-related data, with built-in API documentation.  

---

## Features

- **Listings**: Create, view, update, and delete travel listings with details such as title, description, location, price, and availability.  
- **Bookings**: Book a listing by providing user details and booking dates. View existing bookings.  
- **Reviews**: Users can leave reviews for listings, including a rating and comment.  
- **Serializers**: Data representation through Django REST Framework serializers.  
- **Database Seeder**: A management command to populate the database with sample listings for testing and development.  
- **API Documentation**: Interactive Swagger UI and ReDoc interfaces for testing and exploring endpoints.  

---

## Project Structure

```
alx_travel_app/
│
├── alx_travel_app/           # Main project folder
│   ├── settings.py
│   ├── urls.py               # Includes Swagger/ReDoc routes
│   └── wsgi.py
│
├── listings/                 # App containing models, serializers, and views
│   ├── models.py             # Defines Listing, Booking, and Review models
│   ├── serializers.py        # Serializers for API data representation
│   ├── views.py              # Viewsets and API logic
│   ├── urls.py               # App-specific routes
│   └── management/
│       └── commands/
│           └── seed.py       # Seeder command to populate sample data
│
├── db.sqlite3                # SQLite database (default)
└── manage.py
```

---

## Models

### Listing
- `title` (CharField)  
- `description` (TextField)  
- `location` (CharField)  
- `price` (DecimalField)  
- `available` (BooleanField, default=True)  
- `created_at` (DateTimeField, auto_now_add=True)  

### Booking
- `user_name` (CharField)  
- `listing` (ForeignKey → Listing)  
- `start_date` (DateField)  
- `end_date` (DateField)  
- `created_at` (DateTimeField, auto_now_add=True)  

### Review
- `listing` (ForeignKey → Listing)  
- `user_name` (CharField)  
- `rating` (IntegerField, validators 1–5)  
- `comment` (TextField, optional)  
- `created_at` (DateTimeField, auto_now_add=True)  

---

## Installation & Setup

1. **Clone the project**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed the database with sample data**
   ```bash
   python manage.py seed
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

| Endpoint                   | Method | Description                             |
|-----------------------------|--------|-----------------------------------------|
| `/api/listings/`           | GET    | List all listings                       |
| `/api/listings/`           | POST   | Create a new listing                    |
| `/api/listings/{id}/`      | GET    | Retrieve details of a single listing    |
| `/api/listings/{id}/`      | PUT    | Update a listing                        |
| `/api/listings/{id}/`      | DELETE | Delete a listing                        |
| `/api/bookings/`           | GET    | List all bookings                       |
| `/api/bookings/`           | POST   | Create a new booking                    |
| `/api/reviews/`            | GET    | List all reviews                        |
| `/api/reviews/`            | POST   | Create a review for a listing           |

---

## API Documentation

Interactive API documentation is available:  

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)  

To enable docs, install the required package:

```bash
pip install drf-yasg
```

---

## Tech Stack

- **Python 3.x**  
- **Django 5.x**  
- **Django REST Framework**  
- **drf-yasg (Swagger/ReDoc)**  
- **SQLite (default, can be replaced with PostgreSQL/MySQL)**  

---
