import requests
import time
import socket

#Inform user script has started to run
print("IP logger script written by Ben Webster.")

#Get current system time in seconds since epoch
epoch_time = int(time.time())

#Get current system hostname
hostname = socket.gethostname()

#Get current system local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    local_ip = s.getsockname()[0]
except:
    local_ip = '127.0.0.1'
finally:
    s.close()

#Get public IP from icanhazip
response = requests.get('https://icanhazip.com/')
ip = response.text

#Format string to append to log file
delimiter = ", "
log_line = "system_time=" + str(epoch_time) + delimiter + "hostname=" + str(hostname) + delimiter + "local_ip=" + str(local_ip) + delimiter + "public_ip=" + str(ip)
print("Log line to be appended:")
print(log_line)

#Append string to log file
log_file = open("ip_log.txt", "a")
log_file.write(log_line)
log_file.close()

print("Log line written.")

#Pause to allow user to read message / if troubleshooting
#time.sleep(5)