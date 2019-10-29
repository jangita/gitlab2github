import gitlab import Gitlab
from github import Github
import datetime

# Function to log messages, for now it just prints. You can add file logging etc
def log(msg):
    print(datetime.datetime.now().isoformat + ' ' + str(msg))

