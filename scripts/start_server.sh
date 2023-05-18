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
# 가상환경만들기
cd $PROJECT_BACKEND_PATH
python3 -m venv myvenv
source myvenv/bin/activate
# pip 설치
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install python3
sudo apt-get install -y python3-pip
pip install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py migrate
mkdir media
cp -r $PROJECT_BACKEND_PATH/_Master_data/master_image/ $PROJECT_BACKEND_PATH/media/

# npm 설치
cd ..
cd $PROJECT_NAME/frontend
sudo apt-get install -y nodejs
set NODE_OPTIONS=--max_old_space_size=4096
sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -


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
