import json
x = [{
        "district": 1,
        "own-costs": 10198},
    {
        "location": "38,12",
        "capacity": 1507.0,
        "houses": [
            {
                "location": "33,7",
                "output": 39.45690812,
                "cables": [
                    "33,7",
                    "33,8",
                    "33,9",
                    "33,10",
                    "33,11",
                    "33,12",
                    "34,12",
                    "35,12",
                    "36,12",
                    "37,12",
                    "38,12"                   
                ]
            },
            {
                "location": "30,12",
                "output": 66.05341632,
                "cables": [
                    "30,12",
                    "31,12",
                    "32,12",
                    "33,12",
                    "34,12"                    
                ]
            }
        ]
    },
    {   
        "location": "42,3",
        "capacity": 1507.0,
        "houses": [
            {
                "location": "48,4",
                "output": 58.90934923,
                "cables": [
                "48,4",
                "48,3",
                "47,3",
                "46,3",
                "45,3",
                "44,3",
                "43,3",
                "42,3"
                ]
            }
        ]
    }
]

with open('output.json') as f:
    data = json.load(f)

data = json.dumps(x)
print(data)


# a_file = open("output.json", "r")
# a_json = json. load(a_file)
# pretty_json = json.dumps(x)
# a_file. close()
# print(pretty_json)

# print(json.dumps(x))
