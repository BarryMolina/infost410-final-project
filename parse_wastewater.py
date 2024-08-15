with open("wastewater.csv", "r", encoding="utf-8-sig") as wastewater, open(
    "insert_wastewater.sql", "w"
) as insert_wastewater:

    insert_wastewater.write(
        """
INSERT INTO Wastewater (WeekNum, WeekEnd, ViralActivityLevel)
VALUES
"""
    )
    week_num = 1

    for line in wastewater:
        week_end, viral_activity_level = line.rstrip().split(",")
        """
        example data:
        2022-01-01,16.86
        2022-01-08,23.6
        2022-01-15,23.38
        2022-01-22,19.46
        2022-01-29,13.78
        2022-02-05,9.27
        """
        print(week_end)
        row = f"({week_num}, '{week_end}', {viral_activity_level}),\n"
        insert_wastewater.write(row)
        week_num += 1
