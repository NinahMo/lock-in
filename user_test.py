import unittest
from user import User

class Testuser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Richard Ronald","KING","rontheking44@gmail.com","164534")
    
    def test_init(self):
        self.assertEqual(self.new_user.full_name,"Richard Ronald")
        self.assertEqual(self.new_user.login_name,"KING")
        self.assertEqual(self.new_user.email,"rontheking44@gmail.com")
        self.assertEqual(self.new_user.password_value,"164534")
                
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    

if __name__ == '__main__':
    unittest.main()