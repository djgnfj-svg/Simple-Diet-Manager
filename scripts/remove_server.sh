#!/bin/bash
PROJECT_NAME="Simple-Diet-Manager"
DEPLOY_PATH=/home/ubuntu

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME

# 구니콘 루트
GUNICORN_FILE="/etc/supervisor/conf.d/gunicorn.conf"
# nginx 루트
NGINX_DJANGO_FILE="/etc/nginx/sites-available/nginx.conf"
NGINX_DJANGO_FILE_ENABLE="/etc/nginx/sites-enabled/nginx.conf"

SERVICE_GUNICONR=$(pgrep gunicorn)
SERVICE_NIGNX=$(pgrep nginx)

# 구니콘 파일 제거
if [ -e $GUNICORN_FILE ]; then
    rm -rf $GUNICORN_FILE
    rm -rf /logs
fi

# nginx 파일 제거
if [ -e $NGINX_DJANGO_FILE ]; then
    rm -rf $NGINX_DJANGO_FILE
fi
if [ -e $NGINX_REACT_FILE ] ; then
    rm -rf $NGINX_REACT_FILE
fi

if [ -e $NGINX_DJANGO_FILE_ENABLE ]; then
    rm -rf $NGINX_DJANGO_FILE_ENABLE
fi

# 프로젝트 파일삭제
sudo rm -rf $PROJECT_PATH

# 서비스 중지
sudo supervisorctl stop gunicorn

if [ -z "$SERVICE_NIGNX" ]; then
    sudo service nginx stop
fi

sudo apt-get clean
sudo apt autoremove
sudo apt autoremove --purge
sudo apt autoremove --purge snapd
sudo npm cache clean -f