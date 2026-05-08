"""
find latest new and global updates,
access to weather data
"""

from smolagents import (
    DuckDuckGoSearchTool,
    tool,
    CodeAgent, 
    InferenceClientModel,
)
from huggingface_hub import list_models

import random

# search_tool = DuckDuckGoSearchTool()
# results = search_tool("who is president of France")
# print(results)


class WeatherInforTool(Tool):
    name= "weather_infor"
    description ="Fetches dummy weather information for give location"
    inputs = {
        "location":
        {
            "type": "string",
            "description": "the location to get weather information for"
        }
    }
    output_type = "string"

    def forward(self, location: str):
        weather_conditions = [
            {"condition": "Rainy", "temp_c": 15},
            {"condition": "Clear", "temp_c": 25},
            {"condition": "Windy", "temp_c": 20}
        ]
        data = random.choice(weather_conditions)
        return f"Weather in {location}: {data['condition']}, {data['temp_c']}"
    
class HubStatsTool(Tool):
    name = "hub_stats"
    description = "Fetches the most downloaded model from a specific author on the Hugging Face Hub."
    inputs = {
        "author": {
            "type": "string",
            "description": "The username of the model author/organization to find models from."
        }
    }
    output_type = "string"
    def forward(self, author: str):
        try: 
            models = list(list_models(author = author, sort = "downloads", direction = -1, limit= 1))
            if models:
                model = models[0]
                return f"The most downloaded model by {author}, id {model.id} with {model.downloads:,} download"
            else:
                return f"No model find for author {author}"
        except Exception as e:
            return f"Error fetching models for {author}: {str(e)}"
        
        


weather_infor_tool = WeatherInforTool()
# print(weather_infor_tool("HoChiMinh"))
hub_stats_tool = HubStatsTool()

# Example usage
# print(hub_stats_tool("facebook"))

model = InferenceClientModel()

agent = CodeAgent(
    tools = [weather_infor_tool, hub_stats_tool],
    model = model
)