== A.
>>> print("\n" * 100)

== B.
import os
os.system('cls||clear')

== C.
import subprocess, platform

if platform.system()=="Windows":
    if platform.release() in {"10", "11"}:
        subprocess.run("", shell=True) #Needed to fix a bug regarding Windows 10; not sure about Windows 11
        print("\033c", end="")
    else:
        subprocess.run(["cls"])
else: #Linux and Mac
    print("\033c", end="")

(按 Enter 兩次)

== D.
import sys
sys.stderr.write("\x1b[2J\x1b[H")
