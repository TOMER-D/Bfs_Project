class Bfs:
    def __init__(self, user_node_list, user_center_node):
        self.node_list = []
        for node in user_node_list:
            self.node_list.append(node)
        self.center_node = self.node_list[user_center_node.get_num_index()]
        self.__start()

    def __start(self):
        self.__init_the_nodes()
        self.center_node.set_dist(0)
        queue = [self.center_node]
        self.center_node.set_isUsed(True)
        self.center_node.set_dist(0)
        while len(queue) > 0:
            item = queue[0]
            queue.remove(item)
            if item.get_list_size() == 0:
                continue
            temp_list = item.get_list()
            for child in temp_list:
                if child.get_isUsed():
                    continue
                child.set_prev(item.get_num_index())
                child.set_isUsed(True)
                child.set_dist(item.get_dist() + 1)
                queue.append(child)

    def __init_the_nodes(self):
        for node in self.node_list:
            node.isUsed = False
            node.set_prev(-1)

    def find(self, item):
        if item.get_prev() == -1:
            if item == self.center_node:
                return 0, str(item.get_num_index())
            else:
                return -1, str(item.get_num_index())
        length, string = self.find(self.node_list[item.get_prev()])
        length += 1
        string += "->" + str(item.get_num_index())
        return length, string

    def get_biggest_path(self):
        size = 0
        biggest_list = []
        for node in self.node_list:
            temp_size, x = self.find(node)
            if size > temp_size:
                continue
            if size == temp_size:
                biggest_list.append(node)
            else:
                biggest_list.clear()
                biggest_list.append(node)
                size = temp_size
        return size, biggest_list

