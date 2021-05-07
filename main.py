
import myBfs
import myNode

node_list = myNode.Node.get_random_list(1000, 3, 1)
bfs_alg = myBfs.Bfs(node_list, node_list[5])
size, string = bfs_alg.find(node_list[3])
print("size : ", size, "   | chain : ", string)
size, nodes = bfs_alg.get_biggest_path()
size, string = bfs_alg.find(nodes[0])
print("size : ", size, "   | chain : ", string)

