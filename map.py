# reads in adjancency matrix and start+end point, runs djisktas on it

from math import pow, sqrt
import argparse


# distances are implemented in here


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,point):
        #distance between two points
        return sqrt(pow(self.x-point.x,2)+pow(self.y-point.y,2))

class Map:
    def __init__(self, file):
        # read from file 
        parser = argparse.ArgumentParser(description='Process filename')
        parser.add_argument('filename', metavar='F', type=string, nargs='1', help='filename')
        parser.add_argument('end', metavar='E', type=list, nargs='1', help='end')
        parser.add_argument('start', metavar='S', type=list, nargs='1', help='start')
        parser.parserargs() # maybe
        for line in filename:
            # read in points

            # read in connections


