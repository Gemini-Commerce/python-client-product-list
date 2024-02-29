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

from product-list.models.productlist_get_product_list_associations_by_product_grn_request import ProductlistGetProductListAssociationsByProductGrnRequest

class TestProductlistGetProductListAssociationsByProductGrnRequest(unittest.TestCase):
    """ProductlistGetProductListAssociationsByProductGrnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistGetProductListAssociationsByProductGrnRequest:
        """Test ProductlistGetProductListAssociationsByProductGrnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistGetProductListAssociationsByProductGrnRequest`
        """
        model = ProductlistGetProductListAssociationsByProductGrnRequest()
        if include_optional:
            return ProductlistGetProductListAssociationsByProductGrnRequest(
                tenant_id = '',
                product_grn = ''
            )
        else:
            return ProductlistGetProductListAssociationsByProductGrnRequest(
        )
        """

    def testProductlistGetProductListAssociationsByProductGrnRequest(self):
        """Test ProductlistGetProductListAssociationsByProductGrnRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()