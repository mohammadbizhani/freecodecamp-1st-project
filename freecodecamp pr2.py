# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:22:47 2023

@author: Mohamad
"""

def add_time(x ,y , j = None ):

  AMPM = ["AM" , "PM"]
  # we split x into the time and AM or PM, x[0] is our time and x[1] is our PM or AM
  i = x.split()

  # check the day and night
  if i[1] not in AMPM:
    return "You should write PM or AM after the hour."

  # seperate both of times into the hour and minute
  first_time = i[0].split(":")
  second_time = y.split(":")

  # check the minute
  if int(first_time[1]) >= 60 or int(second_time[1]) >= 60:
    return "You should give standard minutes."

  # reach the sum of two hours
  final_time = (int(first_time[0]) + int(second_time[0]))*60 + int(first_time[1]) + int(second_time[1])
  final_hour = final_time // 60
  final_minute = final_time % 60

  # 12hr scale
  count = 0
  if final_hour > 12 and final_hour % 12 != 0:
    count = final_hour // 12
    final_hour = final_hour % 12
  elif final_hour // 12 > 0 and final_hour % 12 == 0:
    count = (final_hour // 12)
    final_hour = final_hour - (count - 1)*12

  # switch between AM and PM
  if (count % 2) == 0:
    TZ = i[1]
  else:
    if i[1] == "AM":
      TZ = "PM"
    elif i[1] =="PM":
      TZ = "AM"
    else:
      pass

  # changing the days
  day = ""
  if i[1] == "PM" and (count == 1 or count == 2):
    day = "(next day)"
  elif i[1] == "AM" and (count == 2 or count == 3):
    day = "(next day)"
  elif i[1] == "PM" and count > 2:
    day = f'({int((count + 1) / 2)} days later)'
  elif i[1] == "AM" and count > 2:
    day = f'({int((count) / 2)} days later)'

  print( (str(final_hour) + ":" + str(final_minute).rjust(2, '0')), TZ , day )