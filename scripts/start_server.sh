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
python3 $PROJECT_BACKEND_PATH/manage.py migrate

# load data RDS일 경우 조금 거시기해짐...
mkdir -p $PROJECT_BACKEND_PATH/media/master_img
cp $PROJECT_BACKEND_PATH/_Master_data/master_img $PROJECT_BACKEND_PATH/media/master_img
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Food-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Cooking-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_Master_data/Foods.json


# npm 설치
sudo apt-get update
cd $PROJECT_NAME/frontend

# node update
set NODE_OPTIONS=--max_old_space_size=4096

sudo dd if=/dev/zero of=/swapfile bs=128M count=16
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -

# npm install
sudo npm i

# npm build
sudo chown -R $USER:$USER /home/ubuntu/Simple-Diet-Manager/frontend/node_modules
# sudo npm run build


# 구니콘 설정 이동
cd ..
sudo cp $PROJECT_PATH/web/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# 구니콘 실행
sudo mkdir /logs
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart gunicorn

# robots.txt sitemap.xml
sudo cp $PROJECT_PATH/web/robots.txt /etc/nginx/sites-available/robots.txt
sudo cp $PROJECT_PATH/web/sitemap.xml /etc/nginx/sites-available/sitemap.xml

# nginx 설정 이동
sudo cp $PROJECT_PATH/web/nginx.conf /etc/nginx/sites-available/nginx.conf

# nginx 링크
sudo ln /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

# nginx 실행
sudo service nginx restart
