import random
import numpy

wall_patterns = [[[0,0,0,0,0,0,0,0,0,0],
                 [0,1,0,0,0,0,0,0,0,0],
                 [0,0,1,0,0,0,0,0,0,0],
                 [0,0,0,1,0,0,0,0,0,0],
                 [0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,1,0,0,0,0],
                 [0,0,0,0,0,0,1,0,0,0],
                 [0,0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,0,1,0],
                 [0,0,0,0,0,0,0,0,0,0]
                ],
                [[0,0,0,0,0,0,0,0,0,0],
                 [0,1,1,1,1,1,1,1,1,0],
                 [0,0,1,0,0,0,0,1,0,0],
                 [0,0,0,1,0,0,1,0,0,0],
                 [0,0,0,0,1,1,0,0,0,0],
                 [0,0,0,0,1,1,0,0,0,0],
                 [0,0,0,1,0,0,1,0,0,0],
                 [0,0,1,0,0,0,0,1,0,0],
                 [0,1,0,0,0,0,0,0,1,0],
                 [0,0,0,0,0,0,0,0,0,0]
                ],
                [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]
                ],
                [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,1,1,0,0,1,1],
                 [1,0,1,0,1,1,0,1,0,1],
                 [1,0,0,1,1,1,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,1,1,1,1,0,0,1],
                 [1,0,1,0,1,1,0,1,0,1],
                 [1,1,0,0,1,1,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]
                ],
                [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,1,1,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,1,1,1,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,1,1,1,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,1,1,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]
                ]
                ]

def get_random_wallpattern():
    return wall_patterns[random.randrange(len(wall_patterns))]

def make_random_wallpatterns():
    return numpy.random.randint(2,size=(10,10))