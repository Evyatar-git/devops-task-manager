# DevOps Task Manager

A simple task management web application built with Flask for learning DevOps concepts.

## Features
- Add, complete, and delete tasks
- SQLite database storage
- Bootstrap UI
- Health check endpoint for monitoring

## Local Development

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/Scripts/activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`
6. Visit http://localhost:5000

## Testing
Run tests with: `python -m pytest tests/`

## API Endpoints
- `GET /` - Main task list page
- `GET /add` - Add task form
- `POST /add` - Create new task
- `GET /complete/<id>` - Mark task as complete
- `GET /delete/<id>` - Delete task
- `GET /health` - Health check endpoint

## Next Steps
- Containerize with Docker
- Set up CI/CD pipeline
- Deploy to AWS

## Docker Development

1. Make sure Docker Desktop is running
2. Build the container: `docker-compose build`
3. Run the application: `docker-compose up`
4. Visit http://localhost:5000
5. Stop with Ctrl+C

## Health Check
Visit http://localhost:5000/health to verify the application is running.