import json

import pandas as pd
import requests

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

header_data  = {
    'User-Agent': 'Some User Agent',
    'x-nba-stats-origin': 'stats',
    'Referer': 'https://stats.nba.com/',
}


# endpoints
def player_stats_url(season):
    return "http://stats.nba.com/stats/shotchartdetail/?leagueId=00&season={0}&seasonType=Regular+Season&teamId=1610612738&playerId=1628369&gameId=&outcome=&location=&month=0&seasonSegment=&dateFrom=&dateTo=&opponentTeamId=0&vsConference=&vsDivision=&position=&playerPosition=&rookieYear=&gameSegment=&period=0&lastNGames=0&clutchTime=&aheadBehind=&pointDiff=&rangeType=0&startPeriod=1&endPeriod=10&startRange=0&endRange=2147483647&contextFilter=&contextMeasure=PTS".format(
        season)

# Extract json
def extract_data(url):
    r = requests.get(url, headers=header_data)                  # Call the GET endpoint
    resp = r.json()                                             # Convert the response to a json object
    print(resp)
    results = resp['resultSets']                             # take the first item in the resultsSet (This can be determined by inspection of the json response)
    headers = results['headers'][1]['columnNames']
    print(headers)                               # take the headers of the response (our column names)
    rows = results['rowSet']                                    # take the rows of our response
    frame = pd.DataFrame(rows)
    print(frame)                                 # convert the rows to a dataframe
    frame.columns = headers                                     # set our column names using the  extracted headers
    return frame


season = "2020-21"

frame = extract_data(player_stats_url(season))
print(frame)

frame.to_csv("shots_nba_player_data_{0}.csv".format(season), index=False)