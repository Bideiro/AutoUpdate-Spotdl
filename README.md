# A Simple Python Spotfy Auto Playlist Downloader Via SpotDl

## Description:
    This is just a simple python script for downloading your favorite playlists offline. I did this out of a whim so features are kinda limited. This uses the python package named spotdl, it simply just reads your spotify song/playlist then uses youtube as its source for the downloads. More information about its usage and installation is found in its documentation and github repository.

## spotdl repository and documentation:
    -https://github.com/spotDL/spotify-downloader
    -https://spotdl.readthedocs.io/en/latest/

## Features:
    -Detects if spotdl is installed, downloads it if not.
    -Reads a .txt for lists of playlists and its name
    -Creates folders for each playlists, and its own spotdl file.
    -Run again to update playlists songs.

## Usage:
    -Create a text file within the same folder of the file, name it as 'playlists.txt'
    -Format the name of your playlist and its spotify URL, like shown below. The playlists name will be used for the folder name and the spotdl save file.
        A Playlist, https://open.spotify.com/playlist/abc
    -Run the file.