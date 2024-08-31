decompiler.exe -i "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\pak01_dir.vpk" --output "pak01" --vpk_filepath "scripts" -d
robocopy "D:\Steam_client\steamapps\common\Project8Staging\game\citadel\resource\localization\." ".\localization" /e
robocopy "D:\Steam_client\steamapps\common\Project8Staging\game\citadel" ".\ver" steam.inf