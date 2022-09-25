# OnePassword

Make different secure passwords for different website using one safe password and different keywords for websites


## Algorithm of Encryption

* Read users onepassword and keyword
* Encrypt hash onepassword using sha256
* Add the keyword to hashed password and again hash it using sha256
* Return hash value as password


## How to Run

Install requirements ```pip install -r requirements.txt```

Setup ```SECRET_KEY``` in ```server/settings.py```

Run the server

```
python manage.py runserver
```
