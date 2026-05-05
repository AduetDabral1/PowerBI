from playwright.sync_api import sync_playwright
import pandas as pd
import time

TEAM_URLS = {
    "CSK": "https://www.espncricinfo.com/series/ipl-2026-1510719/chennai-super-kings-squad-1511148/series-squads",
    "DC": "https://www.espncricinfo.com/series/ipl-2026-1510719/delhi-capitals-squad-1511107/series-squads",
    "MI": "https://www.espncricinfo.com/series/ipl-2026-1510719/mumbai-indians-squad-1511145/series-squads",
    "RCB": "https://www.espncricinfo.com/series/ipl-2026-1510719/royal-challengers-bengaluru-squad-1511146/series-squads",
    "KKR": "https://www.espncricinfo.com/series/ipl-2026-1510719/kolkata-knight-riders-squad-1511144/series-squads",
    "SRH": "https://www.espncricinfo.com/series/ipl-2026-1510719/sunrisers-hyderabad-squad-1511147/series-squads",
    "RR": "https://www.espncricinfo.com/series/ipl-2026-1510719/rajasthan-royals-squad-1511143/series-squads",
    "PBKS": "https://www.espncricinfo.com/series/ipl-2026-1510719/punjab-kings-squad-1511142/series-squads",
    "GT": "https://www.espncricinfo.com/series/ipl-2026-1510719/gujarat-titans-squad-1511141/series-squads",
    "LSG": "https://www.espncricinfo.com/series/ipl-2026-1510719/lucknow-super-giants-squad-1511149/series-squads"
}

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for team, url in TEAM_URLS.items():
        print(f"\n🔵 {team}")
        page.goto(url, timeout=60000)

        # Wait for player cards to load
        page.wait_for_selector("a[href*='/player/']", timeout=15000)

        players = page.query_selector_all("a[href*='/player/']")

        print(f"➡️ Found {len(players)} players")

        for player in players:
            try:
                name = player.inner_text().strip()
                href = player.get_attribute("href")

                if not name or not href:
                    continue

                player_url = "https://www.espncricinfo.com" + href

                print(f"   → {name}")

                # Open player page
                page.goto(player_url)
                page.wait_for_timeout(1000)

                content = page.content()

                batting = ""
                bowling = ""
                role = ""
                image = ""

                # Extract info (simple parsing)
                if "Batting Style" in content:
                    batting = content.split("Batting Style")[1].split("</span>")[1].split("<")[0].strip()

                if "Bowling Style" in content:
                    bowling = content.split("Bowling Style")[1].split("</span>")[1].split("<")[0].strip()

                if "Playing Role" in content:
                    role = content.split("Playing Role")[1].split("</span>")[1].split("<")[0].strip()

                # Image
                try:
                    img = page.query_selector("img")
                    if img:
                        image = img.get_attribute("src")
                except:
                    pass

                data.append({
                    "player": name,
                    "role": role,
                    "batting_style": batting,
                    "bowling_style": bowling,
                    "Image": image,
                    "team": team
                })

                page.go_back()
                page.wait_for_timeout(1000)

            except Exception as e:
                print(f"❌ Error: {e}")

    browser.close()


df = pd.DataFrame(data).drop_duplicates()

print(f"\n📊 Total players: {len(df)}")

df.to_excel("IPL_2026_Players.xlsx", index=False)

print("✅ Excel created successfully")