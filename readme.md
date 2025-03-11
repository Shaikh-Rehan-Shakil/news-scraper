# Incident Article Scraper

This script fetches incident-related news articles from the *Times of India* RSS feed based on specific keywords and returns the results in JSON format.

## Requirements

Make sure you have Python installed. Then, install the required dependencies using:

```sh
pip install -r requirements.txt
```

## Usage

Run the script using:

```sh
python script.py
```

### Function Usage (Optional)

If using the script as a module, you can call the `fetch_incident_articles` function:

```python
from script import fetch_incident_articles

articles_json = fetch_incident_articles()
print(articles_json)
```

## Output Format

The script returns a JSON array of articles:

```json
[
    {
        "title": "Example Fire Incident",
        "link": "https://example.com/article",
        "date": "2024-03-11"
    }
]
```

If no articles are found, an empty JSON array `[]` is returned.

## Error Handling

- If the RSS feed cannot be fetched, the script returns.
    ```json
    {
        "error": "Failed to fetch RSS feed: [specific error message]"
    }
    ```
- If the RSS feed cannot be fetched, the script returns.
    ```json
    {
        "error": "Failed to parse XML: [specific error message]"
    }
    ```

- If no relevant articles are found, the script returns.
    ```json
    {
        "error": "No relevant articles found"
    }
    ```

## Customization

You can modify the `fetch_incident_articles` function to change:
- The number of days to look back (`days_ago` parameter).
- The keywords used for filtering articles (`keywords` parameter).

