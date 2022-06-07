# Run-Index-Project
This is my first passion project as a beginner in tech. Being the cricket 
aficionado that I am, I felt the need for a proper parameter that estimates the 
impact of a T20 inning. The other parameters like strike rate and average are 
not competent enough to convey the impact. This being my main motivation, I 
devised a new parameter Run Index.

Run Index is the overall T20 impact of a batsman for an inning. This parameter is 
relevant only for T20 format. It can be obtained for every inning of a player's
T20 career. The average run index of all innings gives a very good estimate of the
player's T20 impact. To obtain run index, we have to factor in the runs scored, 
rate at which the runs were scored, and the fraction of the players runs in the 
team's total.

Run Index = R * (R/B) * (1 + (R/T))

R = Runs scored
B = Balls faced
T = Teams total

In the Scrap module, the inning by inning data of runs scored, balls faced, team's
total for every match of the players career is collected. It requires links of the 
webpage of player's innings and team innings. This data is scraped from 
https://www.espncricinfo.com/ database with the help of beautifulsoup python library.

RunIndex module contains functions for generating Run Index of an inning and
calculating overall average run index.

Driver module is the main program where the links are to be pasted and the run index 
of the patricular player is displayed.
