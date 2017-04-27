#
# Jack Morris 04/26/17
#

import config
import requests
import unicodedata

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
  in_folder = False
  #
  all_playlists = []
  print "getting"
  #
  while True:
    #
    playlist_search = request_user_playlists(api_key, user_id, limit, offset)
    playlists = playlist_search["items"]
    #
    offset += limit
    names = [_u(playlist["name"]) for playlist in playlists]
    found_start_playlist = start_name in names
    found_end_playlist   = end_name in names
    #
    if found_start_playlist:
      #
      index = names.index(start_name)
      all_playlists.extend(playlists[index:])
      #
    elif in_folder:
      #
      if found_end_playlist:
        #
        index = names.index(end_name) + 1
        all_playlists.extend(playlists[:index])
        break
        #
      else:
        #
        all_playlists.extend(playlists)
        #
      #
    #
    in_folder = in_folder or found_start_playlist
    #
  #
  print [_u(playlist["name"]) for playlist in all_playlists]
  #

def request_user_playlists(api_key, user_id, limit, offset):
  #
  endpoint = 'users/' + str(user_id) + '/playlists?limit=' + str(limit) + '&offset=' + str(offset)
  #
  return api_request(api_key, endpoint)
  #

def api_request(api_key, endpoint):
  #
  print "GET:\t" + endpoint
  #
  headers = {
    "Authorization": "Bearer " + api_key,
    "Accept": "application/json"
  }
  url = api_url + endpoint
  r = requests.get(url, headers=headers)
  return r.json()  
  #

def _u(s):
  return unicodedata.normalize('NFKD', s).encode('ascii','ignore')
