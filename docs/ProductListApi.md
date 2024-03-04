# product-list.ProductListApi

All URIs are relative to *https://product-list.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_list**](ProductListApi.md#create_product_list) | **POST** /productlist.ProductList/CreateProductList | Create Collection
[**create_product_list_association**](ProductListApi.md#create_product_list_association) | **POST** /productlist.ProductList/CreateProductListAssociation | Create Collection/Product Association
[**delete_product_list**](ProductListApi.md#delete_product_list) | **POST** /productlist.ProductList/DeleteProductList | Delete Collection
[**delete_product_list_association**](ProductListApi.md#delete_product_list_association) | **POST** /productlist.ProductList/DeleteProductListAssociation | Delete Collection/Product Association
[**get_product_list_associations_by_product_grn**](ProductListApi.md#get_product_list_associations_by_product_grn) | **POST** /productlist.ProductList/GetProductListAssociationsByProductGrn | Get Collection/Product Associations by Product GRN
[**get_product_list_by_code**](ProductListApi.md#get_product_list_by_code) | **POST** /productlist.ProductList/GetProductListByCode | Get Collection by Code
[**get_product_list_by_id**](ProductListApi.md#get_product_list_by_id) | **POST** /productlist.ProductList/GetProductListById | Get Collection by Id
[**get_product_list_by_url_key**](ProductListApi.md#get_product_list_by_url_key) | **POST** /productlist.ProductList/GetProductListByUrlKey | Get Collection by Url Key
[**get_product_lists_count**](ProductListApi.md#get_product_lists_count) | **POST** /productlist.ProductList/GetProductListsCount | Get Collection Product Count
[**list_product_list_associations**](ProductListApi.md#list_product_list_associations) | **POST** /productlist.ProductList/ListProductListAssociations | List Collection/Product Associations
[**list_product_lists**](ProductListApi.md#list_product_lists) | **POST** /productlist.ProductList/ListProductLists | List Collections
[**product_list_bulk_update_product_list_associations**](ProductListApi.md#product_list_bulk_update_product_list_associations) | **POST** /productlist.ProductList/BulkUpdateProductListAssociations | 
[**search_product_lists**](ProductListApi.md#search_product_lists) | **POST** /productlist.ProductList/SearchProductLists | Search Collections
[**search_product_lists_by_ids**](ProductListApi.md#search_product_lists_by_ids) | **POST** /productlist.ProductList/SearchProductListsByIds | Search Collections by Ids
[**set_product_list_associations**](ProductListApi.md#set_product_list_associations) | **POST** /productlist.ProductList/SetProductListAssociations | Set Collection/Product Associations
[**update_product_list**](ProductListApi.md#update_product_list) | **POST** /productlist.ProductList/UpdateProductList | Update Collection


# **create_product_list**
> ProductlistCreateProductListResponse create_product_list(body)

Create Collection

The CreateProductList endpoint is used to create a new collection of products within the system. This endpoint allows users to define the details and attributes of the collection.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_create_product_list_request import ProductlistCreateProductListRequest
from product-list.models.productlist_create_product_list_response import ProductlistCreateProductListResponse
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
    except Exception as e:
        print("Exception when calling ProductListApi->create_product_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistCreateProductListRequest**](ProductlistCreateProductListRequest.md)|  | 

### Return type

[**ProductlistCreateProductListResponse**](ProductlistCreateProductListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product_list_association**
> ProductlistCreateProductListAssociationResponse create_product_list_association(body)

Create Collection/Product Association

The CreateProductListAssociation endpoint is used to create an association between a collection and a product.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_create_product_list_association_request import ProductlistCreateProductListAssociationRequest
from product-list.models.productlist_create_product_list_association_response import ProductlistCreateProductListAssociationResponse
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
    body = product-list.ProductlistCreateProductListAssociationRequest() # ProductlistCreateProductListAssociationRequest | 

    try:
        # Create Collection/Product Association
        api_response = api_instance.create_product_list_association(body)
        print("The response of ProductListApi->create_product_list_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->create_product_list_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistCreateProductListAssociationRequest**](ProductlistCreateProductListAssociationRequest.md)|  | 

### Return type

[**ProductlistCreateProductListAssociationResponse**](ProductlistCreateProductListAssociationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_list**
> ProductlistDeleteProductListResponse delete_product_list(body)

Delete Collection

The DeleteProductList endpoint is used to delete an existing collection of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_delete_product_list_request import ProductlistDeleteProductListRequest
from product-list.models.productlist_delete_product_list_response import ProductlistDeleteProductListResponse
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
    body = product-list.ProductlistDeleteProductListRequest() # ProductlistDeleteProductListRequest | 

    try:
        # Delete Collection
        api_response = api_instance.delete_product_list(body)
        print("The response of ProductListApi->delete_product_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->delete_product_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistDeleteProductListRequest**](ProductlistDeleteProductListRequest.md)|  | 

### Return type

[**ProductlistDeleteProductListResponse**](ProductlistDeleteProductListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_list_association**
> ProductlistDeleteProductListAssociationResponse delete_product_list_association(body)

Delete Collection/Product Association

The DeleteProductListAssociation endpoint is used to delete an association between a collection and a product.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_delete_product_list_association_request import ProductlistDeleteProductListAssociationRequest
from product-list.models.productlist_delete_product_list_association_response import ProductlistDeleteProductListAssociationResponse
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
    body = product-list.ProductlistDeleteProductListAssociationRequest() # ProductlistDeleteProductListAssociationRequest | 

    try:
        # Delete Collection/Product Association
        api_response = api_instance.delete_product_list_association(body)
        print("The response of ProductListApi->delete_product_list_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->delete_product_list_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistDeleteProductListAssociationRequest**](ProductlistDeleteProductListAssociationRequest.md)|  | 

### Return type

[**ProductlistDeleteProductListAssociationResponse**](ProductlistDeleteProductListAssociationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_list_associations_by_product_grn**
> ProductlistGetProductListAssociationsByProductGrnResponse get_product_list_associations_by_product_grn(body)

Get Collection/Product Associations by Product GRN

The GetProductListAssociationsByProductGrn endpoint is used to get the associations between a collection and a list of products by product GRN.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_get_product_list_associations_by_product_grn_request import ProductlistGetProductListAssociationsByProductGrnRequest
from product-list.models.productlist_get_product_list_associations_by_product_grn_response import ProductlistGetProductListAssociationsByProductGrnResponse
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
    body = product-list.ProductlistGetProductListAssociationsByProductGrnRequest() # ProductlistGetProductListAssociationsByProductGrnRequest | 

    try:
        # Get Collection/Product Associations by Product GRN
        api_response = api_instance.get_product_list_associations_by_product_grn(body)
        print("The response of ProductListApi->get_product_list_associations_by_product_grn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->get_product_list_associations_by_product_grn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistGetProductListAssociationsByProductGrnRequest**](ProductlistGetProductListAssociationsByProductGrnRequest.md)|  | 

### Return type

[**ProductlistGetProductListAssociationsByProductGrnResponse**](ProductlistGetProductListAssociationsByProductGrnResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_list_by_code**
> ProductlistGetProductListByCodeResponse get_product_list_by_code(body)

Get Collection by Code

The GetProductListByCode endpoint is used to retrieve an existing collection of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_get_product_list_by_code_request import ProductlistGetProductListByCodeRequest
from product-list.models.productlist_get_product_list_by_code_response import ProductlistGetProductListByCodeResponse
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
    body = product-list.ProductlistGetProductListByCodeRequest() # ProductlistGetProductListByCodeRequest | 

    try:
        # Get Collection by Code
        api_response = api_instance.get_product_list_by_code(body)
        print("The response of ProductListApi->get_product_list_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->get_product_list_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistGetProductListByCodeRequest**](ProductlistGetProductListByCodeRequest.md)|  | 

### Return type

[**ProductlistGetProductListByCodeResponse**](ProductlistGetProductListByCodeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_list_by_id**
> ProductlistGetProductListByIdResponse get_product_list_by_id(body)

Get Collection by Id

The GetProductListById endpoint is used to retrieve an existing collection of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_get_product_list_by_id_request import ProductlistGetProductListByIdRequest
from product-list.models.productlist_get_product_list_by_id_response import ProductlistGetProductListByIdResponse
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
    body = product-list.ProductlistGetProductListByIdRequest() # ProductlistGetProductListByIdRequest | 

    try:
        # Get Collection by Id
        api_response = api_instance.get_product_list_by_id(body)
        print("The response of ProductListApi->get_product_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->get_product_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistGetProductListByIdRequest**](ProductlistGetProductListByIdRequest.md)|  | 

### Return type

[**ProductlistGetProductListByIdResponse**](ProductlistGetProductListByIdResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_list_by_url_key**
> ProductlistGetProductListByUrlKeyResponse get_product_list_by_url_key(body)

Get Collection by Url Key

The GetProductListByUrlKey endpoint is used to retrieve an existing collection of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_get_product_list_by_url_key_request import ProductlistGetProductListByUrlKeyRequest
from product-list.models.productlist_get_product_list_by_url_key_response import ProductlistGetProductListByUrlKeyResponse
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
    body = product-list.ProductlistGetProductListByUrlKeyRequest() # ProductlistGetProductListByUrlKeyRequest | 

    try:
        # Get Collection by Url Key
        api_response = api_instance.get_product_list_by_url_key(body)
        print("The response of ProductListApi->get_product_list_by_url_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->get_product_list_by_url_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistGetProductListByUrlKeyRequest**](ProductlistGetProductListByUrlKeyRequest.md)|  | 

### Return type

[**ProductlistGetProductListByUrlKeyResponse**](ProductlistGetProductListByUrlKeyResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_lists_count**
> ProductlistGetProductListsCountResponse get_product_lists_count(body)

Get Collection Product Count

The GetProductListsCount endpoint is used to get the number of products associated with a collection.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_get_product_lists_count_request import ProductlistGetProductListsCountRequest
from product-list.models.productlist_get_product_lists_count_response import ProductlistGetProductListsCountResponse
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
    body = product-list.ProductlistGetProductListsCountRequest() # ProductlistGetProductListsCountRequest | 

    try:
        # Get Collection Product Count
        api_response = api_instance.get_product_lists_count(body)
        print("The response of ProductListApi->get_product_lists_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->get_product_lists_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistGetProductListsCountRequest**](ProductlistGetProductListsCountRequest.md)|  | 

### Return type

[**ProductlistGetProductListsCountResponse**](ProductlistGetProductListsCountResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_list_associations**
> ProductlistListProductListAssociationsResponse list_product_list_associations(body)

List Collection/Product Associations

The ListProductListAssociations endpoint is used to list the associations between a collection and a list of products.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_list_product_list_associations_request import ProductlistListProductListAssociationsRequest
from product-list.models.productlist_list_product_list_associations_response import ProductlistListProductListAssociationsResponse
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
    body = product-list.ProductlistListProductListAssociationsRequest() # ProductlistListProductListAssociationsRequest | 

    try:
        # List Collection/Product Associations
        api_response = api_instance.list_product_list_associations(body)
        print("The response of ProductListApi->list_product_list_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->list_product_list_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistListProductListAssociationsRequest**](ProductlistListProductListAssociationsRequest.md)|  | 

### Return type

[**ProductlistListProductListAssociationsResponse**](ProductlistListProductListAssociationsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_lists**
> ProductlistListProductListsResponse list_product_lists(body)

List Collections

The ListProductLists endpoint is used to retrieve a list of existing collections of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_list_product_lists_request import ProductlistListProductListsRequest
from product-list.models.productlist_list_product_lists_response import ProductlistListProductListsResponse
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
    body = product-list.ProductlistListProductListsRequest() # ProductlistListProductListsRequest | 

    try:
        # List Collections
        api_response = api_instance.list_product_lists(body)
        print("The response of ProductListApi->list_product_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->list_product_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistListProductListsRequest**](ProductlistListProductListsRequest.md)|  | 

### Return type

[**ProductlistListProductListsResponse**](ProductlistListProductListsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list_bulk_update_product_list_associations**
> object product_list_bulk_update_product_list_associations(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_bulk_update_product_list_associations_request import ProductlistBulkUpdateProductListAssociationsRequest
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
    body = product-list.ProductlistBulkUpdateProductListAssociationsRequest() # ProductlistBulkUpdateProductListAssociationsRequest | 

    try:
        api_response = api_instance.product_list_bulk_update_product_list_associations(body)
        print("The response of ProductListApi->product_list_bulk_update_product_list_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->product_list_bulk_update_product_list_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistBulkUpdateProductListAssociationsRequest**](ProductlistBulkUpdateProductListAssociationsRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_product_lists**
> ProductlistSearchProductListsResponse search_product_lists(body)

Search Collections

The SearchProductLists endpoint is used to retrieve a list of existing collections of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_search_product_lists_request import ProductlistSearchProductListsRequest
from product-list.models.productlist_search_product_lists_response import ProductlistSearchProductListsResponse
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
    body = product-list.ProductlistSearchProductListsRequest() # ProductlistSearchProductListsRequest | 

    try:
        # Search Collections
        api_response = api_instance.search_product_lists(body)
        print("The response of ProductListApi->search_product_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->search_product_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistSearchProductListsRequest**](ProductlistSearchProductListsRequest.md)|  | 

### Return type

[**ProductlistSearchProductListsResponse**](ProductlistSearchProductListsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_product_lists_by_ids**
> ProductlistSearchProductListsByIdsResponse search_product_lists_by_ids(body)

Search Collections by Ids

The SearchProductListsByIds endpoint is used to retrieve a list of existing collections of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_search_product_lists_by_ids_request import ProductlistSearchProductListsByIdsRequest
from product-list.models.productlist_search_product_lists_by_ids_response import ProductlistSearchProductListsByIdsResponse
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
    body = product-list.ProductlistSearchProductListsByIdsRequest() # ProductlistSearchProductListsByIdsRequest | 

    try:
        # Search Collections by Ids
        api_response = api_instance.search_product_lists_by_ids(body)
        print("The response of ProductListApi->search_product_lists_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->search_product_lists_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistSearchProductListsByIdsRequest**](ProductlistSearchProductListsByIdsRequest.md)|  | 

### Return type

[**ProductlistSearchProductListsByIdsResponse**](ProductlistSearchProductListsByIdsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_product_list_associations**
> ProductlistSetProductListAssociationsResponse set_product_list_associations(body)

Set Collection/Product Associations

The SetProductListAssociations endpoint is used to set the associations between a collection and a list of products.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_set_product_list_associations_request import ProductlistSetProductListAssociationsRequest
from product-list.models.productlist_set_product_list_associations_response import ProductlistSetProductListAssociationsResponse
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
    body = product-list.ProductlistSetProductListAssociationsRequest() # ProductlistSetProductListAssociationsRequest | 

    try:
        # Set Collection/Product Associations
        api_response = api_instance.set_product_list_associations(body)
        print("The response of ProductListApi->set_product_list_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->set_product_list_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistSetProductListAssociationsRequest**](ProductlistSetProductListAssociationsRequest.md)|  | 

### Return type

[**ProductlistSetProductListAssociationsResponse**](ProductlistSetProductListAssociationsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_list**
> ProductlistUpdateProductListResponse update_product_list(body)

Update Collection

The UpdateProductList endpoint is used to update an existing collection of products within the system.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import product-list
from product-list.models.productlist_update_product_list_request import ProductlistUpdateProductListRequest
from product-list.models.productlist_update_product_list_response import ProductlistUpdateProductListResponse
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
    body = product-list.ProductlistUpdateProductListRequest() # ProductlistUpdateProductListRequest | 

    try:
        # Update Collection
        api_response = api_instance.update_product_list(body)
        print("The response of ProductListApi->update_product_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductListApi->update_product_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductlistUpdateProductListRequest**](ProductlistUpdateProductListRequest.md)|  | 

### Return type

[**ProductlistUpdateProductListResponse**](ProductlistUpdateProductListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

