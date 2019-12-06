import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_expected_s_and_e(self):
        """
        Test a product whose attributes are changed for correct
        Stealability and Explode method values
        """
        prod = Product('1 ton of Wrought Iron')
        prod.weight = 2000
        prod.flammability = 0

        self.assertEqual(prod.explode(), "...fizzle.")
        self.assertEqual(prod.stealability(), "Not so stealable...")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for x in products:
            adj, noun = x.name.split(' ')
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
