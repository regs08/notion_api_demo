# Notion API Demo

This project demonstrates how to interact with the Notion API to pull and push data to your Notion pages.

## Project Structure

```
notion_api_demo/
├── api_keys/           # Directory for storing API keys
├── src/               # Source code
│   ├── __init__.py
│   ├── config.py      # Configuration settings
│   ├── notion_client.py  # Notion API client wrapper
│   └── utils.py       # Utility functions
├── .env              # Environment variables (not tracked in git)
├── requirements.txt  # Project dependencies
└── main.py          # Main script to run the demo
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Notion API key:
   - Create a `.env` file in the root directory
   - Add your Notion API key: `NOTION_API_KEY=your_api_key_here`

## Usage

Run the main script:
```bash
python main.py
```

## Features

- Pull data from Notion pages
- Push data to Notion pages
- Create and update Notion pages
- Handle Notion blocks and content 