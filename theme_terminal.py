#import
import os

#color
white="\033[00;37m"
blue="\033[01;34m"
blue1="\033[02;34m"
#intro
print(f'''
            {white}      .o.       ooooo          ooooooooo
            {white}     .888.      `888'         d"""""""8'
{blue1}oooo    ooo{white}     .8"888.      888               .8'{blue1}  oooo    ooo
{blue1} `88b..8P' {white}    .8' `888.     888              .8' {blue1}   `88b..8P'
{blue1}   Y888'   {white}   .88ooo8888.    888             .8'  {blue1}     Y888'
{blue1} .o8"'88b  {white}  .8'     `888.   888       o    .8'   {blue1}   .o8"'88b
{blue1}o88'   888o{white} o88o     o8888o o888ooooood8   .8'    {blue1}  o88'   888o{blue}
''')
#_____
#_____
#opt

print(f"""{white}
                            ______________________________________
                           |                                      |
                           |       Twitter:alhassanAlharb7        |
                           |               ©{blue}xAL7x{white}                 |
                           |______________________________________|
{blue}kali Linux Theme [{white}1{blue}]
ubuntu Theme [{white}2{blue}]
Parrot os Theme [{white}3{blue}]
Arch Theme [{white}4{blue}]
---------------------------""")
theme=input(f"Theme >> {white}")



#_______________
while True:
    if theme=="1":
        command=input("""\033[0;32m┌──(\033[01;34mxAL7x@Kali\033[0;32m)-[\033[0;40m~\033[0;32m]
└─\033[01;34m$ \033[0;40m""")
        for commands in os.popen(command):
                    print(commands)
    elif theme=="2":
        command=input("""\033[0;32mxAL7x@ubuntu\033[0;37m:\033[0;34m~\033[0;37m$ """)
        for commands in os.popen(command):
                    print(commands)
    elif theme=="3":
        command=input("""\033[00;31m┌──[\033[00;32mxAL7x\033[01;33m@\033[01;36mParrot\033[00;31m]-[\033[02;32m~\033[00;31m] \n\033[00;31m└─$\033[00;38m """)
        for commands in os.popen(command):
                    print(commands)
    elif theme=="4":
        command=input("""\033[00;32m[xAL7x@archlinux ~]$\033[00;37m """)
        for commands in os.popen(command):
                    print(commands)