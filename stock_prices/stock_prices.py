#!/usr/bin/python

import argparse


def find_max_profit(prices):
#Set max profit to nothing
  maxProfit = None
  #For every single price at i besides the last one, we compare price at i to each that comes after
  for i in range(0, len(prices)-2):
    #Here we find out the max profit possible from each selling point in comparison to i
    for x in range(i+1, len(prices)-1):
      if maxProfit is None or prices[x] - prices[i] > maxProfit:
      # if its the new max, update maxProfit accordingly
        print(maxProfit)
        maxProfit = prices[x] - prices[i]
  return maxProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))