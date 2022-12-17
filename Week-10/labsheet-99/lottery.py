#!/usr/bin/env python3

import sys
tickets = sys.stdin.readlines()

#create a list of the winning numbers
winning_ticket = []
winning_ticket.append(int(sys.argv[1]))
winning_ticket.append(int(sys.argv[2]))
winning_ticket.append(int(sys.argv[3]))

#setting variables to check if a number has been read yet
first = True
second = True
third = True

#this loop runs through all the tickets in standard input
i = 0
while i < len(tickets):

  #checks each number and increase total by 1 if it is a winning number
  total = 0
  j = 0
  while j < len(tickets[i].split(" ")):
    if int(tickets[i].split(" ")[0]) in winning_ticket and first is True:
      total = total + 1
      first = False

    if int(tickets[i].split(" ")[1]) in winning_ticket and second is True:
      total = total + 1
      second = False

    if int(tickets[i].split(" ")[2]) in winning_ticket and third is True:
      total = total + 1
      third = False

    j = j + 1
  first = True
  second = True
  third = True

  #the following checks the total variable and prints the prize amount
  if total == 0:
    print(0)

  elif total == 1:
    print(1)

  elif total == 2:
    print(5)

  elif total == 3:
    print(100)

  i = i + 1
