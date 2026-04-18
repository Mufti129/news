import feedparser

def get_news():
    queries = [
        "ekonomi indonesia",
        "bisnis indonesia",
        "inflasi indonesia"
    ]
    
    all_news = []

    for q in queries:
        url = f"https://news.google.com/rss/search?q={q}"
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            all_news.append(entry.title)

    return all_news
