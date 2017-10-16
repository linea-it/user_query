# create environment
cd PROJECT_DIR
virtualenv --python=`which python3` env
source env/bin/activate
pip install -r requirements.txt

# creates database tables
cd user_query/
python manage.py migrate

# optional
python manage.py createsuperuser

# run app
python manage.py runserver
