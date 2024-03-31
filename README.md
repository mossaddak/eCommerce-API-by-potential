# ecommerce

All the backend business logics are connected to the <b>ecommerce</b> project. It's a Django project running Django REST Framework as well as simple product listing using Django Template.


## API Document

    http://127.0.0.1:8000/api/v1/docs

---

**Setting up a virtualenv**

virtualenv is a nifty tool for creating virtual environments for Python projects

    cd ~
    python3 -m venv env
    source ~/env/bin/activate


**Install the Python dependencies for the project**

Run

    pip install -r ~/project/requirements/development.txt

**Run the test server**

    cd ~/project
    python projectile/manage.py runserver 0:8000

You can now visit 127.0.0.1:8000 on your browser and see that the project is running.
