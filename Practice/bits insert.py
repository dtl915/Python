import unittest


class TestBit(unittest.TestCase):

    def test_insert_m_into_n(self):
        n = int('0000011111111011', base=2)
        m = int('0000000000010011', base=2)
        expected = int('0000011101001111', base=2)
        bits = Bits()
        self.assertEqual(bits.insert_m_into_n(m, n, i=2, j=6), expected)
        print('Success: test_insert_m_into_n')


def main():
    test = TestBit()
    test.test_insert_m_into_n()
class Bits(object):
    
    def insert_m_into_n(self, m, n, i, j):
        insertlen=16-j-i
        m=m&(2**insertlen-1)

        m=m<<i
        x=2**16-1
        for i in range(i,j+2):
            x-=2**i
        n=x&n

        return n|m



if __name__ == '__main__':
    main()