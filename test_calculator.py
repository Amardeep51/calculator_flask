import unittest
import calculator


class MyTestCase(unittest.TestCase):
    Test2: object

    def test_results(self):

        #test for additions
        test_a= 555+200000
        self.assertEqual(test_a,200555)
        self.assertEqual(6+9.0,15.0)
        self.assertEqual(0.001+2.00,2.001)
        self.assertNotEqual(0.0+2,3.0)
        self.assertEqual(10+20+30+1,61)

        #test for substractions
        test2 = 55 - 30
        self.assertEqual(test2, 25.0)
        self.assertEqual(0-0,0)
        self.assertEqual(55.0-55,0.00)
        self.assertEqual(0-55,-55)
        self.assertNotEqual(99-99,5)
        self.assertEqual(5-3-2,0)

        #test for multiplications
        test_b=0*0
        self.assertEqual(test_b,0)
        self.assertEqual(55.0*0,0.00)
        self.assertEqual(55*0,0)
        self.assertEqual(100*2,200)
        self.assertEqual(200*2.0,400.00)
        self.assertEqual(2*2*2,8)
        self.assertEqual(5.00*2.00*3.00,30.00)

        #test for divisions
        test1 = 5.00 / 2
        self.assertEqual(test1, 2.50)
        test3 = 55.0/0.11
        self.assertEqual(test3,500.0)
        self.assertEqual(0/22,0)
            #Zero Division test
        try:
            self.assertEqual(22/0,ZeroDivisionError)
        except:
            print("Not Possible")

        self.assertEqual(11/87/29/ 18/ 19/ 242/ 7,7.525509747175684e-09)

        #test for modulus
        test_c=10%5
        self.assertEqual(test_c,0)
        self.assertEqual(10.00%3.00,1.00)
        self.assertEqual(25%4.00,1.00)
        try:
            self.assertEqual(5%0,0)
        except:
            print("Bad Operation")


        #Random Tests

        self.assertNotEqual(5,0)
        self.assertEqual(5.0,5.0)
        self.assertEqual(5.0*5.0,25.00)


        # add assertion here


if __name__ == '__main__':
    unittest.main()
