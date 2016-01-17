import requests
import json
x = requests.get("http://stats.nba.com/stats/scoreboard/?GameDate=01/11/2016&LeagueID=00&DayOffset=0")
data = json.loads(x.text)


print data["resultSets"][0]["rowSet"]
	

