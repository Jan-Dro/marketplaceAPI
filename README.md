# Welcome to my Craigslist API Backend!

## Endpoints

These are the endpoints! Remember to use `127.0.0.0.0:8000/<endpoints>` when making requests:
- `/categories/` GET POST 
- `/categories/<category_id>` GET PUT DELETE
- `/categories/<category_id>/posts` GET POST
- `/categories/<category_id>/posts/<post_id>` GET PUT DELETE

## Setup

**Step 1: Create a Virtual Environment (Optional but Recommended)**
python -m venv venv

**Step 2: Activate the Virtual Environment**
**Windows**
venv\Scripts\activate
**MacOS**
source venv/bin/activate

```bash
**Step 3: Install all the dependencies**
pip install -r requirements.txt

**Step 4: Create Database Migrations**
python manage.py makemigrations

**Step 5: Start Docker Containers**
docker compose up

**Step 6: Apply Database Migrations**
python manage.py migrate

**ONCE everything is running correctly, go ahead and run django server**

**Step 7: Start the Django Development Server**
python manage.py runserver 

**have fun trying out my endpoints! **
and Happy coding!:D