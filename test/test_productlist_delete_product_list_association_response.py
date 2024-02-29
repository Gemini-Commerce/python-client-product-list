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

from product-list.models.productlist_delete_product_list_association_response import ProductlistDeleteProductListAssociationResponse

class TestProductlistDeleteProductListAssociationResponse(unittest.TestCase):
    """ProductlistDeleteProductListAssociationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistDeleteProductListAssociationResponse:
        """Test ProductlistDeleteProductListAssociationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistDeleteProductListAssociationResponse`
        """
        model = ProductlistDeleteProductListAssociationResponse()
        if include_optional:
            return ProductlistDeleteProductListAssociationResponse(
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
            return ProductlistDeleteProductListAssociationResponse(
        )
        """

    def testProductlistDeleteProductListAssociationResponse(self):
        """Test ProductlistDeleteProductListAssociationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
