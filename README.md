# HNG CRUD API
# API Documentation: CRUD Operations for "Person" Resource
<p> This documentation provides a step by step guide on how this CRUD API works

## Getting Started
#### Prerequisites
<p> Before you begin, ensure you have the following prerequisites:

<p> Python 3.x installed.
<p> Flask and SQLAlchemy libraries installed (you can install them via pip).
<p> SQLite or your chosen database installed and configured.

## Installation
- Clone the Github repository for the API
``git clone https://github.com/Mamurooyiboluawhore/HNG-CRUD-API```

- Navigate to the project directory.
  ` cd route.py `
- Navigate to the project directory.
```venv
    python -m venv venv 
    source venv/bin/activate 
```
- Install the required packages.
` pip install Flask Flask-SQLAlchemy `
- python app.py

## API Endpoints
#### Create a Person
- Endpoint: '/api'
- HTTP Method: POST
- Description: Create a new person record.
- Request Format: 
- Request Body
```json
    {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
    }    
```
- Response Status Codes:

    - 201 Created: Person created successfully
    - 400 Bad Request: Invalid request data

#### Retrieve a Person
- Endpoint: /api/<int:id>
- HTTP Method: GET
- Description: Retrieve details of a person by ID.
- Response Format: JSON
- Response Status Codes:
- 200 OK: Person details retrieved successfully
- 404 Not Found: Person with the specified ID not found
#### Update a Person
- Endpoint: /api/<int:id>
- HTTP Method: PUT
- Description: Update details of an existing person by ID.
- Request Format: JSON
- Request Body:

```json
{
  "name": "Updated Name",
  "age": 35,
  "email": "updatedemail@example.com"
}
```
- Response Format: JSON
- Response Status Codes:
- 200 OK: Person updated successfully
- 404 Not Found: Person with the specified ID not found
#### Delete a Person
- Endpoint: /api/<int:id>
- HTTP Method: DELETE
- Description: Remove a person by ID.
- Response Format: JSON
- Response Status Codes:
- 204 No Content: Person deleted successfully
- 404 Not Found: Person with the specified ID not found

## Conclusion
This documentation provides a comprehensive guide to using the CRUD API for managing "Person" resources. If you encounter any issues or have questions, please refer to the documentation or contact the API administrator for assistance.
