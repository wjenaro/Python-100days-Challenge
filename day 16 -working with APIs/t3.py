import requests

url = "https://youtube-music-api-detailed.p.rapidapi.com/get_watch_playlist"

querystring = {"video_id":"1A7Qw88As64"}

headers = {
	"X-RapidAPI-Key": "8972ea1c9bmsh6192d8c1e2219c6p12caf8jsnea3979fdb5a9",
	"X-RapidAPI-Host": "youtube-music-api-detailed.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())