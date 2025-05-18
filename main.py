import requests
from bs4 import BeautifulSoup

def scrape_goaloo_today():
    url = "https://live.goaloo900.com/football/schedule/today"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://live.goaloo900.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to load page:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    matches = []
    rows = soup.select("div[class*=oddsContent] div[class*=matchItem]")

    for row in rows:
        try:
            time = row.select_one(".time").text.strip()
            league = row.select_one(".leagueName").text.strip()
            teams = row.select_one(".teamName").text.strip()
            matches.append({
                "time": time,
                "league": league,
                "teams": teams
            })
        except:
            continue

    for match in matches:
        print(f"{match['time']} - {match['league']} - {match['teams']}")

if __name__ == "__main__":
    scrape_goaloo_today()
