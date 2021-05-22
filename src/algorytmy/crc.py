from src.algorytmy.abstractAlgorithm import AbstractAlgorithm


class Crc(AbstractAlgorithm):
    def __init__(self):
        self.key = 0x18005  # TODO
        self.key_length = 16

    def output(self):
        pass
        # print("test")

    def copy_list(self, src, src_start_idx, dest, dest_start_idx, qty):
        dest = dest[:dest_start_idx] + src[src_start_idx : src_start_idx + qty] + dest[dest_start_idx + qty :]
        return dest

    def count_crc(self, bits):
        n = len(bits)
        crc = [0] * self.key_length
        temp = [0] * (n + self.key_length)
        temp = copy_list(bits, 0, temp, self.key_length, n)
        tkey = []
        for i in range(self.key_length + 1):
            if self.key & (1 << i) == 0:
                tkey.append(0)
            else:
                tkey.append(1)

        for i in range(n + self.key_length - 1, self.key_length - 1, -1):
            if temp[i] == 1:
                for j in range(self.key_length + 1):
                    temp[i - j] = temp[i - j] ^ tkey[self.key_length - j]

        return copy_list(temp, 0, crc, 0, self.key_length)

    # TODO
    # encodeCRC
    def decode_crc(self, coded_data):
        pass
