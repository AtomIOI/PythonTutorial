import unittest

from Tutorial.Inheritance import Person, Student


class MyTestCase(unittest.TestCase):
    def test_inheritance(self):
        person = Person("John", "Smith")
        self.assertEqual("John Smith", person.printname())
        student = Student("Adam", "Kovic", 2019)
        self.assertEqual("Adam Kovic", student.printname())
        self.assertEqual(2019, student.graduationyear)



if __name__ == '__main__':
    unittest.main()
