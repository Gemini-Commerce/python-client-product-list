# coding: utf-8

"""
    Collection Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from product-list.models.productlist_localized_text import ProductlistLocalizedText

class TestProductlistLocalizedText(unittest.TestCase):
    """ProductlistLocalizedText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistLocalizedText:
        """Test ProductlistLocalizedText
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistLocalizedText`
        """
        model = ProductlistLocalizedText()
        if include_optional:
            return ProductlistLocalizedText(
                value = {
                    'key' : ''
                    }
            )
        else:
            return ProductlistLocalizedText(
        )
        """

    def testProductlistLocalizedText(self):
        """Test ProductlistLocalizedText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
