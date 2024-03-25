from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from scripts.score import get_vector_image, get_vector_gizi

service_endpoint = "https://team5search.search.windows.net"
key = "rPeGGz5cb504AJccADBfeqXDrAlOokSFAn4q3ktAR2AzSeDceAw5"
if not key:
    raise ValueError("Missing required Azure Search API key.")


def search_image(image_bytes):
    vector = get_vector_image(image_bytes)
    
    search_client = SearchClient(service_endpoint, "food", AzureKeyCredential(key))
    vector_query = VectorizedQuery(vector=vector, k_nearest_neighbors=3, fields="image_vector")

    results = search_client.search(
        vector_queries=[vector_query],
        select=["carbohydrate", "proteins", "calories", "fat","name", "image"],
    )

    ret = []
    for result in results:
        ret.append(dict(result))
    return ret


def search_gizi(calories, proteins, fat, carbohydrate):
    print(f'gizi: {[calories, proteins, fat, carbohydrate]}')
    vector = get_vector_gizi(calories, proteins, fat, carbohydrate)
    print(f'vector: {vector}')
    
    search_client = SearchClient(service_endpoint, "food", AzureKeyCredential(key))
    vector_query = VectorizedQuery(vector=vector, k_nearest_neighbors=3, fields="gizi_vector")

    results = search_client.search(
        vector_queries=[vector_query],
        select=["carbohydrate", "proteins", "calories", "fat","name", "image"],
    )


    ret = []
    for result in results:
        ret.append(dict(result))
    return ret
