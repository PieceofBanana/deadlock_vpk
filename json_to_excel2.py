import json
import pandas

import re
import shlex
import os
import glob



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

npc_keys=[]

weaponinfo_keys =[
"m_Spread",
"m_flRecoilSpeed",
"m_flZoomFOV",
"m_flDamageFalloffStartRange",
"m_flDamageFalloffEndRange",
"m_flRange",
"m_flBulletLifetime",

"m_iBullets",
"m_flCycleTime",
"m_reloadDuration",
"m_iClipSize",
"m_iBurstShotCount",
"m_flBurstShotCooldown",
"m_flBulletGravityScale",
"m_flBulletRadius",
"m_flBulletDrag",

"m_flCritBonusStart",
"m_flCritBonusEnd",
"m_flCritBonusStartRange",
"m_flCritBonusEndRange",
"m_flCritBonusAgainstNPCs",

"m_flReloadMoveSpeed",

"m_flBulletDamage",
]
usefull_keys=[
"m_nMaxHealth",
"m_flSightRangePlayers",
"m_flSightRangeNPCs",
"m_hFootstepSounds",
"m_flNearDeathDuration",
"m_flWalkSpeed",
"m_flRunSpeed",
"m_flAcceleration",
"m_flMeleeDamage",
"m_flMeleeAttemptRange",
"m_flMeleeHitRange",
"m_flMeleeDuration",
"m_flAttackT1BossMaxRange",
"m_flAttackTrooperMaxRange",
"m_flMeleeChargeRange",
"m_flBarrackGuardianDamageResistPct",
"m_flT1BossDPS",
"m_flT2BossDPS",
"m_flT3BossDPS",
"m_flGeneratorBossDPS",
"m_flBarrackBossDPS",
"m_flPlayerDPS",
"m_flTrooperDPS",
]

skip_keys=[
"m_WeaponInfo",
"m_sModelName",
"m_hFootstepSounds",
"m_flNearDeathDuration",
"m_BossAttackParticle",
"m_sDefaultMaterialGroupName",
"m_sEnemyMaterialGroupName",
"m_flHealthBarOffset",
"m_flHealthBarOffsetDucking",
"m_DeathParticle",
"m_DeathSound",
"m_MeleeHitSound",
"m_MeleeHitPlayerSound",
"m_HealthBarParticle",
"m_sHealthBarAttachment",
"m_HealthBarColorFriend",
"m_HealthBarColorEnemy",
"m_HealthBarColorTeam1",
"m_HealthBarColorTeam2",
"m_HealthBarColorTeamNeutral",
"m_MeleeSwingParticle",
"m_MeleeActivateParticle",
"m_MeleeAnimName",
"m_LastHitParticle",
"m_strLastHitSound",
"m_bPlayLastHitSound",
"m_NearDeathModifier",
"m_TargetingLaserParticle",
"m_TargetingEyeFlashParticle",
"m_sCelebrationSound",

"m_sTeam1MaterialGroupName",
"m_sTeam2MaterialGroupName",
]
    

hero_keys=[]


hero_collums=[]

path = 'D:/git/deadlock_backup/json/npc_units/'
for filename in glob.glob(os.path.join(path, '*.json')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        
        try:
            data =json.load(f) #получем стандартный python словар
            #print("Норм в ",f.name)
            for key in data.keys(): #Вход в основной словарь
                
                #print(data.get(key).get("m_mapAbilityProperties").get("AbilityCooldown").get("m_strValue"))
                if str(key)!=0:
                    hero_keys.append(key)
                    starting_stats_data.append([])
                    
                    if(len(starting_stats_keys)>0):starting_stats_data[hero_keys.index(key)] = [None]*len(starting_stats_keys)

                    #print(key)
                    for value in data[key].keys():
                        if (str(value).strip() in usefull_keys):
                        #print(hero_keys.index(key))
                            value = str(value).strip()
                            if not (value in starting_stats_keys):                         
                                starting_stats_keys.append(value)
                                #print(data[key]["m_mapStartingStats"][value])
                                starting_stats_data[hero_keys.index(key)].append(data[key][value])
                            else:
                            #print(hero_keys.index(key))
                            #print(starting_stats_keys.index(value))
                            #print(value)
                                starting_stats_data[hero_keys.index(key)][starting_stats_keys.index(value)]=data[key][value]
                        elif (value=="m_WeaponInfo"):
                            #print(data[key][value].keys())
                            for weapon_stat in data[key][value].keys():
                                if (weapon_stat in weaponinfo_keys):
                                    
                                    weapon_stat = str(weapon_stat).strip()
                                    if not(weapon_stat in starting_stats_keys):     
                                        print(weapon_stat)                    
                                        starting_stats_keys.append(weapon_stat)
                                        #print(data[key]["m_mapStartingStats"][value])
                                        starting_stats_data[hero_keys.index(key)].append(data[key][value][weapon_stat])
                                    else:
                            #print(hero_keys.index(key))
                            #print(starting_stats_keys.index(value))
                            #print(value)
                                        starting_stats_data[hero_keys.index(key)][starting_stats_keys.index(weapon_stat)]=data[key][value][weapon_stat]
                        else:
                            print("Не вошло",value)


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
excel_name = "D:/git/deadlock_backup/excel/npc_units.xlsx"
df = pandas.DataFrame(data=starting_stats_data,index=hero_keys,columns=starting_stats_keys)

df.to_excel(excel_name)



#print(starting_stats_data)
