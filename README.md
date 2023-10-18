# Fast_api
Library Management Application
This project contains a FastAPI application developed to manage basic operations of a library. It includes CRUD operations for managing books and patrons. Additionally, it allows borrowing and returning books by patrons.

Getting Started
These instructions will guide you on how to run the project locally. There is a separate section for running the project using Docker.

Prerequisites
To run this project, you need Python 3.x and Docker installed on your machine.

Installation
Clone the project files to your local machine.
git clone
cd
Create a Python virtual environment and install the required dependencies.
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
Running
You can run the application with the following command:
uvicorn main:app --reload
The application will run at http://localhost:8000 by default.

Usage
Once the application is running, you can manage books and patrons using the provided API endpoints. For example:

Get All Books: GET /books
Get a Specific Book: GET /books/{id}
Add a New Book: POST /books
Update a Book: PUT /books/{id}
Delete a Book: DELETE /books/{id}
Similar endpoints exist for patrons as well.

Running with Docker
You can run the application using Docker with the following command:
docker-compose up --build
The application will run inside Docker at http://localhost:8000.

Contributing
If you would like to contribute to the project, please create a new branch, make your changes, and submit a pull request. Your contributions are appreciated!
