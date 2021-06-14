# django_todo_app
#### Demo Todo application using Django and Angular

Install the requirements file.

The application uses **MongoDB server 3.6.8**.
[MongoDB installation](https://docs.mongodb.com/manual/installation/)

***Note: CORS is used in the application and port 8181 for Angular App is whitelisted. Please change the port if required.
The code can be found in settings.py of "keep" folder***
```
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8181',
)
```

#### To run the Django backend
```
python manage.py runserver 8000
```

#### To run the Angular application
```
ng serve --port 8181
```
