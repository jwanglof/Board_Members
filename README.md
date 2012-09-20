To create an virtual environment (for Python2):
	virtualenv2 <name> --no-site-packages
		--no-site-packages: The environment is clean from the systems' modules

To run a created environment:
	source <name>/bin/activate

What to do on a new Django-project:
	pip install django
	start a new Django project
	pip install south
	edit settings! (make sure to add south in INSTALLED_APPS!)
	syncdb

Tutorials:
	south:
		http://south.readthedocs.org/en/latest/tutorial/part1.html
	Django:
		http://gettingstartedwithdjango.com/resources/ (version 1.2!)
		http://www.re-cycledair.com/up-and-running-with-django-1-4

Docs:
	The different fields a DB can use:
		https://docs.djangoproject.com/en/dev/ref/models/fields/
