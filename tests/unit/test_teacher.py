import unittest
from freste.model.teacher import Teacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.name = "Mike Piontek"
        self.teacher_a = Teacher(name="Mike Piontek")
        self.teacher_b = Teacher(name="Sally Jones")
        self.teacher_b_id = self.teacher_b.id

    def test_object(self):
        self.assertIsInstance(self.teacher_a, Teacher)

    def test_empty_qualifications_by_default(self):
        self.assertEqual(self.teacher_a.qualified_course_ids, set())

    def test_different_qualification_sets(self):
        self.teacher_a.qualified_course_ids.add("MAT101")
        self.assertNotEqual(self.teacher_a.qualified_course_ids, self.teacher_b.qualified_course_ids)

    def test_add_qualification(self):
        self.teacher_a.qualified_course_ids.add("MAT101")
        self.assertIn("MAT101", self.teacher_a.qualified_course_ids)
        self.assertNotIn("MAT101", self.teacher_b.qualified_course_ids)

    def test_object_name(self):
        self.assertEqual(self.teacher_a.name, self.name)

    def test_id_is_string(self):
        self.assertIsInstance(self.teacher_a.id, str)

    def test_unique_id(self):
        self.assertNotEqual(self.teacher_a.id, self.teacher_b.id)

    def test_id_does_not_change(self):
        self.teacher_b.name = "Sally Mae"
        self.assertEqual(self.teacher_b.id, self.teacher_b_id)

if __name__ == "__main__":
    unittest.main()