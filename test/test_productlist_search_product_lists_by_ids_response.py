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

from product-list.models.productlist_search_product_lists_by_ids_response import ProductlistSearchProductListsByIdsResponse

class TestProductlistSearchProductListsByIdsResponse(unittest.TestCase):
    """ProductlistSearchProductListsByIdsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductlistSearchProductListsByIdsResponse:
        """Test ProductlistSearchProductListsByIdsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductlistSearchProductListsByIdsResponse`
        """
        model = ProductlistSearchProductListsByIdsResponse()
        if include_optional:
            return ProductlistSearchProductListsByIdsResponse(
                results = [
                    product-list.models.productlist_product_list_entity.productlistProductListEntity(
                        id = '', 
                        code = '', 
                        url_key = product-list.models.productlist_localized_text.productlistLocalizedText(
                            value = {
                                'key' : ''
                                }, ), 
                        entity_type = '', 
                        entity_code = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        attributes = {
                            'key' : {
                                'key' : None
                                }
                            }, 
                        count_associations = 56, )
                    ]
            )
        else:
            return ProductlistSearchProductListsByIdsResponse(
        )
        """

    def testProductlistSearchProductListsByIdsResponse(self):
        """Test ProductlistSearchProductListsByIdsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
