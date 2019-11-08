import unittest
from password import Password

class Testpassword(unittest.TestCase):
    def setUp(self):
        self.new_password = Password("Richard Ronald","Lorderonnie","rontheking45@gmail.com","421145","421145")
    
    def test_init(self):
        self.assertEqual(self.new_password.full_name,"Richard Ronald")
        self.assertEqual(self.new_password.user_name,"Lorderonnie")
        self.assertEqual(self.new_password.email,"rontheking45@gmail.com")
        self.assertEqual(self.new_password.password_number,"421145")
        self.assertEqual(self.new_password.password_confirm,"421145")   
    
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def tearDown(self):
        Password.password_list = []
        
    def test_save_multiple_passwords(self):
        self.new_password.save_password()
        test_password = Password("Richard Ronald","Lorderonnie","rontheking45@gmail.com","421145","421145")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Richard Ronald","Lorderonnie","rontheking45@gmail.com","421145","421145")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)
        
    def 
        
        


if __name__ == '__main__':
    unittest.main()