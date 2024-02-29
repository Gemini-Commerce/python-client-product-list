# coding: utf-8

"""
    Collection Service

    API for managing collection

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from product-list.models.productlist_search_product_lists_by_ids_request import ProductlistSearchProductListsByIdsRequest

class TestProductlistSearchProductListsByIdsRequest(unittest.TestCase):
    """ProductlistSearchProductListsByIdsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistSearchProductListsByIdsRequest:
        """Test ProductlistSearchProductListsByIdsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistSearchProductListsByIdsRequest`
        """
        model = ProductlistSearchProductListsByIdsRequest()
        if include_optional:
            return ProductlistSearchProductListsByIdsRequest(
                tenant_id = '',
                ids = [
                    ''
                    ],
                page_size = 56,
                page_number = 56
            )
        else:
            return ProductlistSearchProductListsByIdsRequest(
        )
        """

    def testProductlistSearchProductListsByIdsRequest(self):
        """Test ProductlistSearchProductListsByIdsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()