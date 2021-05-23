from abc import ABC, abstractmethod

class AbstractAlgorithm(ABC):

    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def decode(self):
        pass

    @abstractmethod
    def correction(self):
        pass
