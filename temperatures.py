############################################
# Creating json from n same size iterables #
############################################

# import json module
import json

# iterables examples
date_list = ["2021/04/15", "2021/04/16", "2021/04/17"]
weather_list = ["cloudy", "variable", "sunny"]
temperature_list = [[7, 15], [10, 18], [13, 25]]

# initializing objects and loop counter
my_json = []
json_element = {}
i = 0

# looping through iterables adding elements to final objects
for x in range(len(date_list)):
    json_element["date"] = date_list[i]
    json_element["weather"] = weather_list[i]
    json_element["temperature"] = temperature_list[i]
    
    my_json.append(json_element)
    json_element = {}
    i += 1
    
# creating json file dumping final object
with open('my_json.json', 'w') as outfile:
    outfile.write(json.dumps(my_json, indent=4))

