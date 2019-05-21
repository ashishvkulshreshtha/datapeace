# DataPeace Assignment


DataPeace Assignment is a `CRUD REST API` project created with `Django Rest Framework`. Following are the key features of the project.

  - Listing of the User Profile with search and sorting feature.
  - Retrieve single User profile by Unique ID
  - Update existing User Profile
  - Delete Existing User Profile



### Installation

DataPeace Assignment need [Django](https://www.djangoproject.com/) v2+ to run.
Install the dependencies and start the server for dev environments.

```sh
$ git clone https://github.com/ashishvkulshreshtha/datapeace.git
$ virtualenv env
$ source env/bin/activate
$ cd datapeace_assignment
$ pip install -r requirements.txt
$ ./manage.py runserver
$ http://localhost:8000/
```

### Run
>Get the list of users.
`GET` `http://datapeace.pythonanywhere.com/api/users/`
>Retrieve User data by id.
`GET` `http://datapeace.pythonanywhere.com/api/users/<id>,`
>Create New User Entry
`POST` `http://datapeace.pythonanywhere.com/api/users/`
```JSON
{
    "first_name": "Ashish",
    "last_name": "Kulshreshtha",
    "company_name": "datacultr",
    "city": "Gurugram",
    "state": "Haryana",
    "zip": 122002,
    "email": "ashish@gmail.com",
    "web": "http://ashish.com",
    "age": 25
}
```

>Update existing User Entry
`PUT` `http://datapeace.pythonanywhere.com/api/users/1/`
```JSON
{
    "first_name": "Ashish",
    "last_name": "Kulshreshtha",
    "company_name": "datacultr",
    "city": "Gurugram",
    "state": "Haryana",
    "zip": 122002,
    "email": "ashish@gmail.com",
    "web": "http://ashish.com",
    "age": 25
}
```
>Delete existing User Entry
`DELETE` `http://datapeace.pythonanywhere.com/api/users/1/`

Thanks :)