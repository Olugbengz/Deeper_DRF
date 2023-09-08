from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine




def get_index(index_name='cfe-product'):
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search(quesry, **kwargs):
    index = get_index()
    results = index.search(query)
    return results 