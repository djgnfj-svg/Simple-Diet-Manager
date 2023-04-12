# pip 등 설치(codedeploy도)
sudo yum update -y
sudo yum install git -y
sudo yum install python3-pip python3-devel python3-setuptools -y

sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install python3
sudo apt-get install -y python3-pip

# node 설치
sudo apt-get install -y nodejs

# 구니콘 설치
sudo pip3 install gunicorn django
sudo apt-get install supervisor

# nginx 설치
sudo apt-get install nginx