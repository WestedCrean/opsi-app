from abc import ABC, abstractmethod

class AbstractAlgorithm(ABC):

    @abstractmethod
    def output(self):
        pass