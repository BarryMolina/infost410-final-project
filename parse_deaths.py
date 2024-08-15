from datetime import datetime

with open("deaths.csv", "r", encoding="utf-8-sig") as deaths_long, open(
    "insert_deaths.sql", "w"
) as insert_deaths:

    insert_deaths.write(
        """
INSERT INTO Deaths (WeekNum, WeekEnd, WeeklyDeaths)
VALUES
"""
    )
    week_num = 1

    for line in reversed(list(deaths_long)):
        week, deaths = line.rstrip().split(",")
        """
        example data:
        Aug 03 2024,340
        Jul 27 2024,511
        Jul 20 2024,517
        Jul 13 2024,457
        Jul 06 2024,435
        Jun 29 2024,390
        Jun 22 2024,405
        Jun 15 2024,353
        """
        # print(week)
        week_datetime = datetime.strptime(week.strip(), "%b %d %Y")
        week_iso = week_datetime.strftime("%Y-%m-%d")
        row = f"({week_num}, '{week_iso}', {deaths}),\n"
        print(row)
        insert_deaths.write(row)
        week_num += 1
