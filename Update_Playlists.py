import os 
import subprocess
# Checking if spotdl is installed
print('Checking required package - SpotDL...')
try:
    result = subprocess.run(
        ["spotdl", "--version"],
        capture_output=True, 
        text=True,
        check=True            
    )
    print(f"spotdl is installed! Version: {result.stdout.strip() }")
except Exception as e:
    print('Spotdl not found. Proceding to install...')
    choice = input('Will install Spotdl via pip. \'pip install spotdl \' will run, allow? (y/n): ')

    # Attempt Install if user agrees

    if choice.lower() == 'y':
        try:
            subprocess.run(
                ["pip", "install", "spotdl"],
                check=True
            )
            print('Spotdl installed successfully.')
        except Exception as install_error:
            print(f'Failed to install Spotdl. Error: {install_error}')
            exit()
    else:
        print('Installation aborted by user. Exiting...')
        exit()

print('Spotdl is installed. Proceeding with playlist update...')

def Update_playlist(Folder_name, Playlist_URL):
    save_file = Folder_name.replace(' ','_') + ".spotdl"
    os.makedirs(Folder_name, exist_ok=True)
    os.chdir(Folder_name)

    print(f'Updating {Folder_name} playlist...')

    if os.path.exists(save_file):

        process = subprocess.run(["spotdl", "sync", save_file])
    
    else:

        process = subprocess.Popen(["spotdl", "sync", Playlist_URL, "--save-file", save_file])

    os.chdir('..')

Update_playlist('Change Of Taste V.2','https://open.spotify.com/playlist/56eMQJ01rzM1tKJQaDV0VM?si=95f3d18f984846b4')
Update_playlist('Change Of Taste','https://open.spotify.com/playlist/4nVqac5pCLTWjsW8AAikTD?si=7b7c917202bf447c')
Update_playlist('R & B','https://open.spotify.com/playlist/2quUTcXBBlGMpTI3FlzrAO?si=ddfa808a6f604d84')
Update_playlist('Commute','https://open.spotify.com/playlist/4ikPF2A0q5FkygV6gSKYMk?si=c786093e17cf4aab')
Update_playlist('S K R','https://open.spotify.com/playlist/6ADpuoiA84UHuhwBlPLBTF?si=7b98d2fe46bb4487')
Update_playlist('Ultra Chill','https://open.spotify.com/playlist/6bDYzWmv6BQhWBmOoeRr3U?si=41d70b79b5804412')
Update_playlist('P O P','https://open.spotify.com/playlist/1PcW7mLeXjAZWiXZpwThGI?si=ae4937a766bc402a')
Update_playlist('Eurobeat','https://open.spotify.com/playlist/4fOmmSRTleYJ75RVQ0lVSG?si=4c59082aa91b490c')
Update_playlist('O P M','https://open.spotify.com/playlist/4eEWB7N3UrDlhF5tBWzoRr?si=f42bcd5f074f4c3c')