from gitlab import Gitlab
from github import Github
import datetime

import conf

# Function to log messages, for now it just prints. You can add file logging etc
def log(msg):
    print(datetime.datetime.now().isoformat() + ' ' + str(msg))

log('Script start')

gl = Gitlab(conf.GITLAB_URL, http_username=conf.GITLAB_USER, http_password=conf.GITLAB_PASSWORD)
gl.auth()
for project in gl.projects:
    log(project.ssh_url_to_repo)