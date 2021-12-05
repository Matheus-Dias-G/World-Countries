import requests
from bs4 import BeautifulSoup

#site:https://www.scrapethissite.com/pages/simple/

class Country:
    url = requests.get('https://www.scrapethissite.com/pages/simple/')

    soup = BeautifulSoup(url.content, 'html.parser')
 
    repost = soup.find_all('div', class_='col-md-4 country')
    def get_countrie(self, index):
        c = []
        for cells in self.repost:
            flag_icon = cells.find('h3', class_='country-name').get_text()
            for self.countries in flag_icon.split(' '):
                if self.countries != '\n\n' and self.countries != '':
                    for n in self.countries.split(' '):
                        #if n[-1] == '\n':
                        c.append(self.countries.split(' '))
        
        countries_names = []
        empty_country = ''
        for v in c:
            while v[0][-1] != '\n':
                empty_country += f'{v[0]} '
                break
            if v[0][-1] == '\n' and empty_country != '':
                empty_country += f'{v[0]}'
                countries_names.append(empty_country)
                #print(empty_country)
                empty_country = ''
            elif v[0][-1] == '\n':
                countries_names.append(v[0])
        return countries_names[index]

                #you can change values from string using indice a[0:1] = 'a'
                        
    

    def get_info(self, index_info):
        cap = []
        area = []
        population = []
        all_info = {
                'area':area,
                'population':population,
                'capital':cap
                }

        for x in self.repost:
            capitals = x.find('span', class_='country-capital').get_text()
            popu =  x.find('span', class_='country-population').get_text()
            a = x.find('span', class_='country-area').get_text()
            cap.append(capitals.split(' ')[0])
            area.append(a.split(' ')[0])
            population.append(popu.split(' ')[0])
        
        return all_info['capital'][index_info], all_info['area'][index_info], all_info['population'][index_info]

index = 1
numbers = True
while numbers == True:
    try:
        x = Country()
        a = x.get_countrie(index)
        b = x.get_info(index)
        print('country:\n',
                a,'  |capital   ', '|area   ', '    |population\n', ' ', b)
        index += 1
    except IndexError:
        numbers == False

