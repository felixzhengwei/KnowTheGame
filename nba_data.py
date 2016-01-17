import requests  
import json  
import pandas as pd
import database as db
from datetime import datetime 
import datetime as dtime
import calendar
from dateutil.parser import parse
import time

# Defining constants
default_api_string = "http://stats.nba.com/stats/"
player_stats_endpoint = "playercareerstats?"
player_logs_per_game_endpoint = "playergamelog?"
player_overall_stats_query = "perMode=Totals&playerID="
player_stats_per_game_query = "Season=2015-16&SeasonType=Regular Season&playerID="
league_id = "00"
player_names_map = {}
all_player_names = list()


# Create dictionary of player names and id's
def get_player_name_map():
	with open ('players.json') as player_name_data:
		player_names = json.load(player_name_data)
		for item in range(len(player_names)):
			full_name = player_names[item]['firstName'] + " " + player_names[item]['lastName']
			all_player_names.append(full_name)
			player_id = player_names[item]['playerId']
			player_names_map[full_name] = player_id
	return player_names_map

# Return date number
def dow(dt):
	dat = parse(dt).strftime('%d/%m/%Y')
	y = datetime.strptime(dat, "%d/%m/%Y")
	days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	# day, month, year = (int(x) for x in dat.split('/'))
	dayNumber=dtime.date.weekday(y)
	return days[dayNumber]

# Return id of a given player 
def get_player_id(player_name):
	player_names_map = get_player_name_map()
	for key, value in player_names_map.items():
            if key == player_name: 
                return value

# Get stats of a given player 
def get_overall_player_stats(player_id):  
    # API string for NBA API
    url_string = default_api_string + player_stats_endpoint + player_overall_stats_query + str(player_id)
    # Create dictionary of JSON response 
    response = requests.get(url_string)
    player_overall_data = json.loads(response.text)
    return player_overall_data

# Get stats of a given player 
def get_player_stats_per_game(player_id):  
    # API string for NBA API
    url_string = default_api_string + player_logs_per_game_endpoint + player_stats_per_game_query + str(player_id)
    # Create dictionary of JSON response 
    response = requests.get(url_string)
    player_data_per_game_dirty = json.loads(response.text)
    clean_data(player_data_per_game_dirty)

def clean_data(data):
	clean_data = {}
	record_set = data["resultSets"][0]["rowSet"]
	clean_data["gameDate"] = []
	clean_data["home"] = []
	clean_data["away"] = []
	clean_data["DayofWeek"] = []
	clean_data["wl"] = []
	clean_data["min"] = []
	clean_data["fgPct"] = []
	clean_data["ftPct"] = []
	clean_data["reb"] = []
	clean_data["ast"] = []
	clean_data["stl"] = []
	clean_data["blk"] = []
	clean_data["tov"] = []
	clean_data["pts"] = []
	clean_data["plusMinus"] = []
	

	for each_item in range(len(record_set)):
		clean_data["gameDate"].append(record_set[each_item][3])

		if record_set[each_item][4].find("@") >= 0:
			record_set[each_item][4] = record_set[each_item][4].split('@')
			clean_data["away"].append(record_set[each_item][4][0])
			clean_data["home"].append(record_set[each_item][4][1])
		else: 
			record_set[each_item][4] = record_set[each_item][4].split('vs.')
			clean_data["home"].append(record_set[each_item][4][0].strip())
			clean_data["away"].append(record_set[each_item][4][1].strip())
		# print dow(record_set[each_item][3])
		clean_data["DayofWeek"].append(dow(record_set[each_item][3]))
		clean_data["wl"].append(record_set[each_item][5])
		clean_data["min"].append(record_set[each_item][6])
		clean_data["fgPct"].append(record_set[each_item][9])
		clean_data["ftPct"].append(record_set[each_item][15])
		clean_data["reb"].append(record_set[each_item][18])
		clean_data["ast"].append(record_set[each_item][19])
		clean_data["stl"].append(record_set[each_item][20])
		clean_data["blk"].append(record_set[each_item][21])
		clean_data["tov"].append(record_set[each_item][22])
		clean_data["pts"].append(record_set[each_item][24])
		
	upload_data(clean_data)

def upload_data(clean_data):
	try: 
		for i in range(len(clean_data)):
			sql_command = ('INSERT INTO dbo.player_data_complete (FullName,GameDate,HomeTeam,VisitorTeam,DayofWeek,WL,Min,FgPct,FtPct,Reb,Ast,Stl,Blk,Tov,Pts) VALUES (' + "'" + str(player_name) + "','" + str(clean_data["gameDate"][i]) + "','" + str(clean_data["home"][i]) + "','" + \
			               	 	str(clean_data["away"][i]) + "','" + str(clean_data["DayofWeek"][i]) + "','" + str(clean_data["wl"][i]) + "'," + str(clean_data["min"][i]) + ",'" + str(clean_data["fgPct"][i]) + "','"+  str(clean_data["ftPct"][i]) + "'," + \
			               	 	str(clean_data["reb"][i]) + "," + str(clean_data["ast"][i]) + "," + str(clean_data["stl"][i]) + "," + str(clean_data["blk"][i]) + "," + str(clean_data["tov"][i]) +  "," + \
			               	 	str(clean_data["pts"][i]) + ")")
			print sql_command
		 	db.run_query(sql_command)
	except Exception:
		pass

get_player_name_map()

for player in all_player_names:
	print player
	player_name = player
	player_id = get_player_id(player_name)
	print player_id
	player_data = get_player_stats_per_game(player_id)


# random_name = "Andre Drummond"
# playerID = get_player_id(random_name)
# print playerID 
# data = get_player_stats_per_game(playerID)
# print json.dumps(data, indent = 4, sort_keys = True)




