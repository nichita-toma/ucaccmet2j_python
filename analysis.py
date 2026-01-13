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
        total_precipitation = total_precipitation + int(dat['value'])
    
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


print(text_list_relative)
#print(text_list)         
          

print(total_precipitation)
with open ("results.json", "w", encoding = "utf-8") as file:
       json.dump(text_list, file, indent = 4)

   