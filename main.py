
import json
import requests

from streamlit.connections import ExperimentalBaseConnection


class FruityviceConnection(ExperimentalBaseConnection[requests.Session]):

    """
    A connection class to fruit information data from the  API.

    Attributes:
        connection_name (str): The name of the connection (optional).
    """

    def __init__(self, connection_name=None, **kwargs) :

        """
        Initializes the fruitInformationProviderConnection.

        Args:
            *args: Variable-length argument list.
            connection_name (str, optional): The name of the connection (default is None).
            **kwargs: Keyword arguments.
        """

        super().__init__(connection_name, **kwargs)
        self._resource = self._connect()

    def _connect(self) -> requests.Session:

        """
        Creates a new requests session as the underlying resource.

        Returns:
            requests.Session: A new requests session.
        """

        return requests.Session()
    
    def cursor(self):

        """
        Returns the underlying requests session as the cursor.

        Returns:
            requests.Session: The requests session object.
        """

        return self._resource
    
    def query(self,fruits,ttl: int=3600):

        # Fetches recipes for the specified search query from the Spoonacular API.

        '''
        Args:
            query (string): A search query for which recipes are to be fetched.
        
        Returns:
            dict: A dictionary containing recipe data for each query.
            The Structure of returned dictionary is:

            {
                "name": "Mango",
                "id": 27,
                "family": "Anacardiaceae",
                "order": "Sapindales",
                "genus": "Mangifera",
                "nutritions": {
                    "calories": 60,
                    "fat": 0.38,
                    "sugar": 13.7,
                    "carbohydrates": 15,
                    "protein": 0.82
                }
            }

        
        '''

        def _get_data(query):

            """
            Fetches food information for the specified search query from the Fruityvice API.
            
            """

            fruit_data = {}

            url = f"https://fruityvice.com/api/fruit/{query}"

            params = {
                'name':query
            }

            response = self._resource.get(url=url,params=params)

            if response.status_code ==200:
                data = response.json()

                fruit_data = {
                    'name':data['name'],
                    'family':data['family'],
                    'genus':data['genus'],
                    'calories':data['nutritions']['calories'],
                    'fat': data['nutritions']['fat'],
                    'sugar': data['nutritions']['sugar'],
                    'carbohydrates': data['nutritions']['carbohydrates'],
                    'protein': data['nutritions']['protein'],
                }
            else:
                raise Exception(f"Failed to fetch recipe data for {query}.")
            
            return fruit_data
        return _get_data(fruits)

