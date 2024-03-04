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

from product-list.models.productlist_get_product_list_associations_by_product_grn_response import ProductlistGetProductListAssociationsByProductGrnResponse

class TestProductlistGetProductListAssociationsByProductGrnResponse(unittest.TestCase):
    """ProductlistGetProductListAssociationsByProductGrnResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistGetProductListAssociationsByProductGrnResponse:
        """Test ProductlistGetProductListAssociationsByProductGrnResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistGetProductListAssociationsByProductGrnResponse`
        """
        model = ProductlistGetProductListAssociationsByProductGrnResponse()
        if include_optional:
            return ProductlistGetProductListAssociationsByProductGrnResponse(
                associations = [
                    product-list.models.productlist_product_list_association.productlistProductListAssociation(
                        id = '', 
                        list_id = '', 
                        position = 56, 
                        product_grn = '', )
                    ]
            )
        else:
            return ProductlistGetProductListAssociationsByProductGrnResponse(
        )
        """

    def testProductlistGetProductListAssociationsByProductGrnResponse(self):
        """Test ProductlistGetProductListAssociationsByProductGrnResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
