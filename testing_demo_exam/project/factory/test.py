from project.pet_shop import PetShop
from unittest import TestCase, main

class TestPetShopClass(TestCase):
    def setUp(self):
        self.petshop = PetShop("Sara")
    def test_init(self):

        self.assertEqual("Sara",self.petshop.name)
        self.assertEqual(self.petshop.food, {})
        self.assertEqual([],self.petshop.pets)

    def test_init_again(self):
        self.assertEqual(self.petshop.food, {})
    def test_init_pets_attribute(self):
        self.assertEqual([],self.petshop.pets)

    def test_add_negative_food_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food("grain", -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_if_food_dict_empty(self):

        self.assertEqual(self.petshop.food,{})
    def test_if_name_not_in_food(self):
        self.assertEqual(self.petshop.food,{})
        result = self.petshop.add_food("grain", 10)
        self.assertEqual(self.petshop.food, {"grain":10})
        self.assertEqual("Successfully added 10.00 grams of grain.", result)


    def test_adding_a_new_pet(self):
        self.petshop.pets = ["dog","cat"]
        result = self.petshop.add_pet("horse")
        self.assertIn("horse",self.petshop.pets)
        self.assertEqual(self.petshop.pets,["dog","cat","horse"])
        self.assertEqual("Successfully added horse.",result)

    def test_add_same_pet(self):
        self.petshop.add_pet("dog")
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet("dog")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))



    def test_pet_name_not_in_list(self):
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet("granula", "Richie")
        self.assertEqual("Please insert a valid pet name",str(ex.exception))

    def test_feed_pet_unexisting_food(self):
        self.petshop.add_food("grain", 6)
        self.petshop.add_pet("Kiro")
        result = str(self.petshop.feed_pet("banana", "Kiro"))
        self.assertEqual("You do not have banana", result)

    def test_if_food_less_than_100(self):
        self.petshop.add_pet("Miron")
        self.petshop.add_food("grain", 40)
        result = str(self.petshop.feed_pet("grain","Miron"))
        self.assertEqual("Adding food...",result)
        self.assertEqual(1040, self.petshop.food["grain"])

    def test_proper_quantity_and_successful_feed(self):
        self.petshop.add_pet("Miron")
        self.petshop.add_food("meat", 120)
        result = str(self.petshop.feed_pet("meat","Miron"))
        self.assertEqual(20, self.petshop.food["meat"])
        self.assertEqual("Miron was successfully fed", result)

    def test_represent(self):
        self.petshop.add_pet("Miron")
        self.petshop.add_pet("Kiro")
        result = str(self.petshop)
        self.assertEqual(f"Shop Sara:\nPets: Miron, Kiro", result)


if __name__ == '__main__':
    main()

