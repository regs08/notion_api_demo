"""
Utility functions for the Notion API demo.
"""
from typing import Dict, Any

def format_notion_properties(properties: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format properties for Notion API.
    This is a helper function to convert Python types to Notion property types.
    """
    formatted = {}
    for key, value in properties.items():
        if isinstance(value, str):
            formatted[key] = {
                "title": [{"text": {"content": value}}]
            }
        elif isinstance(value, bool):
            formatted[key] = {
                "checkbox": value
            }
        elif isinstance(value, (int, float)):
            formatted[key] = {
                "number": value
            }
        elif isinstance(value, list):
            formatted[key] = {
                "multi_select": [{"name": item} for item in value]
            }
    return formatted

def extract_page_content(page_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant content from a Notion page response.
    """
    return {
        "id": page_data.get("id"),
        "properties": page_data.get("properties", {}),
        "url": page_data.get("url"),
        "created_time": page_data.get("created_time"),
        "last_edited_time": page_data.get("last_edited_time")
    } 