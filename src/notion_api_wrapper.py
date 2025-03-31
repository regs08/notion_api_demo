from notion_client import Client
from src.config import NOTION_API_KEY

class NotionAPI:
    # Property type mapping dictionary
    PROPERTY_TYPE_MAPPING = {
        'rich_text': lambda prop: prop['rich_text'][0]['text']['content'] if prop['rich_text'] else 'Empty',
        'select': lambda prop: prop['select']['name'] if prop['select'] else 'None',
        'multi_select': lambda prop: [item['name'] for item in prop['multi_select']],
        'date': lambda prop: prop['date']['start'] if prop['date'] else 'No date',
        'checkbox': lambda prop: prop['checkbox'],
        'number': lambda prop: prop['number'],
        'title': lambda prop: prop['title'][0]['text']['content'] if prop['title'] else 'Untitled',
        'email': lambda prop: prop['email'] or 'No email',
        'phone_number': lambda prop: prop['phone_number'] or 'No phone',
        'url': lambda prop: prop['url'] or 'No URL',
        'people': lambda prop: [person['name'] for person in prop['people']] if prop['people'] else [],
        'files': lambda prop: [file['name'] for file in prop['files']] if prop['files'] else [],
        'status': lambda prop: prop['status']['name'] if prop['status'] else 'No status',
        'formula': lambda prop: prop['formula'].get('string', prop['formula'].get('number', 'No result')),
        'relation': lambda prop: [rel['id'] for rel in prop['relation']] if prop['relation'] else []
    }

    def __init__(self):
        self.client = Client(auth=NOTION_API_KEY)
    
    def get_property_value(self, prop_value):
        """Extract the value from a property based on its type"""
        prop_type = prop_value.get('type', 'unknown')
        if prop_type in self.PROPERTY_TYPE_MAPPING:
            try:
                return self.PROPERTY_TYPE_MAPPING[prop_type](prop_value)
            except (KeyError, IndexError):
                return f"Error extracting {prop_type}"
        return f"Unhandled type: {prop_type}"

    def search_all(self):
        """Search for all objects in the workspace"""
        return self.client.search().get("results", [])
    
    def search_databases(self):
        """Search for all databases in the workspace"""
        return self.client.search(filter={"property": "object", "value": "database"}).get("results", []) 

    def get_database_pages(self, database_id):
        """Get all pages from a specific database"""
        try:
            response = self.client.databases.query(
                database_id=database_id,
                page_size=100  # Adjust this number based on your needs
            )
            return response.get('results', [])
        except Exception as e:
            print(f"Error querying database pages: {str(e)}")
            return [] 