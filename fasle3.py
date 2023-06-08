
from google.colab import drive
drive.mount('/content/drive')


print('File decompressed and rewritten.')

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


#25

G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t', nodetype=int)

G_e = nx.gnm_random_graph(G_real.number_of_nodes(), G_real.number_of_edges())

#26

degree = [val for (node, val) in G.degree()]
G_conf = nx.configuration_model(degrees)

#27
11
# Compute degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)


degrees = [val for (node, val) in G_real.degree()]
G_config = nx.configuration_model(degrees)
G_config = nx.Graph(G_config)

# Plot degree distribution
plt.figure()
plt.loglog(degree_count[0], degree_distribution, 'b.', markersize=8)
plt.xlabel('Degree')
plt.ylabel('Probability')
plt.title('Degree Distribution')
plt.show()

#28
spl = dict(nx.all_pairs_shortest_path_length(G))

spl= [path_length for source in spl for target, path_length in source[1].items()]
for source in spl.keys():
    for target in spl[source].keys():
        spl_list.append(spl[source][target])


# 29
clustering = nx.clustering(G)
clustering_sequence = sorted([c for n, c in clustering.items()], reverse=True)
clustering_count = np.unique(clustering_sequence, return_counts=True)
clustering_distribution = clustering_count[1]/sum(clustering_count[1])


cc_sizes = [len(c) for c in nx.connected_components(G)]



# 30
wcc_sizes = [len(c) for c in nx.connected_components(G.to_undirected())]
wcc_count = np.unique(wcc_sizes, return_counts=True)
