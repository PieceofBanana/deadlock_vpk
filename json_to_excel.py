import json
import pandas

import re
import shlex
import os
import glob

path = 'D:\git\deadlock_backup\json\heroes'

upgrades_keys=[
    ["m_mapAbilityProperties","*","m_strValue"],
    "_multibase",
]
hero_usefull_keys=[
    ["m_mapStartingStats"],
    ["m_mapStandardLevelUpUpgrades"],
    ["m_mapScalingStats"],
]


#m_mapStartingStats
lvlup_upgrades_keys=[]
lvlup_upgrades_data=[]
#m_mapStandardLevelUpUpgrades
starting_stats_keys=[]
starting_stats_data=[]
#m_mapScalingStats
scaling_stats_keys=[]
scaling_stats_data=[]

hero_keys=[]


hero_collums=[]


for filename in glob.glob(os.path.join(path, '*.json')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        
        try:
            data =json.load(f) #получем стандартный python словар
            #print("Норм в ",f.name)
            for key in data.keys(): #Вход в основной словарь
                
                #print(data.get(key).get("m_mapAbilityProperties").get("AbilityCooldown").get("m_strValue"))
                if str(key).index("hero_")==0:
                    hero_keys.append(key)
                    starting_stats_data.append([])
                    lvlup_upgrades_data.append([])
                    scaling_stats_data.append([])
                    
                    if(len(starting_stats_keys)>0):starting_stats_data[hero_keys.index(key)] = [None]*len(starting_stats_keys)
                    if(len(lvlup_upgrades_keys)>0):lvlup_upgrades_data[hero_keys.index(key)] = [None]*len(lvlup_upgrades_keys)
                    if(len(scaling_stats_keys)>0):scaling_stats_data[hero_keys.index(key)] = [None]*len(scaling_stats_keys)
                    print(key)
                    for value in data[key]["m_mapStartingStats"].keys():
                        #print(hero_keys.index(key))
                        value = str(value).strip()
                        if not (value in starting_stats_keys):                         
                            starting_stats_keys.append(value)
                            #print(data[key]["m_mapStartingStats"][value])
                            starting_stats_data[hero_keys.index(key)].append(data[key]["m_mapStartingStats"][value])
                        else:
                            #print(hero_keys.index(key))
                            #print(starting_stats_keys.index(value))
                            #print(value)
                            starting_stats_data[hero_keys.index(key)][starting_stats_keys.index(value)]=data[key]["m_mapStartingStats"][value]

                    for value in data[key]["m_mapStandardLevelUpUpgrades"].keys():
                        #print(hero_keys.index(key))
                        value = str(value).strip()
                        if not (value in lvlup_upgrades_keys):                         
                            lvlup_upgrades_keys.append(value)
                            #print(data[key]["m_mapStartingStats"][value])
                            lvlup_upgrades_data[hero_keys.index(key)].append(data[key]["m_mapStandardLevelUpUpgrades"][value])
                        else:
                            #print(hero_keys.index(key))
                            #print(starting_stats_keys.index(value))
                            #print(value)
                            lvlup_upgrades_data[hero_keys.index(key)][lvlup_upgrades_keys.index(value)]=data[key]["m_mapStandardLevelUpUpgrades"][value]
                            
                    #m_mapScalingStats * flScale
                    for value in data[key]["m_mapScalingStats"].keys():
                        print(key)
                        value = str(value).strip()
                        #print(value)
                        if not (value in scaling_stats_keys):                         
                            scaling_stats_keys.append(value)
                            #print(str(data[key]["m_mapScalingStats"][value]))
                            #print(data[key]["m_mapStartingStats"][value])
                            scaling_stats_data[hero_keys.index(key)].append(data[key]["m_mapScalingStats"][value]["flScale"])
                            #print(value)
                        else:
                            #print(hero_keys.index(key))
                            #print(starting_stats_keys.index(value))
                            #print(value)
                            scaling_stats_data[hero_keys.index(key)][scaling_stats_keys.index(value)]=data[key]["m_mapScalingStats"][value]["flScale"]

#                    for value in data[key]["m_mapStandardLevelUpUpgrades"].keys():
#                        if not (str(value).strip() in lvlup_upgrades_keys):
#                            lvlup_upgrades_keys.append(str(value).strip())    
#                            print(value)               
#                        lvlup_upgrades_data[hero_keys.index(key)][lvlup_upgrades_keys.index(value)]=data[key]["m_mapStandardLevelUpUpgrades"][value]



                        #print(str(properties))
                        #print(str(key)," ",str(properties)," ",data[key]["m_mapAbilityProperties"][properties]["m_strValue"])
            

        except:
            print("fuck!")
            #print("Ошибка в ",print(f.name))

#levelup_upgrades_data =[["x"]*lvlup_upgrades_keys_count.count]*hero_count
#print(starting_stats_keys)
#for row in starting_stats_data:
#    print(row,sep="/n")
df = pandas.DataFrame(data=starting_stats_data,index=hero_keys,columns=starting_stats_keys)

excel_name = "D:/git/deadlock_backup/excel/heroes_starting_stats.xlsx"
df.to_excel(excel_name)

excel_name = "D:/git/deadlock_backup/excel/lvlup_upgrades_stats.xlsx"
df = pandas.DataFrame(data=lvlup_upgrades_data,index=hero_keys,columns=lvlup_upgrades_keys)
df.to_excel(excel_name)


excel_name = "D:/git/deadlock_backup/excel/scaling_stats.xlsx"
df = pandas.DataFrame(data=scaling_stats_data,index=hero_keys,columns=scaling_stats_keys)
df.to_excel(excel_name)

#print(starting_stats_data)
