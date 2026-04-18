def format_report(summary, news, trends):
    report = "📊 *LAPORAN EKONOMI HARIAN*\n\n"

    report += "🧠 *INSIGHT UTAMA*\n"
    report += summary + "\n\n"

    report += "📰 *HEADLINES*\n"
    for n in news[:5]:
        report += f"- {n}\n"

    report += "\n🔥 *TRENDING TOPICS*\n"
    for t in trends[:5]:
        report += f"- {t}\n"

    return report
