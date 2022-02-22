# Overview

To complete this task, it's important to first do some cleaning of the data to be processed. Then, check the days that the workers have gone into the office and select those that are the same. Once the day has been chosen, the time intervals are compared to see whether or not they are within the same time frame.

# Explanation

The data of each employee is divided into arrays, one contains the first worker and its data and the other the next one up. Each worker time frame is compared depending if they have gone into the office the same day, if the days don't match then the next value is compared. When the day and the time frames match up, then a 1 is added to a counter. The counter is for storing how many times those two workers were at the office during the same time frame. 

# Methodology

## Data cleaning.
<br>
  Once the file has been loaded, the unwanted characters and blank spaces are removed and added to an array of lines, each line contains the data of the worker.
<br>
## Looping through the data
<br>
  After loading the data, each worker's data is compared to the next one in line. So at the end the employee before the last employee only compares it's data to the last one       since it has been already compared the ones before it.
<br>
## Finding the matching days
<br>
  To find the matching days, only the characters describing the days from Monday to Sunday are selected. When these match, then the time frames are compared.
<br>
## Checking the time frames 
<br>
  Here we have 4 variables, the first 2 contain the start and end hour of the first worker and the other 2 the starting and ending hour of the one before.
  So if the startTime1 is less than or equal than the endTime2 and if the startTime2 is less than or equal of the endTime1 then a 1 is added to the counter.
<br>
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

