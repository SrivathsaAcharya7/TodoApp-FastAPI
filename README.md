
# FastAPI ToDo Application

This is a simple ToDo application built using **FastAPI**. Users can register, log in, add new todos, and edit their todos when they complete a task. The app uses **JWT** for authentication and includes test cases for all components. **Jinja Templates** are used to render the frontend.

## Features

- **User Registration & Login:** Users can create an account or log in if they already have one.
- **JWT Authentication:** Secure API endpoints using JSON Web Tokens.
- **Add/Edit ToDo:** Users can add todos and update them once completed.
- **Test Coverage:** Comprehensive test cases are written for all components.
- **Jinja Templates:** Frontend is rendered using Jinja templates.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLite/PostgreSQL**: Database for storing user and todo data.
- **Jinja Templates**: Template engine for rendering frontend views.
- **JWT**: Used for authentication and securing the API endpoints.
- **Pytest**: For writing and running test cases.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Jinja2
- PyJWT
- Pytest

You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/fastapi-todo-app.git
cd fastapi-todo-app
```

2. **Set up the environment variables:**

Create a `.env` file in the project root and add the following:

```
SECRET_KEY=your_jwt_secret_key
DATABASE_URL=sqlite:///./todos.db
```

3. **Start the FastAPI server:**

```bash
uvicorn main:app --reload
```

4. **Access the application:**

    The application will be available at `http://127.0.0.1:8000`. You can also view the automatically generated API docs at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Authentication

- **Register**: `/register/` (POST)  
  Registers a new user.
- **Login**: `/login/` (POST)  
  Logs in a user and returns a JWT token.

### ToDo

- **Get Todos**: `/todos/` (GET)  
  Get a list of the current user's todos.
- **Add ToDo**: `/todos/` (POST)  
  Add a new todo.
- **Edit ToDo**: `/todos/{id}` (PUT)  
  Edit an existing todo.
  
*Note: Authentication is required for all `/todos/` endpoints using the JWT token.*

## Running Tests

To run the test suite, execute the following command:

```bash
pytest
```

The tests cover the registration, login, and todo functionality of the application.

## Templates

This project uses **Jinja Templates** to render HTML pages for user interfaces. You can find the templates in the `/templates` directory.
