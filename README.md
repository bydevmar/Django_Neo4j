# Django_neo4j

## Overview

Django_neo4j is a sample repository demonstrating how to integrate a Django web application with a Neo4j graph database. This repository provides a simple example to get you started with building Django applications that utilize the powerful capabilities of Neo4j for managing and querying connected data.

## Requirements

- Python (>=3.6)
- Django (>=3.x)
- Neo4j (>=4.x)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/Django_neo4j.git
    ```

2. Install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Neo4j database. You can download and install Neo4j from [here](https://neo4j.com/download/). Make sure to start the Neo4j server.

4. Configure your Django application to connect to the Neo4j database. You can find the database connection settings in `settings.py`.

5. Run the migrations to create the necessary database schema:

    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the Django application by navigating to `http://localhost:8000` in your web browser. You can now explore the sample application, which demonstrates basic CRUD operations with a Django model connected to a Neo4j database.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
