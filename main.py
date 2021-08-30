import plotly.express as px

from plotly.offline import plot
import numpy as np

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", 
             "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", 
             "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

# Countries and their neighbors
neighbors_dict = {
    'Argentina': ['Bolivia', 'Brazil', 'Chile', 'Paraguay', 'Uruguay'],
    'Bolivia': ['Argentina', 'Brazil', 'Chile', 'Paraguay', 'Peru'],
    'Brazil': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Paraguay',
               'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    'Chile': ['Argentina', 'Bolivia', 'Peru'],
    'Colombia': ['Brazil', 'Ecuador', 'Peru', 'Venezuela'],
    'Ecuador': ['Colombia', 'Peru'],
    'Falkland Islands': [],
    'Guyana': ['Brazil', 'Suriname', 'Venezuela'],
    'Paraguay': ['Argentina', 'Bolivia', 'Brazil'],
    'Peru': ['Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador'],
    'Suriname': ['Brazil', 'Guyana'],
    'Uruguay': ['Argentina', 'Brazil'],
    'Venezuela': ['Brazil', 'Colombia', 'Guyana']
    }


# Write your code here
def build_graph(countries, neighbors_dict):
    graph = np.zeros((len(countries), len(countries)))
    
    neigbors_len_list = []
    
    for i in range(len(countries)):
        country = countries[i]
        neigbors = neighbors_dict[country]
        neigbors_index = np.searchsorted(countries, neigbors)
        graph[i][neigbors_index] = 1
        neigbors_len_list.append(len(neigbors_index))
        
    return graph, neigbors_len_list
        

class Graph():
 
    def __init__(self, vertices, sorted_index):
        self.V = vertices
        self.sorted_index = sorted_index
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]
            
    # A utility function to check if the current color assignment is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
    
    # Backtracking function to solve m coloring  problem
    def graphColourUtil(self, m, colour, v, index):
        if v == -1:
            return True
 
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, self.sorted_index[index + 1], 
                                        index + 1) == True:
                    return True
                colour[v] = 0
    
    # Prepare and return color map
    def graphColouring(self, m):
        colour = [0] * self.V
        index = 0
        if self.graphColourUtil(m, colour, self.sorted_index[index], index) == None:
            return False
        
        print("Solution exist")
        colormap_result = {}
        
        for index, country in enumerate(countries):
            colormap_result[country] = colors[colour[index] - 1]
            
        return colormap_result


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    
    plot(fig)
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    
    # Build the graph with neigbors information
    graph, neigbors_len_list = build_graph(countries, neighbors_dict)
    sorted_index = np.argsort(neigbors_len_list)[::-1]
    
    sorted_index = np.append(sorted_index, -1)
    
    # Create graph obj and assign builted graph to obj graph
    g = Graph(len(countries), sorted_index)
    g.graph = graph
    
    # Find color map
    colormap_result = g.graphColouring(len(colors))
    
    # coloring test
    # colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
    #                   "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
    #                   "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    # plot_choropleth(colormap=colormap_test)
    
    plot_choropleth(colormap=colormap_result)

