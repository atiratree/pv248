from functools import reduce

from data.Person import Person
from data.Score import Score
from util.Utils import Utils


class Composer(Person):
    def __init__(self, conn, id, name, born, died, scores=None):
        super().__init__(conn, id, name, born, died)
        self.scores = [] if scores is None else scores

    def __str__(self):
        return reduce(Utils.indentation, self.scores,
                      Utils.indentation(super(Composer, self).__str__(), Score.str_metadata()))
