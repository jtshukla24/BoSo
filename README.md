# H.Ledger School
This is a Django 2.0+ project with information about an educational institution, demonstrating mapping of URLs, their flow of requests
and corresponding responses with Login and Registration portal. The project is deployed on PythonAnywhere so it is optimized for that but is not necessary.

## Features

1.  Django based Backend Structure which includes commands, static and media files, templates,etc.
2.  A basic log-in and registration functionality is available for project production environment.
3.	Frontend with HTML, CSS, Bootstrap
4.	Includes PyCharm project configuration.
5.	Primary repo is in GitHub

## Requirements

1. [Python v3+](https://www.python.org/downloads/)
2.	[Django v2+](https://www.djangoproject.com/download/)
3.	[PyCharm](https://www.jetbrains.com/pycharm/)
4. 	HTML, CSS, [Bootstrap]( https://getbootstrap.com/docs/4.4/getting-started/download/)
4.  Recommended [MySQL v8.0]( https://www.mysql.com/downloads/)
    ### OR
    sqlite3 (Python built-in database )

## Getting Started

1.	If you’re cloning the repo, you should have [Git Bash]( https://desktop.github.com/) installed on the system and then you can use following command :
    ```bash
    $ git clone https://github.com/jtshukla24/BoSo.git
    ```
    ### OR
    you can download it from  **Clone or Download** button in repo.

2.	Install [Python]( https://www.python.org/downloads/) and later using pip, use following command:
    ```bash
    $ pip install django==2.0   (for specific version)
    
    $ pip install django        (for latest version)

3.	You can setup the project environment by setting up the project interpreter by navigating to the path where you have installed Python.

4.	For setting up the database, you can change 'DATABASES’ variable in **_settings.py_** file in project directory.

5.	Setup Database to either MySQL or sqlite3. For using MySQL, you need to setup a database named, **newboso**, in MySQL.
    ```bash
    mysql> create database newboso;
    
    mysql> use newboso;
  

To see data in sqlite3, you can use [DB Browser]( https://sqlitebrowser.org/dl/)

6.	After setting up the project, you can either run **Run manage.py task** from **Tools** menu 

    ### OR
    
    You can use following command in terminal:
    ```bash
    C:/**Project Path**> python manage.py runserver
    ```
	
## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.



