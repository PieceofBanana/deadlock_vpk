import json
import pandas

import re
import shlex
import os
import glob

path = 'D:/git/deadlock_backup/json/npc_units/'
with open(str(path+"trooper_normal.json"), 'r') as f:
            data =json.load(f) #получем стандартный python словар
            #print("Норм в ",f.name)
            for key in data.keys(): #Вход в основной словарь
                    for value in data[key]["m_WeaponInfo"].keys():
                        str="\""+value+"\","
                        print(str)
