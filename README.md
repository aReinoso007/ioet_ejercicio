# Overview

To complete this task, it's important to first do some cleaning of the data to be processed. Then, check the days that the workers have gone into the office and select those that are the same. Once the day has been chosen, the time intervals are compared to see whether or not they are within the same time frame.

# Explanation

The data of each employee is divided into arrays, one contains the first worker and its data and the other the next one up. Each worker time frame is compared depending if they have gone into the office the same day, if the days don't match then the next value is compared. When the day and the time frames match up, then a 1 is added to a counter. The counter is for storing how many times those two workers were during the same time frame. 

# Methodology

1. Data cleaning
2. Looping through the data
3. Finding the matching days
4. Checking the time frames 

# How to run

In order to run this code, Python must be installed. 
```
python main.py "sample.txt"
```
or
```
python main.py "filename"
```
# Problem
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

