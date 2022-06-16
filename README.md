Im assuming that in the first place there are files in S3
git clone https://github.com/Ilankulikov/cron.git
export WEB_REPO_PATH=<web repository url> or set it manually
cd cron && chmod +x cronjob.py install_dependencies.sh
./install_dependencies.sh
aws configure -- > set aws credentials
==============================================================
in cronjob.py
make sure that repo_path,bucket,file_path,url vlues are correct.
==============================================================
repo_path,file_path - only the USER should be modified if needed
run 'crontab -e' and add the following line to the end of file:
*/1 * * * *  /home/ubuntu/cron/cronjob_project/bin/python /home/ubuntu/cron/cronjob.py 2>&1
this command will check for new commits every 5 minutes.
/home/ubuntu/cron/cronjob_project/bin/python /home/ubuntu/cron/cronjob.py