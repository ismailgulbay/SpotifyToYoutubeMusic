import csv
import requests
from ytmusicapi import YTMusic
import time

ytmusic = YTMusic(r"\oauth.json")

def connectToSpotify():

    #add here playlistId from Spotify
    spotify_playlistId = "playlistId" 

    #add here token. You can get from Spotify Dashboard.
    token = "token"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    offset = 0
    loop_count  = 0
    open("output.csv", "w", newline="", encoding="utf-8")

    while True:
        url = f'https://api.spotify.com/v1/playlists/{spotify_playlistId}/tracks?offset={offset}&limit=100'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return False

        total = addtoCSV(response)
        if total == 0:
            return False
        offset += 100

        loop_count += 1
        if loop_count >= total // 100 + 1:
            return True



def addtoCSV(response):
        if response.status_code == 200:
            data = response.json()
            total = data.get("total", "")
            with open("output.csv", "a", newline="", encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile)

                for item in data.get("items", []):
                    track = item.get("track", {})
                    if(track is None):
                        continue
                    track_name = track.get("name", "")

                    artist = track.get("artists", [{}])[0]
                    if(artist is None):
                        continue
                    artist_name = artist.get("name", "")

                    csv_writer.writerow([track_name, artist_name])
            print("The data has been successfully added to the CSV file.")
            return total
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return 0



def findAndInsertSongtoPlaylist(playlistId, dataList):
    videoIdList = []
    for index, song in enumerate(dataList):
        searchSong = ytmusic.search(song, filter="songs")
        if searchSong:
            videoIdList.append(searchSong[0].get("videoId"))
            print(f'{searchSong[0].get("title")} added to videoIdList')
            status = ytmusic.add_playlist_items(playlistId, videoIdList)
            print(status["status"])
            videoIdList.clear()
            time.sleep(0.5)




def getSongListFromCSV():
    with open("output.csv", "r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        data_list = [' '.join(row) for row in csv_reader]
        return data_list


if __name__ == "__main__":
    isSuccessful = connectToSpotify()
    if(isSuccessful):
        dataList = getSongListFromCSV()

        #add here playlistId from Youtube Music
        youtube_playlistId = "playlistId"

        findAndInsertSongtoPlaylist(youtube_playlistId, dataList)



