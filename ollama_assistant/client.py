import logging
from mongoengine import connect
from settings import DEFAULT_API_URL
from chat import Chat
from assistant import Assistant


class OllamaClient:
    """
    OllamaClient provides a high-level interface to interact with Ollama services.

    Parameters
    ----------
    api_url : str, optional
        Base URL for the API endpoints.
    model : str, optional
        The model used by the generation and chat services, default is 'mistrel'.
    db_host : str, optional
        Database host address, default is 'localhost'.
    db_port : int, optional
        Database port number, default is 27017.
    db_name : str, optional
        Database name, default is 'ollama_db'.
    """

    def __init__(
        self,
        api_url=None,
        model=None,
        db_host="localhost",
        db_port=27017,
        db_name="ollama_db",
    ):
        self.__base_url = api_url or DEFAULT_API_URL
        self.__connect_to_db(db_host, db_port, db_name)
        self.__assistant = Assistant(model=model or "mistrel")

    def __connect_to_db(self, db_host, db_port, db_name):
        """
        Establish a connection to the MongoDB database.

        Parameters
        ----------
        db_host : str
            Database host address.
        db_port : int
            Database port number.
        db_name : str
            Database name.
        """
        try:
            connect(db_name, host=f"mongodb://{db_host}:{db_port}")
            logging.info(
                f"Connected to MongoDB at mongodb://{db_host}:{db_port}/{db_name}"
            )
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise

    @property
    def assistant(self):
        """Provides access to the assistant thread."""
        return self.__assistant
