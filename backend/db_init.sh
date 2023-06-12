
# delete db.sqlite3
rm -rf db.sqlite3

# delete migrations
rm -rf account/migrations
rm -rf foods/migrations
rm -rf diets/migrations
rm -rf meals/migrations

python manage.py makemigrations account
python manage.py makemigrations foods
python manage.py makemigrations meals
python manage.py makemigrations diets
python manage.py makemigrations


python manage.py migrate account
python manage.py migrate foods
python manage.py migrate meals
python manage.py migrate diets
python manage.py migrate

python manage.py loaddata _Master_data/Food-Category.json
python manage.py loaddata _Master_data/Foods.json