import os,platform
os.system('git pull')
os.system('rm -rf Mafia.so')
MAFIA=platform.architecture()[0]
if MAFIA=="64bit":
     if not os.path.isfile('Mafia.so'):
        os.system('curl -L https://github.com/Muzammil-404/MAFIA/blob/main/Mafia.cpython-311.so?raw=true -o Mafia.so') 
        import Mafia
     else:
        import Mafia 
elif MAFIA=="32bit":
    print(' Your Device didn't support this tool ...')
    exit()

