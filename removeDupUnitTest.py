# unit test to remove duplicate item from list and sort
import unittest
import removeDup as rd

class RemoveDuplicateInitTest(unittest.TestCase):
    def test_rem_dup(self):
        dup_lst = [2,10,5,1,0,3,2,9,10]
        no_dup_sorted_lst = [0,1,2,3,5,9,10]
        self.assertEqual(rd.remove_dup(dup_lst), no_dup_sorted_lst)

    def test_rem_dup_empty_lst(self):
        dup_lst = []
        no_dup_sorted_lst = []
        self.assertEqual(rd.remove_dup(dup_lst), no_dup_sorted_lst)   
        
    def test_rem_dup_single_item(self):
        dup_lst = [2]
        no_dup_sorted_lst = [2]
        self.assertEqual(rd.remove_dup(dup_lst), no_dup_sorted_lst)   

        
if __name__ == '__main__':
    unittest.main()
