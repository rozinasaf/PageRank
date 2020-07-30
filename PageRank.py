import random
from collections import defaultdict
import crawler

graph = crawler.graph

def pagerank(graph, damping):
    iter = 1000000
    c = defaultdict(float)
    for l in graph:
        c.update({l:0.0})
                
    jump = random.choice(list(graph.keys()))
    for i in range(0, iter):
        c[jump] += 1
        x = random.random()
        if(x > damping):
            link = random.randint(0, len(graph[jump])-1)
            jump = graph[jump][link]
        else:
            jump = random.choice(list(graph.keys()))
    
    for j in c:
        c[j] = c[j]/float(iter)
        print(j, ": ", c[j])       
    
def main():
    crawler.crawler("/wiki/PageRank")
    pagerank(crawler.graph, 0.3)
    
if __name__ == "__main__":
    main()