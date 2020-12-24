import wealthsimple
import json

# Get username and password from creds.txt file
with open("creds.txt", 'r') as f:
    credentials = f.readlines()
    username = credentials[0].strip()
    password = credentials[1].strip()
    ws_id = credentials[2].strip()
f.close()


def two_factor_auth():
    code = ""
    while not code:
        code = input("Enter two-factor authentication code: ")

    return code


WS = wealthsimple.WSTrade(username, password, two_factor_callback=two_factor_auth)

#print(WS.get_account_ids())
#print(WS.get_activities())
position_list = WS.get_positions(ws_id)
data = {'positions': []}
for p in position_list:
    data['positions'].append(p)

with open('positions.txt', 'w') as outfile:
    json.dump(data, outfile)
outfile.close()
