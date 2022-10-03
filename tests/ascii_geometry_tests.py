import unittest
from ascii_geometry import AsciiContext


class AsciiContextTest(unittest.TestCase):

    def test_triangle_hashtag_output(self):
        """Test for a '#' triangle of height 3"""

        expected_output = """  #  
 ### 
#####
"""

        actual_output = AsciiContext('#').get_triangle(3)

        self.assertEqual(expected_output, actual_output)

    def test_triangle_zero_output(self):
        """Test for a '0' triangle of height 10"""

        expected_output = """         0         
        000        
       00000       
      0000000      
     000000000     
    00000000000    
   0000000000000   
  000000000000000  
 00000000000000000 
0000000000000000000
"""

        actual_output = AsciiContext('0').get_triangle(10)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
