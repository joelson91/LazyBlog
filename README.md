# Lazy Blog

A simple system for creating and managing blogs, developed with Django.

## Description

This project is a blogging system that allows users to create, edit, and delete posts. The goal is to provide a simple
and intuitive platform for sharing ideas and experiences.

## Installation

Follow the steps below to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/joelson91/LazyBlog.git
   cd LazyBlog
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

After starting the server, you can:

- Create a user account.
- Log in and start creating posts.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -m 'Adds new feature'`).
4. Push to the remote repository (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).