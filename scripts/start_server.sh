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
cp -r $DEPLOY_PATH/.secrets.json $PROJECT_BACKEND_PATH/.secrets.json


# requirements.txt 설치
pip install -r $PROJECT_BACKEND_PATH/requirements.txt
#static file
python3 $PROJECT_BACKEND_PATH/manage.py collectstatic
#migrate
python3 $PROJECT_BACKEND_PATH/manage.py migrate

# load data RDS일 경우 조금 거시기해짐...
mkdir -p $PROJECT_BACKEND_PATH/media/master_img
cp $PROJECT_BACKEND_PATH/_Master_data/master_img $PROJECT_BACKEND_PATH/media/master_img
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Food-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Cooking-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Foods.json


# npm 설치
cd $PROJECT_NAME/frontend

# node update
sudo apt-get install -y nodejs
set NODE_OPTIONS=--max_old_space_size=4096
sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -


# npm install
# npm update
# sudo rm -rf node_modules
# sudo rm -f package-lock.json
# sudo npm cache verify
# export NODE_OPTIONS=--max_old_space_size=800
# sudo npm i

# 구니콘 설정 이동
cd ..
sudo cp $PROJECT_PATH/web/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# 구니콘 실행
sudo mkdir /logs
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start gunicorn

# robots.txt sitemap.xml
sudo cp $PROJECT_PATH/web/robots.txt /etc/nginx/sites-available/
sudo cp $PROJECT_PATH/web/sitemap.xml /etc/nginx/sites-available/

# nginx 설정 이동
sudo cp $PROJECT_PATH/web/nginx.conf /etc/nginx/sites-available/

# nginx 링크
sudo ln /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

# nginx 실행
sudo service nginx restart
