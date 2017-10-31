class Node:
    
    def __init__(self, n_id, val, neighbors = []):
        self.id = n_id
        self.val = val
        self.neighbors = neighbors

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors
