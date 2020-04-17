# Pathway 1

## Contents
The folder "course2" is created by Scrapy. Within "course2" there is another "course2" folder that contains my code under /spiders/mathucb.py. The data exportting code is in settings.py 

## Procedure 
- Using scrapy, I created a project called course2
- within this project I created a spider called mathucb. The mathucb spider reads the HTML file containing the course content for Math 104: Intro to Real Analysis at UC Berkeley in the Spring of 2019. 
- The parser takes out some of the course information (i.e., title, instructor information and section times). I also included the body of the course page separately, which can be decomposed in a similar way. 
- The scraped info is then outputted in a python dictionary and saved in coursepage.csv.
