# Bikom

Bikom is stand for "Bimbingan Konseling Telkom Bandung" in Indonesian. This web app, used for making appointment for the student
to consult something (or anything really...) to their "BK (Bimbingan Konseling)" teacher. 

TODO
- [ ] Basic CRUD to the profile of the student (ongoin)
- [ ] Teacher can issue and assignment (survey)
- [ ] Student can make an appointment
- [ ] Notification system (idk, it's gonna realtime or not...)

## Quick Start

Make sure python is installed and can be accessed via terminal or cmd or powershell.

### Linux/Unix
```console
$ git clone https://github.com/Lukmanhakim112/bikom
$ cd bikom
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py compilemessages
$ python manage.py runserver
```

### Windows
```console
$ git clone https://github.com/Lukmanhakim112/bikom
$ cd bikom
$ py -m venv venv

for cmd:
$ venv\Scripts\activate.bat

for powershell:
$ venv\Scripts\Activate.ps1

$ pip install -r requirements.txt
$ py manage.py migrate
$ py manage.py compilemessages
$ py manage.py runserver
```
If the server is running, that mean you install it successfully.

## Resources

1. Illustration taken from: https://undraw.co/ checkout their website, it's very cool!
