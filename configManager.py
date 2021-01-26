import os
import json

default_json = {'discordbot': {'bottoken': ''}, 'server': {'guild': '', 'duckChannel': '', 'factChannel': ''}}

if not os.path.exists("config.json"):
    print("There was no config file yet. Creating one now. Please fill in all required information.")
    with open("config.json", 'w') as outfile:
        json.dump(default_json, outfile, indent=4)
        exit()

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    botData = data["discordbot"]
    serverData = data["server"]