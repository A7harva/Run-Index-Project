from bs4 import BeautifulSoup
import requests

def Name_scrap(player_link):
    html_text = requests.get(player_link).text
    soup = BeautifulSoup(html_text, 'lxml')

    name = soup.find('div', class_ = 'icc-home').find('a').text[26:-31]

    return name    


def Data_scrap(player_link, match_link):
    data = []

    #Initializing html file and beautifulsoup
    html_text = requests.get(player_link).text
    soup = BeautifulSoup(html_text, 'lxml')
    html_text1 = requests.get(match_link).text
    soup1 = BeautifulSoup(html_text1, 'lxml')

    totals = soup1.find('td', class_ = 'padTSw').find_parent().find_parent().find_all('tr')
    innings = soup.find_all('tr', class_ = 'data1')[1:]

    
    #collecting data by iterating each inning data
    for index,inning in enumerate(innings):

        if 'DNB' not in inning.td.text:

            if '*' not in inning.find_all('td')[0].text:
                runs = int(inning.find_all('td')[0].text)
                status = False
            else:
                runs = int(inning.find_all('td')[0].text[:-1])
                status = True


            if '/' in totals[index].td.text:
                total = int(totals[index].td.text[:-2])
            else:
                total = int(totals[index].td.text)


            balls = int(inning.find_all('td')[2].text)
            if balls == 0:
                continue


            data.append({"r": runs, "b": balls, "t": total, "s": status})
    

    return data