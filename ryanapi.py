import requests
 
headers = {
    'Postman-Token': '41c63c39-c172-49f4-99c9-3f14a0711de2',
    'Referer': 'stats.nba.com',
    'cache-control': 'no-cache'
}
 
params = (
    ('leagueId', '00'),
    ('season', '2020-21'),
    ('seasonType', 'Regular Season'),
    ('teamId', '1610612738'),
    ('playerId', '1628369'),
    ('gameId', ''),
    ('outcome', ''),
    ('location', ''),
    ('month', '0'),
    ('seasonSegment', ''),
    ('dateFrom', ''),
    ('dateTo', ''),
    ('opponentTeamId', '0'),
    ('vsConference', ''),
    ('vsDivision', ''),
    ('position', ''),
    ('playerPosition', ''),
    ('rookieYear', ''),
    ('gameSegment', ''),
    ('period', '0'),
    ('lastNGames', '0'),
    ('clutchTime', ''),
    ('aheadBehind', ''),
    ('pointDiff', ''),
    ('rangeType', '0'),
    ('startPeriod', '1'),
    ('endPeriod', '10'),
    ('startRange', '0'),
    ('endRange', '2147483647'),
    ('contextFilter', ''),
    ('contextMeasure', 'PTS'),
)
 
response = requests.get('http://stats.nba.com/stats/shotchartdetail/?leagueId=00&season=2020-21&seasonType=Regular+Season&teamId=1610612738&playerId=1628369&gameId=&outcome=&location=&month=0&seasonSegment=&dateFrom=&dateTo=&opponentTeamId=0&vsConference=&vsDivision=&position=&playerPosition=&rookieYear=&gameSegment=&period=0&lastNGames=0&clutchTime=&aheadBehind=&pointDiff=&rangeType=0&startPeriod=1&endPeriod=10&startRange=0&endRange=2147483647&contextFilter=&contextMeasure=PTS', headers=headers)
print(response)