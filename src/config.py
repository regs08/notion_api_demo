"""
Configuration settings for the Notion API demo.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Notion API configuration
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
if not NOTION_API_KEY:
    raise ValueError("NOTION_API_KEY not found in environment variables")

# Default database ID (you can change this in your .env file)
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID', '')

# API version
NOTION_VERSION = '2022-06-28' 