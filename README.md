# Django Blog

**Learning Django framework - blog app**
Scalable blog made with the Django Framework. Deployed to an Apache server in an EC2 instance. An S3 bucket is used to store images and AWS RDS is used to store content.


# Script Commands


**Install All Dependencies**

    pip install requirements.txt

**run server, port 8000 default** 

    python manage.py runserver

**------------------------------------**


**Create a New app** 

    python manage.py startapp sampleApp

**Open a DJango shell to manage \models** 

    python manage.py shell

**initiate db migration** 

    python manage.py makemigrations

**Migrate DB**

    python manage.py migrate

**-------------------------------**

**Get requirements from current project scope**

    pip freeze > requirements.txt

**Upgrade requirements**

    pip install --upgrade -r requirements.txt
