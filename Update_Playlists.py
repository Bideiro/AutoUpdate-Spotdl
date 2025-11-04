import os 
import subprocess

text_file = 'playlists.txt'

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
    choice = input('Will install Spotdl via pip. \'pip install spotdl\' will run, allow? (y/n): ')

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

print(f'Opening file named {text_file}')

with open(text_file, "r") as file:
    for line in file:
        parts = line.split(",")
        Update_playlist(parts[0].strip(),parts[1].strip())