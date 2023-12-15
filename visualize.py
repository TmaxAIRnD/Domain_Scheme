import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import matplotlib as mpl

df = pd.read_csv('schema/Article.csv')
df = df.iloc[:, :5]
df.head(5)

df['Entity'] = df['Entity'].fillna(method='ffill')
df.set_index(['Entity'])


rel_df = pd.read_csv('schema/Relation.csv')
rel_df.head()

G = nx.from_pandas_edgelist(rel_df, 'Subject', 'Object', 'Relation', create_using=nx.DiGraph(directed=True))
nx.get_edge_attributes(G, 'Relation')

plt.rc('font', family='Malgun Gothic')

options = {
    "node_size": 2500,
    "font_size": 12,
    "font_family": "Malgun Gothic",
    "font_color": "white",
    "arrows": True,
    "arrowsize": 10,
    "width": 1.0
}


fig, ax = plt.subplots(1, 1, figsize=(15, 10))
pos = nx.spring_layout(G)  # 그래프 레이아웃 설정
nx.draw_networkx(G, pos, **options)
# nx.draw_networkx_nodes(G, pos, node_size=2500)  # 노드 시각화
# nx.draw_networkx_labels(G, pos, font_family="Malgun Gothic", font_color="white")  # 노드 라벨 시각화
# nx.draw_networkx_edges(G, pos, width=1.0, arrows=True, arrowstyle="-|>", arrowsize=10)  # 엣지 시각화
# edge_labels = nx.get_edge_attributes(G, 'Relation')  # 엣지 속성값 가져오기
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family="Malgun Gothic", font_color="black")  # 엣지 라벨 시각화
for u, v, d in G.edges(data=True):
    if u == v:  # if self loop
        plt.text(pos[u][0]-0.07, pos[u][1]+0.1, str(d['Relation']), fontsize=10)
    else:
        nx.draw_networkx_edge_labels(G, pos, {(u, v): str(d['Relation'])}, font_family="Malgun Gothic")

plt.show()