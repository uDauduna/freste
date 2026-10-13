import unittest
from freste.model.student_group import StudentGroup

class TestStudentGroup(unittest.TestCase):

    def setUp(self):
        self.group_a = StudentGroup(level="Sophomore", section="A")
        self.group_b = StudentGroup(level="Sophomore", section="A")
        self.group_b_id = self.group_b.id

    def test_object_level(self):
        self.assertEqual(self.group_a.level, "Sophomore")

    def test_object_section(self):
        self.assertEqual(self.group_a.section, "A")

    def test_different_student_group(self):
        self.assertNotEqual(self.group_a, self.group_b)

    def test_object_id(self):
        self.assertNotEqual(self.group_a.id, self.group_b.id)

    def test_id_does_not_change(self):
        self.group_b.section = "B"
        self.assertEqual(self.group_b.id, self.group_b_id)

    def test_id_is_string(self):
        self.assertIsInstance(self.group_a.id, str)

    


if __name__ == "__main__":
    unittest.main()