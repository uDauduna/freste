import unittest
from freste.model.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_a = Room(name="Room 101", capabilities={"General"})
        self.room_b = Room(name="Room")
        self.room_b_id = self.room_b.id

    def test_room_name(self):
        self.assertEqual(self.room_a.name, "Room 101")

    def test_different_room(self):
        self.assertNotEqual(self.room_a, self.room_b)

    def test_room_id(self):
        self.assertNotEqual(self.room_a.id, self.room_b.id)

    def test_id_does_not_change(self):
        self.room_b.name = "Room 102"
        self.assertEqual(self.room_b.id, self.room_b_id)

    def test_room_capabilities(self):
        self.assertEqual(self.room_a.capabilities, {"General"})
    
    def test_default_capabilties(self):
        self.assertEqual(self.room_b.capabilities, set())

    def test_capabilities_are_independent(self):
        self.room_b.capabilities.add("Computer Lab")
        self.assertNotIn("Computer Lab", self.room_a.capabilities)

    def test_id_is_string(self):
        self.assertIsInstance(self.room_a.id, str)

if __name__ == "__main__":
    unittest.main()