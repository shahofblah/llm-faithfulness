import abc
import google.generativeai as genai
import os
import grpc
import typing_extensions as typing
import time
from functools import wraps

genai.configure(api_key=os.environ["API_KEY"])

class LLMClient(abc.ABC):
    """
    Abstract base class for LLM clients.
    """
    @abc.abstractmethod
    def make_request(self, request):
        """
        Make a request to the API using the client.
        """
        pass

def retry_on_resource_exhausted(max_attempts: int = 5):
    """
    A decorator that retries a function on gRPC RESOURCE_EXHAUSTED errors.
    
    Args:
        max_attempts: Maximum number of retry attempts before giving up
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except grpc.RpcError as e:
                    attempt += 1
                    if e.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
                        if attempt >= max_attempts:
                            print(f"Maximum retry attempts ({max_attempts}) reached. Raising error.")
                            raise
                        print(f"Attempt {attempt}/{max_attempts} failed with RESOURCE_EXHAUSTED. "
                              f"Retrying in 60 seconds...")
                        time.sleep(60)
                    else:
                        # Don't retry on other types of gRPC errors
                        raise
        return wrapper
    return decorator

class Gemini(LLMClient):
    """
    Gemini client.
    """
    def __init__(self, model):
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel(model)

    @retry_on_resource_exhausted(max_attempts=3)
    def make_request(self, request):
        """
        Create the Gemini client instance.
        """
        return self.model.generate_content(request)

class GeminiJSON(Gemini):
    """
    Gemini client.
    """
    def __init__(self, model, schema):
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel(model)
        self.generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=schema)

    @retry_on_resource_exhausted(max_attempts=3)
    def make_request(self, request):
        return self.model.generate_content(request,generation_config=self.generation_config)
    
# Example usage:
DEFAULT_MODEL = "gemini-1.5-flash"
CLASSIFIER_SCHEMA = list[bool]
CLASSIFICATION_TASK_SCHEMA = list[(str,bool)]

def GetGemini(model=DEFAULT_MODEL):
    return Gemini(model)

def GetGeminiClassifier(model=DEFAULT_MODEL):
    return GeminiJSON(model, CLASSIFIER_SCHEMA)

def GetGeminilassificationTask(model=DEFAULT_MODEL):
    return GeminiJSON(model, CLASSIFICATION_TASK_SCHEMA)



# gemini = GetGemini()
# response = gemini.make_request("Write a story about a magic backpack.")
# print(response)
