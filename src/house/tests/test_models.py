from unittest import TestCase

from django.db import IntegrityError

from house.models import House


class HouseModelTests(TestCase):

    def test_default_name_is_applied(self):
        weight = 12
        height = 34
        location = "St.California"
        new_house = House.objects.create(weight=weight, height=height, location=location)
        self.assertEqual(new_house.name, "Undefined")

    def test_creation_without_location(self):
        with self.assertRaises(IntegrityError):
            House.objects.create(
                name="ef",
                location=None
            )

    def test_str_method_works_fine(self):
        name = "wergfewr"
        weight = 12
        height = 34
        location = "St.California"
        new_house = House.objects.create(name=name, weight=weight, height=height, location=location)
        self.assertTrue(new_house.__str__() == f"{new_house.name}, {new_house.location}")

    def test_height_weight_method(self):
        name = "wergfewr"
        weight = 12
        height = 34
        location = "St.California"
        new_house = House.objects.create(name=name, weight=weight, height=height, location=location)
        self.assertTrue(f"Height: {new_house.height}, Weight: {new_house.weight}" == new_house.height_weight())

    # def test_house_deleted(self):
    #     name = "House1"
    #     weight = 14
    #     height = 35
    #     location = "California"
    #     House.objects.create(name=name, weight=weight, height=height, location=location)
    #     house2del = House.objects.get(name=name, weight=weight, height=height, location=location)
    #     house2del.delete()
    #     with self.assertRaises(DoesNotExist):  # не знаю как ловить, это же из системыв запросов эрор
    #         House.objects.get(name=name, weight=weight, height=height, location=location)
