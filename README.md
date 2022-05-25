# urich_tz
    git clone https://github.com/JackScher/urich_tz.git
    cd urich_tz
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd app
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py runserver
