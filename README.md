# Learning FastAPI

A beginner-friendly CRUD REST API built with **FastAPI** and **Python**.

This project demonstrates how to build a REST API with request validation, JSON-based data storage, custom middleware, automatic API documentation, and Docker containerization.

---

## 🚀 Features

- REST API built with FastAPI
- CRUD operations for issues
- JSON file-based data storage
- Request and response validation using Pydantic
- Custom middleware for request timing
- Automatic API documentation with Swagger UI
- Automatic OpenAPI documentation
- Docker support
- Easy local development setup

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| Pydantic | Data validation |
| JSON | Data storage |
| Docker | Containerization |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```text
Learning fastapi/
│
├── app/
│   ├── middleware/
│   │   └── timer.py
│   ├── routes/
│   │   └── issues.py
│   ├── schemas.py
│   └── storage.py
│
├── data/
│   └── issues.json
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

### File and Directory Description

- `app/` — Contains the main application modules.
- `app/routes/issues.py` — Contains the API routes related to issues and CRUD operations.
- `app/schemas.py` — Contains Pydantic schemas used for validating API data.
- `app/storage.py` — Handles reading and writing issue data.
- `app/middleware/timer.py` — Contains custom middleware used to measure request processing time.
- `data/issues.json` — JSON file used as the project's data store.
- `main.py` — Main entry point of the FastAPI application.
- `requirements.txt` — Python dependencies required by the project.
- `Dockerfile` — Instructions for building the Docker image.
- `.dockerignore` — Files and directories excluded from the Docker build context.

---

# ⚙️ Getting Started

## Prerequisites

Make sure the following are installed:

- Python 3.9 or later
- pip
- Git

For Docker usage:

- Docker Desktop or Docker Engine

---

# 💻 Running Locally

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "Learning fastapi"
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Virtual Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Start the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Swagger UI allows you to:

- View available endpoints
- See request parameters
- See request/response schemas
- Send API requests
- Test CRUD operations directly from your browser

## ReDoc

```text
http://localhost:8000/redoc
```

## OpenAPI Schema

```text
http://localhost:8000/openapi.json
```

---

# 🔄 CRUD Operations

The API follows the standard CRUD pattern:

| Operation | Description |
|-----------|-------------|
| Create | Add a new issue |
| Read | Retrieve existing issues |
| Update | Modify an existing issue |
| Delete | Remove an issue |

The exact endpoints and request schemas can be viewed through Swagger UI at:

```text
http://localhost:8000/docs
```

---

# 🗄️ Data Storage

The project currently uses a JSON file instead of a database.

Data is stored in:

```text
data/issues.json
```

The storage module handles reading and writing data to this file.

Using JSON keeps the project simple and useful for learning REST APIs, CRUD operations, request validation, and file-based persistence.

For a production application, a proper database would generally be more appropriate.

---

# 🐳 Running with Docker

The project includes Docker support so the application can run inside a container.

## 1. Build the Docker Image

From the project root:

```bash
docker build -t learning-fastapi .
```

This creates a Docker image named:

```text
learning-fastapi
```

## 2. Run the Docker Container

```bash
docker run -p 8000:8000 learning-fastapi
```

The application will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## 3. Stop the Container

If the container is running in the foreground, press:

```text
Ctrl + C
```

---

# 🐳 Docker Configuration

The Dockerfile:

1. Uses Python 3.9
2. Sets `/app` as the working directory
3. Copies `requirements.txt`
4. Installs the required dependencies
5. Copies the application source code
6. Exposes port `8000`
7. Starts the FastAPI application using Uvicorn

The application is started inside the container using:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

# 🔒 .dockerignore

The project uses a `.dockerignore` file to prevent unnecessary files from being included in the Docker build context.

Examples include:

```text
.venv
__pycache__
*.pyc
.git
.gitignore
```

This helps keep the Docker build context smaller and prevents local development files from being included in the image.

---

# 📦 Dependencies

The project's Python dependencies are stored in:

```text
requirements.txt
```

The main dependencies include:

- FastAPI
- Uvicorn
- Pydantic

Install them with:

```bash
pip install -r requirements.txt
```

---

# 🧪 Testing the API

After starting the application, open:

```text
http://localhost:8000/docs
```

From Swagger UI, you can test the available API endpoints.

A typical CRUD workflow is:

```text
Create Issue
     ↓
Read Issue
     ↓
Update Issue
     ↓
Read Updated Issue
     ↓
Delete Issue
```

---

# 🏗️ Application Architecture

```text
                    ┌─────────────────┐
                    │     Client      │
                    │ Browser / API   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    │    main.py      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Routes      │
                    │   issues.py     │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
             ┌─────────────┐   ┌─────────────┐
             │  Schemas    │   │   Storage   │
             │  Pydantic   │   │    JSON     │
             └─────────────┘   └──────┬──────┘
                                      │
                                      ▼
                              ┌──────────────┐
                              │ issues.json  │
                              └──────────────┘
```

---

# 🐳 Docker Architecture

```text
                 Your Computer
                      │
                      │ localhost:8000
                      ▼
             ┌──────────────────┐
             │ Docker Container │
             │                  │
             │     FastAPI      │
             │       +          │
             │    Uvicorn       │
             │       +          │
             │   JSON Storage   │
             └──────────────────┘
```

---

# 🌱 Development

During local development:

```bash
source .venv/bin/activate
```

Then:

```bash
uvicorn main:app --reload
```

The `--reload` option automatically restarts the server when code changes are detected.

---

# 🔀 Git Workflow

Check the current changes:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Update project"
```

Push to GitHub:

```bash
git push
```

---

# 🚀 Deployment

The project can be deployed using platforms that support Python applications or Docker containers.

Possible deployment options include:

- Render
- Railway
- Fly.io
- Other Docker-compatible hosting platforms

When deploying the Docker version, the platform should use the included `Dockerfile`.

> **Note:** The current application uses a JSON file for storage. Container-based deployments may have ephemeral filesystems, so persistent data should be moved to a proper database or persistent storage solution for production use.

---

# 🔮 Future Improvements

- [ ] Add automated tests with Pytest
- [ ] Replace JSON storage with PostgreSQL
- [ ] Add authentication and authorization
- [ ] Add better error handling
- [ ] Add environment variables
- [ ] Add Docker Compose
- [ ] Add CI/CD pipeline
- [ ] Add database migrations
- [ ] Improve API validation
- [ ] Add production logging
- [ ] Deploy the Dockerized application

---

# 📖 What I Learned

This project was built to practice:

- FastAPI fundamentals
- REST API development
- CRUD operations
- Pydantic models
- API request validation
- Middleware
- JSON-based storage
- Uvicorn
- Virtual environments
- Docker
- Docker images and containers
- Git and GitHub
- API documentation with Swagger

---

# 📌 Project Status

**Status:** 🚧 In Development

The basic CRUD API and Docker configuration are implemented. Additional features and production improvements may be added in the future.

---

# 👨‍💻 Author

**Aakash**

Built while learning and practicing **FastAPI, REST APIs, Docker, and backend development**.
