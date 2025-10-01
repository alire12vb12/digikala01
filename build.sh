set -o errexit 
pip install -r requirements.txt
python manage.py migrate
python manage.py migrate createsuperuser --noinput
python manage.py migrate collectstatic --noinput

