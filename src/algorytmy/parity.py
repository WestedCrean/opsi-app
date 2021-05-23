from src.algorytmy.abstractAlgorithm import AbstractAlgorithm


class Parity(AbstractAlgorithm):
    def __init__(self):
        self.key = 0x18005  # TODO
        self.key_length = 16

    def set_key_length(self, kl):
        if kl in [12, 16, 32]:
            self.key_length = kl

    def encode(self, encoded_message):
        ones = 0
        for ch in encoded_message:
            if ch == "1":
                ones += 1
        if ones % 2 == 0:
            return "0" + encoded_message
        else:
            return "1" + encoded_message

    def decode(self, message_with_parity_bit, disturbed_message):
        disturbed_message = self.encode(disturbed_message)
        message = message_with_parity_bit[1:]
        result = self.encode(message)
        return disturbed_message[0] == result[0]

    def correction(self):
        pass
