# pip 설치
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install python3
sudo apt-get install -y python3-pip


sudo pip install pip --upgrade
sudo pip install pyopenssl --upgrade

# node 설치
sudo apt-get install -y nodejs

# 구니콘 설치
sudo pip3 install gunicorn django
sudo apt-get install supervisor

# nginx 설치
sudo apt-get install nginx