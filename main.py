"""
Main script to demonstrate Notion API functionality.
"""
from src.notion_api_wrapper import NotionAPI

def main():
    # Initialize the Notion API client
    notion = NotionAPI()
    
    try:
        print("Searching for all accessible objects in your workspace...")
        all_objects = notion.search_all()
        
        if all_objects:
            print(f"\nFound {len(all_objects)} total objects:")
            for obj in all_objects:
                obj_type = obj.get('object', 'unknown')
                
                if obj_type == 'page':
                    properties = obj.get('properties', {})
                    # Get title/Name
                    title = properties.get('title', properties.get('Name', {}))
                    title_text = notion.get_property_value(title) if title else 'Untitled'
                    
                    print(f"\nType: {obj_type}")
                    print(f"Title: {title_text}")
                    print(f"ID: {obj.get('id')}")
                    print(f"URL: {obj.get('url')}")
                    print("Properties:")
                    # Print all properties using the mapping
                    for prop_name, prop_value in properties.items():
                        value = notion.get_property_value(prop_value)
                        print(f"  {prop_name}: {value}")
                else:
                    # For databases, just show basic info
                    title = obj.get('title', [{}])[0].get('plain_text', 'Untitled')
                    print(f"\nType: {obj_type}")
                    print(f"Title: {title}")
                    print(f"ID: {obj.get('id')}")
                    print(f"URL: {obj.get('url')}")
        else:
            print("No objects found in your workspace.")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 