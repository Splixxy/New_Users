#imports contab package
from crontab import CronTab
#creates the cron job of Users.py script to run every hour
cron = CronTab(user="root")
Usersjob = cron.new(command="python3 Users.py")
Usersjob.hour.every(1)
cron.write()
