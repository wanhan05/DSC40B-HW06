from collections import deque
def assign_good_and_evil(graph):
    labels = {}
    nodes = graph.nodes
    for start_node in nodes:
        if start_node in labels:
            continue
        
        queue = deque([start_node])
        labels[start_node] = 'good'
        
        while queue:
            current = queue.popleft()
            current_label = labels[current]
            opposite_label = 'evil' if current_label == 'good' else 'good'
            for neighbor in graph.neighbors(current):
                if neighbor in labels:
                    if labels[neighbor] != opposite_label:
                        return None
                else:
                    labels[neighbor] = opposite_label
                    queue.append(neighbor)
    
    return labels
    
