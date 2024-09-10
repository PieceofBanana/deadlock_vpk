decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "scripts" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "animgraphs" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "cfg" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "panorama" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "resource" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "smartprops" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "smart_props" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "soundevents" -d
decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "soundstacks" -d
robocopy "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\resource\localization\." ".\localization" "*english.txt" /e
robocopy "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\resource\localization\." ".\localization" "*russian.txt" /e
robocopy "D:\Steam_client\steamapps\common\Project8Staging\game\citadel" ".\ver" steam.inf
call test.bat
set /p clientver=< .\ver\steam.inf
git commit -a -m %clientver%
git push origin
ping -n 11 127.0.0.1 > nul