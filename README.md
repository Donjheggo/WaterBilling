# Water Billing Management System with SMS API from twillio using [Python - Django Framework]
This was Developed By [Fermilan, Christian Jhegg](https://www.facebook.com/Donjheggo/) a Student @ [Surigao del Norte State University](https://snsu.edu.ph/)


You can ADD a STAR ⭐️  if you like this project 👆

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*


### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/Donjheggo/OnlineVotingSystem.git
```

Then, Enter the project
```
$  cd snsucomelec
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Run migrations and migrate**
```python manage.py makemigrations```
```python manage.py migrate```

**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```

Then Add Email and Password


## For Sponsor or Projects Enquiry
1. Email - christianjheggfer@gmail.com
2. LinkedIn - [donjheggo](www.linkedin.com/in/donjheggo)
2. Facebook - [donjheggo](https://www.facebook.com/Donjheggo)


## How the system works
Administrator is required to add clients and set metrics for billing.


## Can OTP verification be bypassed ?
Yeah, sure.
Open `settings.py` and toggle `OTP` to  `False`
Then, wait till server restarts

## If OTP is True
Fill up the OTP_EMAIL and OTP_PASSWORD in settings.py
then go to your gmail settings and allow less secure apps for smtp to enable
tutorial - [How to Setup Gmail SMTP Server](https://www.youtube.com/watch?v=1YXVdyVuFGA)


## Open to contribution ?
Yeah. Pull requests are welcomed.

## Having any issue using this ?
Please, let us know. Open up an issue. 
