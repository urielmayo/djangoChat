# Django Chat APP

This is a chat app using django and bootstrap. 

You can sign in, sign up and chat with everyone who has signed in.

This project is currently using sqlite3 as database.

## intallation:

- Install requierements
```
pip3 install -r requirements.txt
```

- Generate a secret key. You can use [Djecrety](https://djecrety.ir/) for example.


- Create .env file to store the secret key:
```
echo 'SECRET_KEY=your_secret_key' > djangochat/.env

# you can do this manually, creating a .env file inside djangochat directory
# and writing SECRET_KEY=<your_secret_key> in the first line
```

- Run django commands to generate migrations and run de server
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```