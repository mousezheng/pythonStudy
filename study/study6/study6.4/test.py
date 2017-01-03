import pydot
import pylab as plb
g = pydot.Dot(graph_type='graph')
g.add_node(pydot.Node(str(0),fontcolor='transparent'))
for i in range(5):
    g.add_node(pydot.Node(str(i+1)))
    g.add_edge(pydot.Edge(str(0),str(i+1)))
    for j in range(5):
        g.add_node(pydot.Node(str(j+1)+'-'+str(i+1)))
        g.add_edge(pydot.Edge(str(j+1)+'-'+str(i+1),str(j+1)))
imshow(g)