import requests
from bs4 import BeautifulSoup
import time
import re
import csv
import json


data = []

for vnum in range(1,114):
        
    URL = "https://www.codewithharry.com/videos/java-tutorials-for-beginners-"+str(vnum)

    print("going to hit => "+URL)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", class_="contentBox")

    try:
        for link in results.find_all('a', attrs={'href': re.compile("(.pdf)")}) :
            print("LinkRecieved => "+ link.get('href'))
            data.append(['videoNo ' + str(vnum), str(link.get('href'))]) 
        
            # print(data)
    except:
    
        print("An exception occurred")
        data.append(['videoNo ' + str(vnum), "No Link Find"]) 
        print("No Link Found at vid " + str(vnum) + " No Link Find \n") 

    time.sleep(3)    
    

print("\n")
print('I am on final stage')
# print(data)
json_data = json.dumps(data)

f = open("RawData.txt", "a")
f.write(str(json_data))
f.close()

# arr = []
# for vnum in range(1,10):
#     arr.append(['Afghanistan'+str(vnum), 652090, 'AF'+str(vnum), 'AFG'+str(vnum)])
#     print(arr)
#     print('\n')


# print('final stage data \n')
# print(arr)



# links = results.findAll("a")







header = ['Video No', 'Link']
# data = [
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA'],
#     ['American Samoa', 199, 'AS', 'ASM'],
#     ['Andorra', 468, 'AD', 'AND'],
#     ['Angola', 1246700, 'AO', 'AGO']
# ]

with open('CodeHarryJavaNotes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(data)


# cars = []

# for x in range(6):
#     time.sleep(1)
#     cars.append("Honda"+str(x))
#     print(x)
    

# print(cars)


# lk = "https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/java-tutorials-for-beginners-111/AdvancedJava2Notes.pdf"

# print(lk.endswith('.pdf'))













# Use Regex for find perfect link .pdf ending
# Check blank / no link
# 