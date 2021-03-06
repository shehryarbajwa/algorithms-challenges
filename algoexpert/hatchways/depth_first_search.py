

# Sample Input

# graph = A
#       / |  \
#      B  C   D
#     / \    /  \
#    E   F  G    H
# After DFS - [A,B,E,F,C,D,G,H]

#Time Complexity O(V + E) O(V) for adding each vertex to the array. O(V) for the amount of times we have to traverse the children Nodes
#Space Complexity O(V) for adding DFS to the call stack for each vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(Node(child))

    def depth_first_search(self, array):
        array.append(self.name)

        for child in self.children:
            child.depth_first_search(array)

        return array

#                                           A
#                                          / \
#                                         B   C
#                                        /     \
#                                       E       D



node1 = Node('A')
node1.add_child('B')
node1.add_child('C')
node1.children[0].add_child('E')
node1.children[1].add_child('D')
print(node1.depth_first_search([]))

