import datasets
from langchain_core.documents import Document
from smolagents import Tool
from langchain_community.retrievers import BM25Retriever

guest_datasets = datasets.load_dataset("agents-course/unit3-invitees", split="train")

docs = [
    Document(
        page_content="\n".join([
            f"Name: {guest['name']}",
            f"Relation: {guest['relation']}",
            f"Description: {guest['description']}",
            f"Email: {guest['email']}",
        ]),
        metadata={"name": guest['name']}
    ) for guest in guest_datasets
]

class GuestRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = "Retrieves detailed information about gala guests based on their name or relation"
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about"
        }
    }
    output_type = "string"

    def __init__(self, docs):
        super().__init__()
        self.is_initialized = False
        self.retriever = BM25Retriever.from_documents(docs)

    def forward(self, query: str):
        results = self.retriever.invoke(query)
        if results:
            return "\n\n".join([doc.page_content for doc in results[:3]])
        else:
            return "No matching guest information found"

guest_info_tool = GuestRetrieverTool(docs)

from smolagents import CodeAgent, InferenceClientModel

# Initialize the Hugging Face model
model = InferenceClientModel()

# Create Alfred, our gala agent, with the guest info tool
alfred = CodeAgent(tools=[guest_info_tool], model=model)

# Example query Alfred might receive during the gala
response = alfred.run("Tell me about our guest named 'Lady Ada Lovelace'.")

print("🎩 Alfred's Response:")
print(response)