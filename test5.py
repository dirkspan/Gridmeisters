import json
# from code.classes import grid

x = [{
        "district": district,
        "own-costs": own-costs},
    {
        "location": coordinates_battery,
        "capacity": cap_bat,
        "houses": [
            {
                "location": coordinates_house,
                "output": output_house,
                "cables": [
                    coordinates_cables                    
                ]},
            {
                "location": coordinates_house,
                "output": output_house,
                "cables": [
                    coordinates_cables                    
                ]
            }
        ]
    },
    {
        "location": coordinates_battery,
        "capacity": cap_bat,
        "houses": [
            {
                "location": coordinates_house,
                "output": output_house,
                "cables": [
                    coordinates_cables                    
                ]
            }
        ]
    }]

print(json.dumps(x))
