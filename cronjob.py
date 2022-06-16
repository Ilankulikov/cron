
from datetime import datetime as dt
import git
import subprocess

repo_path = '/home/ubuntu/web'
bucket = 's3://web-test-ilan'
file_path = '/home/ubuntu/cron/'
file_name = "commit.txt"
url = 'https://github.com/Ilankulikov/web.git'
date = "[" + dt.now().strftime("%Y-%m-%d %H:%M:%S") + "]: "
repo = git.Repo(repo_path)
sha = git.cmd.Git().ls_remote(url, heads=True).split('\t',1)[0]

try:
    f = open(file_path + file_name, 'r+')
    current_commit = f.read()
    print('Current commit: ', current_commit )
    if current_commit == sha:
        print(date, "Repository is up to date.")
    else:
        print(date, "Repository has changed.")
        repo.remotes.origin.pull('main')
        repo.remotes.origin.pull('main')
        print(date, "Removing old files...")
        subprocess.run(['aws', 's3', 'ls', repo_path, bucket, '--recursive','--quiet' '--exclude', 'README.md', '.git/*'])
        print(date, "Uploading new files...")
        subprocess.run(['aws', 's3', 'cp', repo_path, bucket, '--recursive', '--quiet'])
        open(file_path + file_name,"w").close()
        f.write(sha)

except:
    print("File not found, creating file.")
    f = open(file_path + file_name, 'w+')
    f.write(sha)
