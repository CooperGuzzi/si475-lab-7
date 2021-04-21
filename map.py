# reads in adjancency matrix and start+end point, runs djisktas on it

from math import pow, sqrt
import argparse
import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt

# distances are implemented in here


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,point):
        #distance between two points
        return sqrt(pow(self.x-point.x,2)+pow(self.y-point.y,2))

class Map:
    def __init__(self):
        # read from file 
        parser = argparse.ArgumentParser(description='Read in Dot file and 1-2 x y points')
        parser.add_argument('f', help='filename')
        parser.add_argument('e', type=int, nargs=2, help='end')
        parser.add_argument('-s','--start', type=int, nargs=2, help='start')
        args = parser.parse_args() # maybe
        #open f as file
        #for line in f: 
            # read in points

            # read in connections
        #https://stackoverflow.com/questions/17947027/open-dot-formatted-graph-from-python
        Gtmp = pgv.AGraph(f)
        G = nx.Graph(Gtmp)
        nx.draw(G)
        plt.show()

m = Map()


'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
'''