import requests

draft_id = 522458773321240576
url = f'https://api.sleeper.app/v1/draft/{draft_id}/picks'

response = requests.get(url)

# print(response.status_code) - prints 200
# print(response.json())

picks = response.json()
# print(picks[0]) - look for 'roster_id' in both outputs -> use that to link pick number and total points acquired
for pick in picks:
    print(pick['metadata']['first_name'], pick['metadata']['last_name'], pick['metadata']['position'])

league_id = 522458773317046272

url2 = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
response2 = requests.get(url2)
# print(response2.status_code) - prints 200

rosters = response2.json()
# print(rosters[0]) - look for 'roster_id' in both outputs -> use that to link pick number and total points acquired

# fpts: actual points the team got in total
# ppts: highest total score a team could have gotten if the team had their highest scoring team in each week