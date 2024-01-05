import datetime
import sys


print(dir(sys))
print(dir(datetime))

try :
    7 / 0
except Exception as e:
    sys.stdout = open("error_log.txt", "w")
    now = datetime.datetime.now()
    print(f"{str(now).split(".")[0]} - ERROR - {now} An error occurred: {e}")
    sys.stdout.close()



