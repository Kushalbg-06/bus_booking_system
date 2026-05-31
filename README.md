<<<<<<< HEAD
# Travel Bus Backend

A REST API backend for a bus booking system built with **FastAPI** and **SQLAlchemy**. It supports user authentication, bus and route management, seat tracking, and booking operations.

## Features

- User registration and JWT-based login
- CRUD operations for buses, routes, and users
- Seat availability per bus
- Booking creation, listing, and cancellation (booking router)
- SQLite database with automatic table creation on startup
- Interactive API docs via Swagger UI

## Tech Stack

| Layer        | Technology              |
| ------------ | ----------------------- |
| Framework    | FastAPI                 |
| ORM          | SQLAlchemy              |
| Database     | SQLite                  |
| Auth         | JWT (python-jose)       |
| Password hashing | Argon2 (passlib)    |
| Server       | Uvicorn                 |

## Project Structure

```
travel_bus_backend/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── models.py               # SQLAlchemy models
│   ├── database.py             # DB engine and session
│   ├── hashing.py              # Password hashing utilities
│   ├── authentication/
│   │   ├── auth.py             # Register & login routes
│   │   ├── token.py            # JWT creation & verification
│   │   └── oauth.py            # OAuth2 bearer dependency
│   ├── routers/
│   │   ├── user_router.py      # User CRUD
│   │   ├── bus_router.py       # Bus CRUD
│   │   ├── route_router.py     # Route management
│   │   ├── seat_router.py      # Seat listing
│   │   └── booking_router.py   # Booking operations
│   └── schemas/
│       ├── users.py
│       ├── buses.py
│       ├── routes.py
│       ├── seats.py
│       └── booking.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10+
- pip

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd travel_bus_backend
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

From the project root:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

On first run, a `database.db` SQLite file is created automatically in the project root.

## API Endpoints

### General

| Method | Endpoint | Description        |
| ------ | -------- | ------------------ |
| GET    | `/`      | Health check       |

### Authentication (`/auth`)

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| POST   | `/auth/register` | Register a new user      |
| POST   | `/auth/login`    | Login and receive a JWT  |

**Register request body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "yourpassword"
}
```

**Login request body:**

```json
{
  "email": "john@example.com",
  "password": "yourpassword"
}
```

**Login response:**

```json
{
  "access_token": "<jwt>",
  "token_type": "bearer"
}
```

### Users (`/users`)

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/users/`     | Create a user     |
| GET    | `/users/`     | List all users    |
| GET    | `/users/{id}` | Get user by ID    |
| DELETE | `/users/{id}` | Delete a user     |

### Buses (`/buses`)

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| POST   | `/buses/`        | Add a new bus      |
| GET    | `/buses/`        | List all buses     |
| GET    | `/buses/{id}`    | Get bus by ID      |
| PUT    | `/buses/{bus_id}`| Update a bus       |
| DELETE | `/buses/{id}`    | Delete a bus       |

**Bus request body:**

```json
{
  "bus_number": "BUS-101",
  "origin": "City A",
  "destination": "City B",
  "departure_time": "08:00",
  "arrival_time": "14:00",
  "total_seats": 40
}
```

### Routes (`/route`)

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| POST   | `/route/`     | Add a new route    |
| GET    | `/route/`     | List all routes    |
| DELETE | `/route/{id}` | Delete a route     |

**Route request body:**

```json
{
  "origin": "City A",
  "destination": "City B",
  "distance": 350,
  "duration": 6.5
}
```

### Seats (`/seat`)

| Method | Endpoint     | Description              |
| ------ | ------------ | ------------------------ |
| GET    | `/seat{id}`  | List seats for a bus     |

### Bookings (`/booking`)

> The booking router is defined in `app/routers/booking_router.py`. Mount it in `main.py` to enable these endpoints.

| Method | Endpoint                  | Description              | Auth required |
| ------ | ------------------------- | ------------------------ | ------------- |
| POST   | `/booking/`               | Book a seat              | Yes           |
| GET    | `/booking/my`             | Get current user's bookings | Yes        |
| DELETE | `/booking/cancel/{booking_id}` | Cancel a booking   | Yes           |

## Database Models

| Model    | Fields                                                                 |
| -------- | ---------------------------------------------------------------------- |
| User     | id, name, email, password                                              |
| Bus      | id, bus_number, origin, destination, departure_time, arrival_time, total_seats, is_cancelled |
| Seats    | id, bus_id, seat_number, is_booked                                     |
| Booking  | id, user_id, bus_id, seat_id, booking_time, seat_status                |
| Route    | id, origin, destination, distance, duration                            |

## Authentication

Protected endpoints expect a Bearer token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

Tokens are signed with HS256 and expire after 30 minutes by default.

## License

This project is for educational and development purposes.
=======
# bus_booking_system(backend) 
tech stack:FastAPI,Sqllite,RestAPI

need to add more
>>>>>>> 9117be4692d7395e36d28a5189880db3d6cc7dc1
