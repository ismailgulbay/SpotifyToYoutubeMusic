# SpotifyToYoutubeMusic


Before running you must install ytmusicapi library this here --> https://ytmusicapi.readthedocs.io/en/stable/setup/index.html

And you can access Spotify Token from here --> https://developer.spotify.com/documentation/web-api/concepts/access-token


You can transfer playlists from Spotify to YoutubeMusic using this project. Before starting you have to create playlist on Youtube Music and you can get playlist Ids from Spotify and Youtube Music.


First of all, after connecting Spotify with the token, it creates an XML file and appends singer's names and song title. After that it connects to YouTube music. Then it tries to find the music by searching for the singer and song name in the XML file. After finding it, it adds it to the list.
