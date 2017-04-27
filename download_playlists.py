#
# Jack Morris 04/26/17
#

import config
import requests

api_url = "https://api.spotify.com/v1/"
max_limit = 50

def download(start_name, end_name):
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
  print "getting"
  #
  while True:
    #
    playlists = request_user_playlists(api_key, user_id, limit, offset)
    print playlists
    all_playlists.extend(playlists)
    offset += limit
    names = [playlist.name for playlist in playlists]
    found_start_playlist = (start_name in names) or found_start_playlist
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
  endpoint = 'users/' + str(user_id) + '/playlists?limit=' + str(limit) + '&offset=' + str(offset)
  #
  return api_request(api_key, endpoint)
  #

def api_request(api_key, endpoint):
  #
  headers = {
    "Authorization": "Bearer " + api_key,
    "Accept": "application/json"
  }
  print "headers", headers
  url = api_url + endpoint
  r = requests.get(url, headers=headers)
  return r.json()  
  #
