# IP address logging script
 
I was interested to track the IP address leased to me by my ISP in order to understand how frequently this was changed, if at all.

I plan to expand this project at some point, so that if my IP changes this script will update the IP address in my domain's DNS records - allowing my domain to resolve to the correct and current IP, behind which my public facing services can be found.

## Configure to run on a Windows host

The script will need to be configured to run on a schedule, in order to log the system's public and internal IP addresses periodically. This can be achieved as follows:
1. Open Task Scheduler
2. Click Create Task
3. Enter a name for the task, and a description if you want
4. It's fine to leave the defaults for the rest of the General tab
5. Click on the Triggers tab
6. Click New
7. From the Begin the task drop down, select On a schedule
8. Select the One time radio button
9. Under advanced settings, check the Repeat task every box and select the frequency you would like - I chose 1 hour
10. Check the Enabled box
11. Click OK
12. Under the Actions tab, click New
13. From the Action drop down, select Start a program
14. Enter the path to the location of the python executable on your machine, for me this was: "C:\Program Files (x86)\Python38-32\python.exe"  (the quotes are included in the text box )
15. In the Add arguments field, enter the following: public_ip_logger.py
16. In the Start in field, enter the path to the directory you are storing this app on your machine, for me this was: C:\Users\Ben\Desktop\python_projects\public_ip_logger
17. Click OK
18. Click OK again, and that should be the task scheduled

## Configure to run on a Linux host

The script can be configured to run on a schedule on a linux host by creating a new cron job

1. 