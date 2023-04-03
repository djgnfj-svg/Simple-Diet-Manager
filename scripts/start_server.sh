#!/bin/bash
DEPLOY_PATH=/home/ubuntu
PROJECT_NAME="Simple-Diet-Manager"
PROJECT_BACKEND_NAME="backend"
PROJECT_BACKEND_PATH=$PROJECT_NAME/$PROJECT_BACKEND_NAME

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME


# 깃 클론
cd $DEPLOY_PATH/
git clone https://github.com/djgnfj-svg/Simple-Diet-Manager.git

# 시크릿 파일 이동
cp $DEPLOY_PATH/.secrets.json $PROJECT_BACKEND_PATH/.secrets.json


# requirements.txt 설치
pip install -r $PROJECT_BACKEND_PATH/requirements.txt
#static file
python3 $PROJECT_BACKEND_PATH/manage.py collectstatic
#migrate
python3 $PROJECT_BACKEND_PATH/manage.py makemigrations
python3 $PROJECT_BACKEND_PATH/manage.py migrate

# load data RDS일 경우 조금 거시기해짐...
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Food-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Cooking-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Foods.json


# npm 설치
cd $PROJECT_NAME/frontend

# node update
sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install nodejs


# npm install
sudo npm i
sudo chown -R $USER:$USER /home/ubuntu/Simple-Diet-Manager/frontend/node_modules

# npm build
sudo npm run build


# 구니콘 설정 이동
#  TODO : 너무 하드 코딩이다. 나중에 수정해야함
cd ..
sudo cp web/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# 구니콘 실행
sudo mkdir /logs
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart gunicorn

# robots.txt sitemap.xml
sudo cp web/robots.txt /etc/nginx/sites-available/robots.txt
sudo cp web/sitemap.xml /etc/nginx/sites-available/sitemap.xml

# nginx 설정 이동
#  TODO : 너무 하드 코딩이다. 나중에 수정해야함
sudo cp web/nginx.conf /etc/nginx/sites-available/nginx.conf

# nginx 링크
sudo ln /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

# nginx 실행
sudo service nginx restart
