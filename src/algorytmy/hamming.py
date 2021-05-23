from src.algorytmy.abstractAlgorithm import AbstractAlgorithm


class Hamming(AbstractAlgorithm):
    def __init__(self):
        self.key = 0x18005  # TODO
        self.key_length = 16

    def set_key_length(self, kl):
        if kl in [12,16,32]:
            self.key_length = kl

    def encode(self):
        pass

    def decode(self):
        pass

    def correction(self):
        pass