import unittest

from Tutorial.Polymorphism import Person,Doctor
class MyTestCase(unittest.TestCase):
    def test_inheritance(self):
        doctor = Doctor("James", "Willems")
        self.assertEqual("Dr.James Willems", doctor.printinfo())
        person = Person("Alanah", "Pearce")
        self.assertEqual("Alanah Pearce", person.printinfo())


if __name__ == '__main__':
    unittest.main()
