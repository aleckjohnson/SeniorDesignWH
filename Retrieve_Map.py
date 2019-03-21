import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
ox.config(use_cache=True, log_console=False)		# Enable cache for storing json data and enable console output for debugging
#ox.__version__



# get a graph for some city
G = ox.graph_from_place('Winter Haven, Florida, USA', network_type='all_private')
fig, ax = ox.plot_graph(G, node_size=10, node_color='#66cc66')
ox.save_graph_shapefile(G, filename='wh.jpg')
width = fig.dpi
height = fig.dpi
print("Height is "+str(height)+" Width is "+str(width))

# Determine the area in square meters
G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges = False);
area_meters = nodes_proj.unary_union.convex_hull.area
print("Area = " + str(area_meters));
