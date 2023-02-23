#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these test if the storage is not db
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not fs")
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.storage

    def test_user(self):
        """ Tests user """
        user = User(name="Makuo")
        self.assertEqual(user.name, "Makuo")

    def test_city(self):
        """ test user """
        city = City(name="Maradi")
        state = State()
        city.state_id = state.id
        self.assertEqual(city.name, "Maradi")

    def test_state(self):
        """ test state"""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_place(self):
        """ test place """
        place = Place(name="Palace", number_rooms=4)
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "Palace")

    def test_amenity(self):
        """ test amenity """
        amenity = Amenity(name="Startlink")
        self.assertTrue(amenity.name, "Startlink")

    def test_review(self):
        """ test review """
        review = Review(text="no comment")
        self.assertEqual(review.text, "no comment")
