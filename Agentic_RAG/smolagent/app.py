import random
from smolagent import CodeAgent, InferenceClientModel
from tools import DuckDuckGoSearchTool, WeatherInforTool, HubStatsTool
from retriever import guest_info_tool

model = InferenceClientModel()
search_tool = DuckDuckGoSearchTool()
weather_infor_tool = WeatherInforTool()
hub_starts_tool = HubStatsTool()
alfred = CodeAgent(
    tools = [search_tool, weather_infor_tool, hub_starts_tool, guest_info_tool],
    model = model,
    add_base_tools= True, # Add any additional base tools
    planning_interval = 3 #Enable planning every 3 steps
)


query = "Tell me about 'Lady Ada Lovelace'"


# query = "What's the weather like in Paris tonight? Will it be suitable for our fireworks display?"
# query = "One of our guests is from Qwen. What can you tell me about their most popular model?"
# query = "I need to speak with Dr. Nikola Tesla about recent advancements in wireless energy. Can you help me prepare for this conversation?"
response = alfred.run(query)

print("🎩 Alfred's Response:")
print(response)


# # Create Alfred with conversation memory
# alfred_with_memory = CodeAgent(
#     tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool], 
#     model=model,
#     add_base_tools=True,
#     planning_interval=3
# )

# # First interaction
# response1 = alfred_with_memory.run("Tell me about Lady Ada Lovelace.")
# print("🎩 Alfred's First Response:")
# print(response1)

# # Second interaction (referencing the first)
# response2 = alfred_with_memory.run("What projects is she currently working on?", reset=False)
# print("🎩 Alfred's Second Response:")
# print(response2)