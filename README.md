__Im assuming that in the first place there are files in S3__

**run the following command on the vm.**

    git clone https://github.com/Ilankulikov/cron.git
    
set environment variabl with the web repo url or se it manually in install_dependencies.sh

    export WEB_REPO_PATH=<web repository url> # or set it manually
 
run the script to install all dependencies
 
    cd cron && chmod +x cronjob.py install_dependencies.sh
  
    ./install_dependencies.sh
    
set aws configure 

    aws configure
  
==============================================================
  
## in cronjob.py
  
make sure that repo_path,bucket,file_path,url vlues are correct.

repo_path,file_path - only the USER should be modified if needed

##

run 'crontab -e' and add the following line to the end of file:

    */1 * * * *  /home/ubuntu/cron/cronjob_project/bin/python /home/ubuntu/cron/cronjob.py 2>&1
    
this command will check for new commits every 1 minutes.
