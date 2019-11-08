import unittest
from password import Password

class Testpassword(unittest.TestCase):
    def setUp(self):
        self.new_password = Password("Instagram","Lorderonnie","421145")
    
    def tearDown(self):
        Password.password_list = []
    
    def test_init(self):
        self.assertEqual(self.new_password.app_name,"Instagram")
        self.assertEqual(self.new_password.user_name,"Lorderonnie")
        self.assertEqual(self.new_password.password_number,"421145")       
    
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

        
    def test_save_multiple_passwords(self):
        self.new_password.save_password()
        test_password = Password("Instagram","Lorderonnie","421145")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Instagram","Lorderonnie","421145")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)
        
    def test_display_all_contacts(self):
        self.assertEqual(Password.display_passwords(),Password.password_list)
    

if __name__ == '__main__':
    unittest.main()