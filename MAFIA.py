import os,platform
os.system('git pull')
MAFIA=platform.architecture()[0]
if MAFIA=="64bit":
     import Mafia
elif MAFIA=="32bit":
    print(' Your Device is not support this tool ...')
    exit()

