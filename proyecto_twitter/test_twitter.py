import unittest

from Twitter import AuthenticationManager, TwitterApp

class TestAuthenticationManager(unittest.TestCase):
    def setUp(self):
        self.manager = AuthenticationManager()

    def test_register_user(self):
        user = self.manager.register("Juan", "Contraseña", "2")
        self.assertEqual(user.username, "Juan")
        self.assertEqual(user.password, "Contraseña")
        self.assertFalse(user.superUser)
        print("Prueba exitosa")

    def test_successful_login(self):
        user = self.manager.register("Kevin", "Kevin123", "2")
        logged_user = self.manager.login("Kevin", "Kevin123")
        self.assertEqual(logged_user, user)
        print("Prueba exitosa")

    def test_invalid_credentials_login(self):
        user = self.manager.register("Reynaldo", "contraseña", "2")
        logged_user = self.manager.login("John", "ContraseñaIncorrecta")
        self.assertIsNone(logged_user)
        print("Prueba exitosa")


if __name__ == "__main__":
    unittest.main()