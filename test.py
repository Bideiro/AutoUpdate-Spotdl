with open("playlists.txt", "r") as file:
    for line in file:
        parts = line.split(",")
        print(parts[0].strip())