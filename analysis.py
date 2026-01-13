import json
location = {}
monthly = 0
list_dates = []
total_precipitation = 0
monthly_precipitation = {}
sum = 0

with open('precipitation.json') as file:
    data = json.load(file)
for dat in data:
        
    if dat['station'] == 'GHCND:US1WAKG0038':
        date = dat["date"]
        dates = date.split("-")
        months_index = dates[1]
            #total_precipitation = total_precipitation + int(dat['value'])
    
        if months_index not in monthly_precipitation:
            monthly_precipitation[months_index] = 0
        monthly_precipitation[dates[1]] += dat["value"]


for items in  monthly_precipitation :
    print(items,monthly_precipitation[items] )          
          
        
           # monthly_precipitation[int(dates[1])] = sum(location[int(dates[2])])
             
           # for key in location:
             #   monthly_precipitation [key[1]] = location[key]

            #while location[int(key[1])] > 12:

            
               
            #rint(monthly_precipitation)

            






      #  if dat['date'] == '2010-05':
         #   monthly_precipitation = monthly_precipitation + int(dat['value'])
       
#print(location)



#print(total_precipitation)

#print(data)