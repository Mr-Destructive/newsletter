## Newsletter App 

### A Python/Django Application to fetch latest articles from RSS Feeds of some Programming/Developer Blogging sites and parse them in a Newsletter email.

The Newsletter App has several components like feed aggregator into the database, email form, newsletter subscription form and the actual website for interacting with all the components.

Firstly, thee Newsletter Subscription form allows to get email from the users and saves into the database, next using the feedparser module in Python we extract RSS feeds and grab the article tittles and links.
Lastly, the content is stored in a database and fetched into the mail form and is rendered as a HTML template and the mail is sent.

## Techstack
- Python
- Python Libraries (crispy forms, feedparser, dateutil, psycopg2, etc)
- Django
- PostgreSQL
- Bootstrap + HTML + CSS


We have used Django for creating the webapp, PostgreSQL as the local database, Python modules and libraries for aggregating feed and sending mail.

## Installation:

Clone the repository in your system. 

```
git clone https://github.com/Mr-Destructive/newsletter
```

Python should be installed along with pip.
PostgreSQL is used in this application so that can be instlled from here.

Install the virtualenv package in Python

```
pip install virtualenv
```

Create a virtualenv in the current folder

```
virtualenv venv
```

Activate the virtualenv 

For Windows:
```
source venv\Scripts\activate
```

For Linux:
```
source venv/bin/activate
```   

Install the dependencies with pip

```
pip install -r requirements.txt
```

Create the Database in pgAdmin with a name `newsletter`
Kepp the host to default as `postgres`
You can keep the password as `@1234567` or change in this file [settings.py](https://github.com/Mr-Destructive/newsletter/blob/main/newsletter/settings.py)
Your password can be hardcoded in the settings.py file -> Database section -> password field. 

To create an account:
- Username
- User Email
- Password
- [Google App Password](https://myaccount.google.com/apppasswords) (2FA required)

To create Admin account:

```
python manage.py createsuperuser
```
Give in your details to be used in accessing the webapp

**Make sure the venv(virtual environemnt) is activated while doing anything(running commands) in the terminal**

To run the server:
```
python manage.py runserver
```

You will see the homepage with the latest posts from dev.to / medium.com / techrepublic / geeksforgeeks/ hackernoon 

![newsletter-app-homepage](https://res.cloudinary.com/dgpxbrwoz/image/upload/v1638449223/temp/newsletter-dj_qksz7k.png)


