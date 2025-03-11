import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json


def fetch_incident_articles(days_ago=1, keywords=None):
    URL = "https://timesofindia.indiatimes.com/rssfeeds/2647163.cms"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return json.dumps({"error": f"Failed to fetch RSS feed: {str(e)}"}, indent=3)

    try:
        data = BeautifulSoup(response.text, "xml")
    except Exception:
        return json.dumps({"error": f"Failed to parse XML: {str(e)}"}, indent=3)

    yesterday = datetime.now().date() - timedelta(days=days_ago)

    if keywords == None:
        keywords = [
            "fire",
            "Fire",
            "flood",
            "Flood",
            "earthquake",
            "Earthquake",
            "forest fire",
            "Forest Fire",
        ]

    articles = []

    for item in data.find_all("item"):
        title = item.title.text.strip()
        pub_date = item.pubDate.text.strip()
        link = item.link.text.strip()

        try:
            pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%S%z")
            article_date = pub_date.date()
        except ValueError:
            continue

        if (
            any(keyword in title.lower() for keyword in keywords)
            and article_date == yesterday
        ):
            articles.append({"title": title, "link": link, "date": str(article_date)})

    return json.dumps(
        articles if articles else {"error": "No relevant articles found"}, indent=3
    )


if __name__ == "__main__":
    result = fetch_incident_articles()
    print(result)
