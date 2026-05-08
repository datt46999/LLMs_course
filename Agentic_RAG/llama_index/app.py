from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI

from tools import search_tool, weather_info_tool, hub_stats_tool
from retriever import guest_info_tool

llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")

# Create Alfred with all the tools
alfred = AgentWorkflow.from_tools_or_functions(
    [guest_info_tool, search_tool, weather_info_tool, hub_stats_tool],
    llm=llm,
)




# query = "Tell me about Lady Ada Lovelace. What's her background?"
# query = "What's the weather like in Paris tonight? Will it be suitable for our fireworks display?"
# query = "One of our guests is from Google. What can you tell me about their most popular model?"
query = "I need to speak with Dr. Nikola Tesla about recent advancements in wireless energy. Can you help me prepare for this conversation?"
response = await alfred.run(query)

print("🎩 Alfred's Response:")
print(response.response.blocks[0].text)


# Advanced Features: Conversation Memory

# from llama_index.core.workflow import Context

# alfred = AgentWorkflow.from_tools_or_functions(
#     [guest_info_tool, search_tool, weather_info_tool, hub_stats_tool],
#     llm=llm
# )

# # Remembering state
# ctx = Context(alfred)

# # First interaction
# response1 = await alfred.run("Tell me about Lady Ada Lovelace.", ctx=ctx)
# print("🎩 Alfred's First Response:")
# print(response1)

# # Second interaction (referencing the first)
# response2 = await alfred.run("What projects is she currently working on?", ctx=ctx)
# print("🎩 Alfred's Second Response:")
# print(response2)