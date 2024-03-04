# product-list
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-product-list.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-product-list.git`)

Then import the package:
```python
import product-list
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import product-list
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import product-list
from product-list.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://product-list.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = product-list.Configuration(
    host = "https://product-list.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with product-list.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product-list.ProductListApi(api_client)
    body = product-list.ProductlistCreateProductListRequest() # ProductlistCreateProductListRequest | 

    try:
        # Create Collection
        api_response = api_instance.create_product_list(body)
        print("The response of ProductListApi->create_product_list:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductListApi->create_product_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://product-list.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProductListApi* | [**create_product_list**](docs/ProductListApi.md#create_product_list) | **POST** /productlist.ProductList/CreateProductList | Create Collection
*ProductListApi* | [**create_product_list_association**](docs/ProductListApi.md#create_product_list_association) | **POST** /productlist.ProductList/CreateProductListAssociation | Create Collection/Product Association
*ProductListApi* | [**delete_product_list**](docs/ProductListApi.md#delete_product_list) | **POST** /productlist.ProductList/DeleteProductList | Delete Collection
*ProductListApi* | [**delete_product_list_association**](docs/ProductListApi.md#delete_product_list_association) | **POST** /productlist.ProductList/DeleteProductListAssociation | Delete Collection/Product Association
*ProductListApi* | [**get_product_list_associations_by_product_grn**](docs/ProductListApi.md#get_product_list_associations_by_product_grn) | **POST** /productlist.ProductList/GetProductListAssociationsByProductGrn | Get Collection/Product Associations by Product GRN
*ProductListApi* | [**get_product_list_by_code**](docs/ProductListApi.md#get_product_list_by_code) | **POST** /productlist.ProductList/GetProductListByCode | Get Collection by Code
*ProductListApi* | [**get_product_list_by_id**](docs/ProductListApi.md#get_product_list_by_id) | **POST** /productlist.ProductList/GetProductListById | Get Collection by Id
*ProductListApi* | [**get_product_list_by_url_key**](docs/ProductListApi.md#get_product_list_by_url_key) | **POST** /productlist.ProductList/GetProductListByUrlKey | Get Collection by Url Key
*ProductListApi* | [**get_product_lists_count**](docs/ProductListApi.md#get_product_lists_count) | **POST** /productlist.ProductList/GetProductListsCount | Get Collection Product Count
*ProductListApi* | [**list_product_list_associations**](docs/ProductListApi.md#list_product_list_associations) | **POST** /productlist.ProductList/ListProductListAssociations | List Collection/Product Associations
*ProductListApi* | [**list_product_lists**](docs/ProductListApi.md#list_product_lists) | **POST** /productlist.ProductList/ListProductLists | List Collections
*ProductListApi* | [**product_list_bulk_update_product_list_associations**](docs/ProductListApi.md#product_list_bulk_update_product_list_associations) | **POST** /productlist.ProductList/BulkUpdateProductListAssociations | 
*ProductListApi* | [**search_product_lists**](docs/ProductListApi.md#search_product_lists) | **POST** /productlist.ProductList/SearchProductLists | Search Collections
*ProductListApi* | [**search_product_lists_by_ids**](docs/ProductListApi.md#search_product_lists_by_ids) | **POST** /productlist.ProductList/SearchProductListsByIds | Search Collections by Ids
*ProductListApi* | [**set_product_list_associations**](docs/ProductListApi.md#set_product_list_associations) | **POST** /productlist.ProductList/SetProductListAssociations | Set Collection/Product Associations
*ProductListApi* | [**update_product_list**](docs/ProductListApi.md#update_product_list) | **POST** /productlist.ProductList/UpdateProductList | Update Collection


## Documentation For Models

 - [OrderByDirection](docs/OrderByDirection.md)
 - [ProductlistBulkUpdateProductListAssociationsRequest](docs/ProductlistBulkUpdateProductListAssociationsRequest.md)
 - [ProductlistBulkUpdateProductListAssociationsRequestProductListAssociation](docs/ProductlistBulkUpdateProductListAssociationsRequestProductListAssociation.md)
 - [ProductlistCreateProductListAssociationRequest](docs/ProductlistCreateProductListAssociationRequest.md)
 - [ProductlistCreateProductListAssociationResponse](docs/ProductlistCreateProductListAssociationResponse.md)
 - [ProductlistCreateProductListRequest](docs/ProductlistCreateProductListRequest.md)
 - [ProductlistCreateProductListResponse](docs/ProductlistCreateProductListResponse.md)
 - [ProductlistDeleteProductListAssociationRequest](docs/ProductlistDeleteProductListAssociationRequest.md)
 - [ProductlistDeleteProductListAssociationResponse](docs/ProductlistDeleteProductListAssociationResponse.md)
 - [ProductlistDeleteProductListRequest](docs/ProductlistDeleteProductListRequest.md)
 - [ProductlistDeleteProductListResponse](docs/ProductlistDeleteProductListResponse.md)
 - [ProductlistGetProductListAssociationsByProductGrnRequest](docs/ProductlistGetProductListAssociationsByProductGrnRequest.md)
 - [ProductlistGetProductListAssociationsByProductGrnResponse](docs/ProductlistGetProductListAssociationsByProductGrnResponse.md)
 - [ProductlistGetProductListByCodeRequest](docs/ProductlistGetProductListByCodeRequest.md)
 - [ProductlistGetProductListByCodeResponse](docs/ProductlistGetProductListByCodeResponse.md)
 - [ProductlistGetProductListByIdRequest](docs/ProductlistGetProductListByIdRequest.md)
 - [ProductlistGetProductListByIdResponse](docs/ProductlistGetProductListByIdResponse.md)
 - [ProductlistGetProductListByUrlKeyRequest](docs/ProductlistGetProductListByUrlKeyRequest.md)
 - [ProductlistGetProductListByUrlKeyResponse](docs/ProductlistGetProductListByUrlKeyResponse.md)
 - [ProductlistGetProductListsCountRequest](docs/ProductlistGetProductListsCountRequest.md)
 - [ProductlistGetProductListsCountResponse](docs/ProductlistGetProductListsCountResponse.md)
 - [ProductlistListProductListAssociationsRequest](docs/ProductlistListProductListAssociationsRequest.md)
 - [ProductlistListProductListAssociationsResponse](docs/ProductlistListProductListAssociationsResponse.md)
 - [ProductlistListProductListsRequest](docs/ProductlistListProductListsRequest.md)
 - [ProductlistListProductListsResponse](docs/ProductlistListProductListsResponse.md)
 - [ProductlistLocalizedText](docs/ProductlistLocalizedText.md)
 - [ProductlistOrderBy](docs/ProductlistOrderBy.md)
 - [ProductlistProductListAssociation](docs/ProductlistProductListAssociation.md)
 - [ProductlistProductListAssociationError](docs/ProductlistProductListAssociationError.md)
 - [ProductlistProductListEntity](docs/ProductlistProductListEntity.md)
 - [ProductlistProductListError](docs/ProductlistProductListError.md)
 - [ProductlistSearchProductListsByIdsRequest](docs/ProductlistSearchProductListsByIdsRequest.md)
 - [ProductlistSearchProductListsByIdsResponse](docs/ProductlistSearchProductListsByIdsResponse.md)
 - [ProductlistSearchProductListsRequest](docs/ProductlistSearchProductListsRequest.md)
 - [ProductlistSearchProductListsResponse](docs/ProductlistSearchProductListsResponse.md)
 - [ProductlistSetProductListAssociationsRequest](docs/ProductlistSetProductListAssociationsRequest.md)
 - [ProductlistSetProductListAssociationsResponse](docs/ProductlistSetProductListAssociationsResponse.md)
 - [ProductlistUpdateProductListRequest](docs/ProductlistUpdateProductListRequest.md)
 - [ProductlistUpdateProductListResponse](docs/ProductlistUpdateProductListResponse.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [SearchProductListsRequestQuery](docs/SearchProductListsRequestQuery.md)
 - [SetProductListAssociationsRequestAssociation](docs/SetProductListAssociationsRequestAssociation.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


