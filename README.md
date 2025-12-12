# fastapi-demo

A full-stack demo application built while learning modern web development using **FastAPI**, **React.js**, and **PostgreSQL**.
This project focuses on understanding backend API development, frontend integration, database connectivity, and full-stack communication.

---

## Tech Stack

### **Frontend**

* **React.js**
* Fetch/Axios for API calls
* Simple UI for interacting with backend routes

### **Backend**

* **FastAPI** – high-performance Python API framework
* **Uvicorn** – ASGI server
* **SQLAlchemy** – ORM for database modeling
* **Pydantic** – data validation and schema handling
* **PostgreSQL** – relational database

---

## Purpose of This Project

This repository is part of my learning journey into full-stack development.
The goals include:

* Building REST API endpoints using FastAPI
* Connecting FastAPI to a PostgreSQL database
* Using SQLAlchemy ORM for models
* Validating and structuring data with Pydantic
* Creating a simple React frontend to interact with API
* Understanding frontend ↔ backend communication
* Practicing CRUD operations (Create, Read, Update, Delete)
* Structuring a real full-stack project

---

## Backend Setup (FastAPI)

### 1️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_demo
```

### 4️⃣ Run the FastAPI server

```bash
uvicorn main:app --reload
```

API Docs available at:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## Frontend Setup (React)

### 1️⃣ Navigate to the frontend folder

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Start the React development server

```bash
npm start
```

The UI runs at:

**[http://localhost:3000](http://localhost:3000)**

---

## Database

This project uses **PostgreSQL**.

Create a database:

```sql
CREATE DATABASE fastapi_demo;
```

Make sure your `.env` file contains correct credentials.

---

## Features

* FastAPI backend
* PostgreSQL database connection
* SQLAlchemy models & CRUD
* Pydantic schemas
* React frontend UI
* Full frontend ↔ backend communication
* API documentation via Swagger UI
* Simple demo to practice full-stack concepts

---

## Notes

This is a learning project — not intended for production use.
It will evolve as more concepts are explored.