from news import get_news
from trends import get_trends
from ai_summary import generate_ai_summary
from send_report import send_telegram
from save import save_to_csv
from formatter import format_report

def run():
    news = get_news()
    trends = get_trends()

    summary = generate_ai_summary(news, trends)

    report = format_report(summary, news, trends)

    save_to_csv(news, trends)

    send_telegram(report)

if __name__ == "__main__":
    run()
