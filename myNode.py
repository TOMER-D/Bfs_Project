import random


class Node:
    def __init__(self, num, list_size):
        self.num = num
        self.isUsed = False
        self.child_list = [Node]*list_size
        self.cnt = 0
        self.dist = 0
        self.prev = -1

    def get_num_index(self):
        return self.num

    def add_to_list(self, node):
        self.child_list.append(node)

    def set_prev(self, prev_number):
        self.prev = prev_number

    def get_prev(self):
        return self.prev

    def get_list_size(self):
        return len(self.child_list)

    def get_dist(self):
        return self.dist

    def set_dist(self, dist):
        self.dist = dist

    def get_isUsed(self):
        return self.isUsed

    def set_isUsed(self, condition):
        self.isUsed = condition

    def get_list(self):
        return self.child_list

    def add(self, node) -> bool:
        if self.cnt >= len(self.child_list):
            return False
        if isinstance(node, Node):
            if node not in self.child_list and node.num != self.num:
                self.child_list[self.cnt] = node
                self.cnt += 1
        return True

    @staticmethod
    def get_random_list(max_number, max_connections, min_connections):
        node_list = [Node] * max_number
        for i in range(0, max_number):
            size_rnd = random.randint(min_connections, max_connections)
            node_list[i] = Node(i, size_rnd)

        for item in node_list:
            index_rnd = random.randint(0, max_number - 1)
            if isinstance(node_list[index_rnd], Node):
                while True:
                    if not item.add(node_list[index_rnd]):
                        break
                    index_rnd = random.randint(0, max_number - 1)
        return node_list
