import unittest
from freste.model.subject import Subject

class TestSubject(unittest.TestCase):

    def setUp(self):
        self.name = "Mathematics"
        self.subject_a = Subject(name="Mathematics")
        self.subject_b = Subject(name="Mathematics")
        self.subject_b_id = self.subject_b.id

    def test_object(self):
        self.assertIsInstance(self.subject_a, Subject)

    def test_object_name(self):
        self.assertEqual(self.subject_a.name, self.name)

    def test_id_is_string(self):
        self.assertIsInstance(self.subject_a.id, str)

    def test_unique_id(self):
        self.assertNotEqual(self.subject_a.id, self.subject_b.id)

    def test_id_does_not_change(self):
        self.subject_b.name = "Physics"
        self.assertEqual(self.subject_b.id, self.subject_b_id)

if __name__ == "__main__":
    unittest.main()