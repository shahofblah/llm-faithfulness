from llm import LLMClient, GetGeminilassificationTask
from classification import labeledData

celestialObjects = """
Generate a list of names of objects from either the Milky Way or Andromeda galaxy, 40 total. Ensure they don't contain
Milky Way or Andromeda in their name. Label them as true or false depending on whether they belong to Milky Way or Andromeda.
""" 

def generateLabeledData(llm: LLMClient, query: str) -> labeledData:
    return llm.make_request(query)

# Testing
gemClient = GetGeminilassificationTask()
data = generateLabeledData(gemClient, celestialObjects)
print("data:",data)