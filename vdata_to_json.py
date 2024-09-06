import json
import re
import shlex
import os
import glob
import sys

def is_member(arr,str):
    for char in arr:
        if (char in str):
            return True
    return False
def parse_custom_dict(file_path):
    global num
    lastline=""
    abilities={}
    with open(file_path, 'r') as file:
        
        tokens = []

        brackets=None
        i=1
        for line in file:
            i=i+1
            #print(line)
            
            #print(line)
            if "<" in line and ">" in line:
                #print("test")
                #print(line)
                continue

            if line.count("\"")%2!=0:
                #print(line)
                continue
           # elif brackets==0:
           #     continue
            else:
                lastline=lastline.strip()+line.strip()
                line=lastline
                lastline=""
            



            if brackets==None and line.count("{")>0:
                brackets=0
                continue
            if brackets!= None:brackets=brackets+line.count("{")
            if brackets!= None:brackets=brackets-line.count("}")
            #if  brackets==0:print("пустые скобки",line,"    ",lastline)
            #if brackets==0:print("i=",i," ",line)


            #pattern = re.compile(r"/s|(=)")
            #line = re.split(pattern,line.strip())
            line = shlex.split(line, posix=False)
            i=-1
            while i < len(line):
                i=i+1
                if(i==len(line)): continue
                
                #print("i ",i," len",len(line))
                #print("токен",line[i])
                if line[i] != "" and line[i] != None:
                    if("," in line[i] and "}" in line): line[i] = line[i].replace(",","")
                    if("," in line[i] and line[i]!=","):
                        #print(line[i])
                        line[i] = line[i].replace(",","")                        
                        line.insert(i+1,",")
                        #print("new",line[i+1])
                        

                    if(line[i]=="," and tokens[-1]==","):
                        continue
                        
                    if line[i].strip() == "": continue
                    if len(tokens)>1:
                        
                        
                        if (tokens[-2]==":" and not (tokens[-1]=="{" or tokens[-1]=="[")):
                            #print(tokens[i-1], " ,"," ",line[i])
                            tokens.append(",")
                        if(is_member(['}','}'],tokens[-1])):
                            if(not is_member(['}','}'],line[i])):
                                tokens.append(",")

                    if((line[i]=="}" or line[i]=="]")):
                        #print(tokens[i-1], "запятая"," ",line[i])
                        if(len(tokens)==0):
                            #tokens.append(line[i])
                            #tokens.append(",")
                            continue
                        if tokens[-1]==",":
                           #print("pop ",i,"  ", tokens[-2])
                           tokens.pop(-1)                           

                        #print(tokens[i-1], " ,"," ",line[i])
                        tokens.append(line[i])
                        tokens.append(",")
                        continue

                        
                               

                    if (line[i]=="="):
                        tokens.append(":")
                        continue     
                    if not ( is_member(["[","]","{","}",":",","],line[i])):
                        if(line[i].count("\"")==0):
                            #print(line[i])                            
                            tokens.append("\""+line[i]+"\"")
                            continue
                    if(":" in line[i]):
                        if(line[i].find("\"")==0):
                            temp = line[i]
                        else:
                            temp = line[i].split(":",maxsplit=1)[-1]

                        if temp!="":tokens.append(temp)
                        continue
                    tokens.append(line[i])

            
            if brackets==0 and tokens.count("{")>0: #ВОТ ЭТОТ КАУНТ ЭТО ВООБЩЕ НЕОПТИМИЗИРОВАННЫЙ КАЛ   
                num=0       
                #abilities=find_value(tokens)
                #print("ВХОД")
                #json_object = json.dumps(abilities,sort_keys=True,indent=4)
                name = tokens[0]
                if(tokens[-1]==","):tokens.pop(-1)
                #print(name)
                
                name=re.sub('[^a-z0-1_.]', '', name)


                json_str="{"
                for token in tokens:
                    json_str=json_str+' '+str(token)
                json_str=json_str+'}'
                output=json.loads(json_str)
                
                output_path = sys.argv[2]+name+".json"
                #output_path = "D:/git/deadlock_backup/json/"+name+".json"
                os.makedirs(os.path.dirname(output_path),exist_ok=True)
                with open(output_path, "w") as outfile:
                    json.dump(output,outfile,indent=4)

                #    outfile.write("{")
                #    for row in tokens:
                #        outfile.write(str(row) + ' ')
                #    outfile.write("}")                    
                
                outfile.close()
                abilities={}
                tokens=[]
                         
        return abilities

input_path = sys.argv[1]
#input_path = "D:/git/deadlock_backup/pak01/scripts/abilities.vdata"
print("вход",sys.argv[1])
print("выход",sys.argv[2])
#wait = input("Press Enter to continue...")
arr = parse_custom_dict(input_path)



       







