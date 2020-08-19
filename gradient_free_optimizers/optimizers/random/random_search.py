# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from ..base_optimizer import BaseOptimizer
from ...search import Search


class RandomSearchOptimizer(BaseOptimizer, Search):
    def __init__(self, search_space):
        super().__init__(search_space)

    def iterate(self):
        return self.move_random()

