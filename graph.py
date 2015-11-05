# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, dist, outside):
        self.src = src
        self.dest = dest
        self.dist = dist
        self.outside = outside
    def getDist(self):
        return self.dist
    def getOutside(self):
        return self.outside
    def __str__(self):
       return str(self.src) + '->' + str(self.dest) + "  " + self.outside + "  " + self.dist


class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
   def addNode(self, node):
       if node in self.nodes:
           #raise ValueError('Duplicate node')
           pass
       else:
           self.nodes.add(node)
           self.edges[node] = []
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src].append(dest)
   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]

class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        dist = edge.getDist()
        outside = edge.getOutside()
        if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
        self.edges[src].append((dest, dist, outside))


        # Right now, destinations of edges are added to the src nodes.  Figure out how to attach the weights to them.