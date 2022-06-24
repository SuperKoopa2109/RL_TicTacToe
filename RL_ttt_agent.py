import itertools
import numpy as np

class MCT():
    size = 0

    def __init__(self):
        self.add_root()
        pass

    def add_root(self) -> object:
        Node()
        pass

    def add_Node(self, parent_node: object = None) -> object:
        if parent_node == None:
            return 'error'
        new_node = Node(parent_node = parent_node)
        parent_node.add_subnode(new_node)
        return new_node

    def get_size(self):
        return self.size

class Node():
    def __init__(self, node_id: int = 0, val: int = 0, subnode_count: int = 0, subnodes: object = None, parent_node: object = None) -> None:
        self.node_id = node_id
        self.val = val
        self.subnode_count = subnode_count

        if subnodes == None:
            subnodes = []
        self.subnodes = subnodes

        self.parent_node = parent_node
    
    def get_value(self) -> int:
        return self.val

    def get_subnode_count(self) -> int:
        return self.subnode_count

    def get_subnodes(self) -> object:
        return self.subnodes

    def get_subnode(self, idx: int) -> object:
        return self.subnodes[idx]

    def add_subnode(self, node: object) -> object:
        self.subnodes.append(node)
        print(f"""subnode count first: {self.subnode_count}""")
        self.subnode_count += 1
        print(f"""subnode count after: {self.subnode_count}""")
        return self.subnodes

    def is_leaf_node(self) -> bool:
        return True if self.val == 0 and self.subnode_count == 0 else False

class Agent():
    Q = {} # Q Values
    A = {} # Actions
    S = {} # States
    R = {} # Rewards
    discount = 1 # discount
    learning_rate = 0.1 # This is the variable for the learning rate.
    decay = 5000
    exploration = 0
    continuous = False
    showUI = True
    max_score = 0

    curr_state = ()
    prev_state = ()
    last_action = ()

    def __init__(self, agent_type: str = 'TTT', train_type: str = 'MCTS', R: object = None, continuous: bool = True, showUI: bool = True) -> None:
        if agent_type == 'TTT':
            if train_type == 'MCTS':
                self.MCT = []
            
            print('Tic Tac Toe Agent has been released.')
            self.A = [(x, y) for x in range(3) for y in range(3)]
            self.S = {}

            if R == None:
                self.R = {'win': 1, 'lose': -1}
            else:
                self.R = R 
            self.continuous = continuous
            self.showUI = showUI
            self.curr_state = ()


class TTT_Agent(Agent):
    def __init__(self) -> None:
        super().__init__('TTT')

        self.MCT.append(self.get_initial_leaf())

        if self.MCT[0].get_subnode_count() == 0:
            self.MCT[0].subnodes.append(self.get_initial_leaf(parent_node = self.MCT[0]))
            self.MCT[0].subnodes.append(self.get_initial_leaf(parent_node = self.MCT[0]))

    def getActions(self) -> None:
        print(self.A)

    def get_initial_leaf(self, parent_node: object = None) -> object:
        return Node(parent_node = parent_node) #{'node_id': 0, 'val': 0, 'subnode_count': 0, 'subnodes': []}

    def get_ucb1(self, node: object, total_nodes: int) -> int:
        return node.get_value() + 2 * np.sqrt(np.log(total_nodes) / node.get_subnode_count() ) if total_nodes != 0 else 99999 #V[i] + 2 * np.sqrt(np.log(N)/ N[i])

    def get_multi_ucb1(self, nodes: object, total_nodes: int) -> object:
        for node in nodes:
            print(node)
            print(node.get_subnode_count())
        return [node.get_value() + 2 * np.sqrt(np.log(total_nodes) / node.get_subnode_count() ) if total_nodes != 0 else 99999 for node in nodes]
    
    def iterate(self) -> None:
        root = self.MCT[0]
        
        if root.get_subnode_count() == 0:
            root.add_subnode(self.get_initial_leaf(parent_node = root))
            root.add_subnode(self.get_initial_leaf(parent_node = root))

        total_nodes = root.get_subnode_count()

        #ucb1_val_left = self.get_ucb1(root.get_subnode(0), total_nodes)
        #ucb1_val_right = self.get_ucb1(root.get_subnode(1), total_nodes)
        
        print(self.get_multi_ucb1(root.get_subnodes(), total_nodes))

        chosen_idx = np.argmax(self.get_multi_ucb1(root.get_subnodes(), root.get_subnode_count()))  #np.argmax([ucb1_val_left, ucb1_val_right])

        current_node = root.get_subnode(chosen_idx)

        while True:
            
            if current_node.is_leaf_node():
                return self.rollout(current_node)

            # If current node does not have subnodes and is no leaf node -> create subnodes.
            if current_node.get_subnode_count() == 0:
                current_node.add_subnode(self.get_initial_leaf(parent_node = current_node))
                current_node.add_subnode(self.get_initial_leaf(parent_node = current_node))

            chosen_idx = np.argmax(self.get_multi_ucb1(current_node.get_subnodes(), current_node.get_subnode_count()))

            current_node = current_node.get_subnode(chosen_idx)
            

    def rollout(self, node):
        return 10

ttt_agnt = TTT_Agent()

ttt_agnt.getActions()

ttt_agnt.iterate()
    