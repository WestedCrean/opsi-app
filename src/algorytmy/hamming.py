from src.algorytmy.abstractAlgorithm import AbstractAlgorithm


class Hamming(AbstractAlgorithm):
    def __init__(self):
        self.key = 0x18005  # TODO
        self.key_length = 16

    def set_key_length(self, kl):
        if kl in [12,16,32]:
            self.key_length = kl

    def encode(self, data):
        length = len(data)
        i = 0
        redundancy = 0
        summ = 0

        while(i < length):
            if(2**redundancy - 1 == summ):
                redundancy += 1
            else:
                i += 1
        
        coded_data = []

        mask = 0
        redundancy = 0
        i = 0
        summ = 0
        
        while(i < length):
            if(2**redundancy - 1 == summ):
                redundancy += 1
            else:
                coded_data[summ] = data[i]
                mask ^= summ + 1 if data[i] == 1
                i += 1
            summ += 1

        redundancy = 0

        for j in range(0, summ):
            if(2**redundancy - 1 == j):
                if (mask & ( 1 << redundancy)) == 0:
                    coded_data[i] = 0
                else:
                    coded_data[i] = 1

        return coded_data

    def decode(self, encoded_data):
        length = len(encoded_data)
        d = 0
        redundancy = 0

        for i in range(0, length):
            if (2**redundancy - 1 != i):
                d += 1
            else:
                redundancy += 1
        
        decoded_data = []
        d = 0
        redundancy = 0
        for i in range(0, length):
            if (2**redundancy - 1 != i):
                decoded_data[d] = encoded_data[i]
                d += 1
            else:
                redundancy += 1
        
        return decoded_data

    def correction(self, encoded_data):
        length = len(encoded_data)
        d = 0
        redundancy = 0
        errors = 0

        decoded_data = encoded_data.copy()

        for i in range(0, length):
            if (2**redundancy - 1 != i):
                d += 1
            else:
                redundancy += 1
        
        data = []

        mask = 0
        d = 0
        redundancy = 0

        bit_type = []

        for i in range(0, length):
            if(decoded_data[i] == 1):
                mask ^= i + 1
            
            if(2**redundancy - 1 != i):
                d += 1
                bit_type[i] = 0
            else:
                bit_type[i] = 3
                redundancy += 1

        if (mask != 0):
            errors += 1
            num = mask - 1

            if num < len(decoded_data):
                if (bit_type[num] == 0):
                    bit_type[num] = 1 
                elif (bit_type[num] == 3):
                    bit_type[num] = 4

                if (decoded_data[num]==1):
                    decoded_data[num] = 0
                else:
                    decoded_data[num] = 1

             




