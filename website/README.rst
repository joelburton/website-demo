Ubermelon Website Django Example
================================

This is the example Django project we built together.

This interesting stuff is mostly in `planner`, the application for
projects & tasks.

To install::

    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt

To make the database (only have to do once)::

    (env) $ python manage.py migrate
    (env) $ python manage.py createsuperuser

To run the tests::

    (env) $ python manage.py test

To run the server::

    (env) $ python manage.py runserver

Then visit:

- http://localhost:8000/admin/ and add some projects + related tasks
- http://localhost:8000 to browse the site.

Happy exploring!

- Joel
