from simpleai.search import (SearchProblem , 
                             astar,breadth_first,
                             depth_first,uniform_cost,
                             greedy,viewers)
ALGORITMOS_VALIDOS = [astar, breadth_first, depth_first, uniform_cost, greedy]

class Exploracion_Robotica(SearchProblem):
    def __init__(self, initial_state=None):
        super().__init__(initial_state=initial_state)

    def actions(self, state):
        return super().actions(state)
    def cost(self, state, action, state2):
        return super().cost(state, action, state2)
    def heuristic(self, state):
        return super().heuristic(state)
    def result(self, state, action):
        return super().result(state, action)
    def is_goal(self, state):
        return super().is_goal(state)
    

