import config
import requests

api_url = "https://api.spotify.com/v1/"
max_limit = 50

def download_playlists(start_name, end_name):
  #
  api_key = config.api_key
  user_id = config.user_id
  #
  limit = max_limit
  offset = 0
  #
  found_start_playlist = False
  #
  all_playlists = []
  #
  while True:
    #
    playlists = request_user_playlists(api_key, user_id, limit, offset)
    all_playlists.extend(playlists)
    offset += limit
    names = [playlist.name for playlist in playlists]
    found_start_playlist = (start_name in names) || found_start_playlist
    #
    if found_start_playlist and end_name in names:
      #
      break
      #
    #
  #
  print all_playlists
  #

def request_user_playlists(api_key, user_id, limit, offset):
  #
  endpoint = 'users/' + user_id 
     + '/playlists?limit=' + limit
     + '&offset=' + offset
  #
  return api_request(api_key, endpoint)
  #

def api_request(api_key, endpoint):
  #
  headers = {
    "Authorization": "Bearer " + api_key
    "Accept": "application/json"
  }
  url = api_url + endpoint
  r = requests.get(url, headers=headers)
  return r.json()  
  #
