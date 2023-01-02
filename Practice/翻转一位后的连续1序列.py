import unittest


class TestBits(unittest.TestCase):

    def test_flip_bit(self):
        bits = Bits()
        self.assertRaises(TypeError, bits.flip_bit, None)
        self.assertEqual(bits.flip_bit(0), 1)
        self.assertEqual(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        print('Success: test_print_binary')

class Bits(object):
    
    MAX_BITS = 32

    def flip_bit(self, num):
        if num is None:
            raise TypeError
        elif num==-1:
            return self.MAX_BITS
        elif num==0:
            return 1
        else:
            max_consecutive=[]
            for i in range(32):
                temp_num=num
                temp_num=temp_num|2**i
                if temp_num==num:
                    pass
                else:
                    consecutives=0
                    for j in range(32):
                        if temp_num==temp_num|1:
                            consecutives+=1
                            
                        else:
                            max_consecutive.append(consecutives)
                            consecutives=0
                        temp_num=temp_num>>1


            return max(max_consecutive)



def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()
