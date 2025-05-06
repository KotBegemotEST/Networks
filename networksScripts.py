# import os
# import time

# hosts = ["8.8.8.7", "1.1.1.1", "192.168.1.1"]

# while True:
#     print("Проверка доступности:")
#     for host in hosts:
#         response = os.system(f"ping -n 1 {host} > nul")  # Windows; на Linux — ping -c 1
#         if response == 0:
#             print(f"{host} доступен ✅")
#         else:
#             print(f"{host} недоступен ❌")
#     print("-" * 30)
#     time.sleep(10)


import os
import time
import datetime
import csv

host = "8.8.8.8"
logfile = "ping_log.csv"

if not os.path.exists(logfile):
    with open(logfile, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Status"])

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = os.system(f"ping -n 1 {host} > nul")
    status = "OK" if result == 0 else "FAIL"

    print(f"{now} - {host} - {status}")

    with open(logfile, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, status])

    time.sleep(10)



import csv
import matplotlib.pyplot as plt
from datetime import datetime

times = []
statuses = []

with open("ping_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        times.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
        statuses.append(1 if row[1] == "OK" else 0)

plt.plot(times, statuses, marker="o")
plt.ylim(-0.1, 1.1)
plt.yticks([0, 1], ["FAIL", "OK"])
plt.xlabel("Time")
plt.ylabel("Status")
plt.title("Server Availability Over Time")
plt.grid(True)
plt.show()

# import os

# base_ip = "192.168.1."  # Измени под свою сеть

# for i in range(1, 255):
#     ip = base_ip + str(i)
#     response = os.system(f"ping -n 1 {ip} > nul")  # на Linux - ping -c 1
#     if response == 0:
#         print(f"{ip} доступен ✅")
#     else:
#         print(f"{ip} недоступен ❌")
import socket

ip = "192.168.1.1"  # Замени на нужный IP
ports = [22, 23, 80, 443, 3389]  # Список портов

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Порт {port} открыт ✅")
        else:
            print(f"Порт {port} закрыт ❌")
