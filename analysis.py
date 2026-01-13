import json
stations = { "GHCND:USW00093814", "GHCND:US1WAKG0038", "GHCND:USC00513317", "GHCND:US1CASD0032"}
monthly = 0
list_dates = []
total_precipitation = 0
monthly_precipitation = {}
all_stations_total_precipitation = 0
sum = 0

with open('precipitation.json') as file:
    data = json.load(file)
    for total_rain in data:
        all_stations_total_precipitation = all_stations_total_precipitation + int(total_rain["value"])
    for station in stations: 
        relative_yearly_precipitation = 0
        total_precipitation = 0
        for dat in data: 
            if dat['station'] == station:
                date = dat["date"]
                dates = date.split("-")
                months_index = dates[1]
                total_precipitation = total_precipitation + dat['value']
            
                if months_index not in monthly_precipitation:
                    monthly_precipitation[months_index] = 0
                monthly_precipitation[dates[1]] += dat["value"]


                text_list = []
                text_list_relative = []
                
                for items in  monthly_precipitation :
                    text = f'Monthly precipitation in month {items} is {monthly_precipitation[items]}'
                    text_list.append(text)
                    text_relative = f'The relative precipitacion for month {items} is {monthly_precipitation[items]/total_precipitation}'
                    text_list_relative.append(text_relative)
                
            relative_yearly_precipitation = total_precipitation/all_stations_total_precipitation


        
            
             
            
        print(data)
    
        #print(all_stations_total_precipitation)
        #print(relative_yearly_precipitation)         
          

#print(total_precipitation)
#with open ("results.json", "w", encoding = "utf-8") as file:
     #  json.dump(text_list, file, indent = 4)

   