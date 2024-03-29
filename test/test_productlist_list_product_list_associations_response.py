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

from product-list.models.productlist_list_product_list_associations_response import ProductlistListProductListAssociationsResponse

class TestProductlistListProductListAssociationsResponse(unittest.TestCase):
    """ProductlistListProductListAssociationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistListProductListAssociationsResponse:
        """Test ProductlistListProductListAssociationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistListProductListAssociationsResponse`
        """
        model = ProductlistListProductListAssociationsResponse()
        if include_optional:
            return ProductlistListProductListAssociationsResponse(
                associations = [
                    product-list.models.productlist_product_list_association.productlistProductListAssociation(
                        id = '', 
                        list_id = '', 
                        position = 56, 
                        product_grn = '', )
                    ],
                next_page_token = ''
            )
        else:
            return ProductlistListProductListAssociationsResponse(
        )
        """

    def testProductlistListProductListAssociationsResponse(self):
        """Test ProductlistListProductListAssociationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
