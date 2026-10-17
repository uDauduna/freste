import unittest
from freste.model.course import Course
from freste.model.subject import Subject

class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course_name = "Mathematics 101"
        self.subject = Subject(name="Mathematics")
        self.course_a = Course(name=self.course_name, subject=self.subject)
        self.course_b = Course(name="Mathematics 102", subject=self.subject)
        self.course_b_id = self.course_b.id


    def test_object_name(self):
        self.assertEqual(self.course_a.name, self.course_name)

    def test_id_is_string(self):
        self.assertIsInstance(self.course_a.id, str)

    def test_subject_is_an_object(self):
        self.assertIs(self.course_a.subject, self.subject)

    def test_courses_share_subject(self):
        self.assertIs(self.course_a.subject, self.course_b.subject)

    def test_unique_id(self):
        self.assertNotEqual(self.course_a.id, self.course_b.id)

    def test_id_does_not_change(self):
        self.course_b.name = "Mathematics 103"
        self.assertEqual(self.course_b.id, self.course_b_id)



if __name__ == "__main__":
    unittest.main()