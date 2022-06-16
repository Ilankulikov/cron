#! /bin/bash

sudo apt update
sudo apt install awscli -y
sudo apt install python3-pip -y
sudo apt install python3.10-venv -y
sudo sudo python3 -m venv cronjob_project 
sudo chown -R $USER /home/ubuntu/cron/cronjob_project/
source /home/ubuntu/cron/cronjob_project/bin/activate
pip install -r dependencies.txt
git clone $WEB_REPO_PATH ~/web
