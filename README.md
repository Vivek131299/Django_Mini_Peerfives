# Mini Peerfives #

## Problem Statement ##

Mini Peerfives allows users to reward other people with peerfives (P5) points.
1) P5 - Points that can be given to others
2) Rewards - Points that are earned and can not be given to others


## Project Setup ##

1) Clone the repository.

2) Open terminal and cd into the root project directory (where manage.py and requirements.txt file exists).

3) Create a new virtual environment with command: `python -m venv venv`

4) Activate the virtual environment using command(for Windows): `.\venv\Scripts\activate`

5) Install required python packages (including django) using requirements.txt file with command: `pip install -r requirements.txt`

6) Set up a database: Create a MySQL database/schema with the name "mini_peerfives".
Update the database credentials (user and password) in settings.py file.

7) Run following commands for applying database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

8) Start the server with the command: `python manage.py runserver`

9) If everything is configured correctly, the application will start and will be accessible on the url - http://127.0.0.1:8000/

10) For testing, you may have to create few users using 'Create new user' button on the landing page.

11) NOTE: Both backend and frontend is being done in Django.