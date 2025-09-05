# 🧳 ALX Travel App 0x00

A Django-based travel listing platform that allows users to browse listings, book stays, and leave reviews. This version (`alx_travel_app_0x00`) includes database models, API serializers, and a seed command for populating the database with sample data.

---

## 📁 Project Structure


alx_travel_app_0x00/
├── alx_travel_app/ # Main Django project settings
├── listings/ # App containing models, serializers, views
│ ├── models.py
│ ├── serializers.py
│ └── management/commands/seed.py
├── manage.py
└── README.md


## API Endpoints

Base URL: `/api/`

| Endpoint             | Method | Description             |
|----------------------|--------|-------------------------|
| `/listings/`         | GET    | List all listings       |
| `/listings/`         | POST   | Create a new listing    |
| `/listings/<id>/`    | PUT    | Update a listing        |
| `/listings/<id>/`    | DELETE | Delete a listing        |
| `/bookings/`         | GET    | List all bookings       |
| `/bookings/`         | POST   | Create a new booking    |
| `/bookings/<id>/`    | PUT    | Update a booking        |
| `/bookings/<id>/`    | DELETE | Delete a booking        |

## Swagger Documentation

Available at: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## To Run Locally

```bash
git clone https://github.com/yourusername/alx_travel_app_0x01.git
cd alx_travel_app_0x01
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
