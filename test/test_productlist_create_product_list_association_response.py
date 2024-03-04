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

from product-list.models.productlist_create_product_list_association_response import ProductlistCreateProductListAssociationResponse

class TestProductlistCreateProductListAssociationResponse(unittest.TestCase):
    """ProductlistCreateProductListAssociationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistCreateProductListAssociationResponse:
        """Test ProductlistCreateProductListAssociationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistCreateProductListAssociationResponse`
        """
        model = ProductlistCreateProductListAssociationResponse()
        if include_optional:
            return ProductlistCreateProductListAssociationResponse(
                association = product-list.models.productlist_product_list_association.productlistProductListAssociation(
                    id = '', 
                    list_id = '', 
                    position = 56, 
                    product_grn = '', ),
                errors = [
                    product-list.models.productlist_product_list_association_error.productlistProductListAssociationError(
                        code = '', 
                        message = '', )
                    ]
            )
        else:
            return ProductlistCreateProductListAssociationResponse(
        )
        """

    def testProductlistCreateProductListAssociationResponse(self):
        """Test ProductlistCreateProductListAssociationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
