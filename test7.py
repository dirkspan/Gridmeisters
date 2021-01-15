coordinate_house =[33, 7]
coordinate_corner=[33, 12]
coordinate_battery=[38, 12]

route = []

# start is house, end is battery
current_x_cor = coordinate_house[0]
end_x= coordinate_battery[0]
current_y_cor = coordinate_house[1]
end_y = coordinate_battery[1]

while current_y_cor < end_y:
    route.append((current_x_cor, current_y_cor))
    current_y_cor += 1

while current_x_cor <= end_x:
    route.append((current_x_cor, current_y_cor))
    current_x_cor += 1

print(route)