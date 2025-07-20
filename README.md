This is the backend RESTful API for an E-commerce platform, built using [Django REST Framework ]. It handles core functionality such as user authentication, product listings, cart management, order processing, and payments.

> 💡 **Frontend Repository:** [E-commerce Frontend]([https://github.com/yourusername/ecommerce-frontend](https://github.com/Aragorn3022/Ecommerce-Frontend))  

---

## 📌 Features

- User registration, login, and JWT-based authentication
- Product catalog (CRUD)
- Categories & filters
- Shopping cart and checkout
- Order placement and tracking
- Admin dashboard APIs

---

## 🛠️ Tech Stack

- **Backend Framework:** Django + Django REST Framework / Express.js / FastAPI *(edit accordingly)*
- **Database:** MySQL 
- **Authentication:** JWT

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.10+ / Node.js 18+ *(depending on tech stack)*
- PostgreSQL / MongoDB installed
- `pip` / `npm` / `yarn`
- `virtualenv` (for Python projects)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ecommerce_api.git
cd ecommerce_api

# Create virtual environment (Python)
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
