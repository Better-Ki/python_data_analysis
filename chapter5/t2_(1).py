import graphviz

with(open('tree.dot', encoding='utf-8')) as f:
    dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.view()