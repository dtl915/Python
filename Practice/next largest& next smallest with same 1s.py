# %load test_get_next_largest.py
import unittest


class TestBits(unittest.TestCase):

    def test_get_next_largest(self):
        bits = Bits()
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        self.assertEqual(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        bits = Bits()

        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        self.assertEqual(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()

class Bits(object):
    def number_of_ones(self,num):
        number=0
        while True:
            if num%2==1:
                number+=1
            elif num==0:
                break
            num=num//2
        return number
                
    def get_next_largest(self, num):
        # TODO: Implement me
        number=self.number_of_ones(num)
        while True:
            num+=1
            if self.number_of_ones(num)==number:
                return num

    def get_next_smallest(self, num):
        number=self.number_of_ones(num)
        while True:
            num-=1
            if self.number_of_ones(num)==number:
                return num


if __name__ == '__main__':
    main()