# E-Food (Django) - Project Skeleton

## Defaults chosen
- Project name: `efood`
- Database: SQLite (default)
- Contact form: EmailJS placeholders included (replace YOUR_EMAILJS_USER_ID, YOUR_SERVICE_ID, YOUR_TEMPLATE_ID)
- Design: Modern Bootstrap-based UI (responsive)

## Setup (local)
1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run server:
   ```
   python manage.py runserver
   ```
6. Access: http://127.0.0.1:8000

## Notes
- Add your EmailJS credentials in `templates/contact.html`.
- Add restaurant/menu images to the `media/` folder or upload via Django admin.
- This is a starting skeleton — extend features like cart, orders, user auth, payments as needed.
