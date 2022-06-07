from msvcrt import getch
import RunIndex
import Scrap

vk_player_link = 'https://stats.espncricinfo.com/ci/engine/player/253802.html?class=3;template=results;type=batting;view=innings'
vk_match_link = 'https://stats.espncricinfo.com/ci/engine/team/6.html?class=3;filter=advanced;orderby=start;player_involve=49752;template=results;type=team;view=innings'

print(open("info.txt", "r").read())

player_link = input('Enter Player link: ')
match_link = input('Enter Match link: ')

print('----------------------------------------------------------------------------------')

print(Scrap.Name_scrap(player_link), RunIndex.Avg_run_index(Scrap.Data_scrap(player_link, match_link)))
print("Virat Kohli's Run Index for reference", RunIndex.Avg_run_index(Scrap.Data_scrap(vk_player_link, vk_match_link)))

print('----------------------------------------------------------------------------------')

getch()