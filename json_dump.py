#import json
import io

#with io.open('LinkedIn_Saved2.txt', mode='r', encoding='utf-8') as file:
#    data = file.read()

#print(data)
#print(json.dumps(data))


from bs4 import BeautifulSoup
with io.open('LinkedIn_Saved2.html', mode='r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# find the title
title = soup.find('span', attrs={'class': 'lls-card-headline'})

print(title.string)

# loop through each iteration
#for each in title:
#    if each.find('title'):
#        title = title_box.text.strip().encode('utf-8')

# print the result
#print title