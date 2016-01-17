import requests  
import json  
import pandas as pd

# Defining constants
default_api_string = "http://stats.nba.com/stats/"
player_stats_endpoint = "playercareerstats?"
player_logs_per_player = "playergamelog?"
player_stats_query = "perMode=Totals&playerID="
season = "2015-16"
league_id = "00"
player_names_map = {}

# Create dictionary of player names and id's
def get_player_name_map():
	with open ('players.json') as player_name_data:
		player_names = json.load(player_name_data)
		for item in range(len(player_names)):
			full_name = player_names[item]['firstName'] + " " + player_names[item]['lastName']
			player_id = player_names[item]['playerId']
			player_names_map[full_name] = player_id
	return player_names_map

# Return id of a given player 
def get_player_id(player_name):
	player_names_map = get_player_name_map()
	for key, value in player_names_map.items():
            if key == player_name: 
                return value


# Get stats of a given player 
def get_player_stats(player_id):  
    # API string for NBA API
    url_string = default_api_string + player_stats_endpoint + player_stats_query + str(player_id)
    # Create dictionary of JSON response 
    response = requests.get(url_string)
    player_data = json.loads(response.text)
    return player_data

# Test
random_name = "Stephen Curry"
playerID = get_player_id(random_name)
print playerID 
data = get_player_stats(playerID)
print json.dumps(data, indent = 4, sort_keys = True)

