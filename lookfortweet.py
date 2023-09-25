import json
import os

deleted_list = []
nondeleted_list = []
resultslist = []

directory = 'twitter_scraper_data'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file = open(f)
        data = json.load(file)
        print(f)

        for i in data:
            resultslist.append(str(i['startUrl']))

        with open('SpiltFolder/' + str(f)[45:52] + '.txt', 'r') as file:
            print('SpiltFolder/' + str(f)[45:52] + '.txt')
            linklist = file.read().splitlines()


        for n in linklist:
            if str(n) not in resultslist:
                deleted_list.append((str(n)[35:57]))
                # print('Does not contain ' + str(n))
            else:
                nondeleted_list.append((str(n)[35:57]))
                # print('Does contain ' + str(n))


with open('deleted_ids.txt', 'w') as f:
    for id in deleted_list:
        f.write(id + str('\n'))

with open('nondeleted_ids.txt', 'w') as f:
    for id in nondeleted_list:
        f.write(id + str('\n'))

# print(deleted_list)
print('Length of Deleted ' + str(len(deleted_list)))
# print(nondeleted_list)
print('Length of Nondeleted ' + str(len(nondeleted_list)))






