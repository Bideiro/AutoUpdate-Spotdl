# A Simple Python Spotfy Auto Playlist Downloader Via SpotDl

## Description:

This is just a simple python script for downloading your favorite playlists offline. I did this out of a whim so features are kinda limited. This uses the python package named spotdl, it simply just reads your spotify song/playlist then uses youtube as its source for the downloads. More information about its usage and installation is found in its documentation and github repository.

## SpotDL repository and documentation:
[SpotDL Github Repository](https://github.com/spotDL/spotify-downloader) <br>
[SpotDL Documentation](https://spotdl.readthedocs.io/en/latest/)

## Features:
-Detects if spotdl is installed, downloads it if not.<br>
-Reads a .txt for lists of playlists and its name<br>
-Creates folders for each playlists, and its own spotdl file.<br>
-Run again to update playlists songs.<br>

## Usage:
- Create a text file within the same folder of the file, name it as 'playlists.txt'<br>
- Format the name of your playlist and its spotify URL, like shown below. The playlists name will be used for the folder name and the spotdl save file.<br>
    A Playlist, https://open.spotify.com/playlist/abc<br>
- Run the file.<br>

>[!CAUTION]
> At the current time this doesnt have error handling for incorrect format in .txt file
