######Dev:- Joel Dcosta######################################
######Telegram:- https://t.me/pysnake
######FB Group:- https://www.facebook.com/groups/pythonsnake/
######FB Page:- https://www.facebook.com/PythonProgrammers/
#############################################################

import os
import sys

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
# For Python 2.7+ to 3.4+ users use python 
# For python 3.7+ users use python3 

# I am using python3.7+
pip_install = "python3 -m pip install "
#pip_install = "python -m pip install " #For python2+

install_input = input("What Module you want to install?:- ")

print(pip_install + install_input)
os.system(pip_install+install_input)
print("Done")
restart_program()
