
day_count = 0
days = range(1,30+1)
seasons = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]]

f = open("enoch.py", "a")


f.write("day_number = {")
for season in seasons:
    for month in season:
        for day in days:
            day_count = day_count + 1

            if month == 3 or month == 6 or month == 9 or month == 12:
                if day == 30:
                    f.write(f"{day_count}:'{month}-{day}',")
                    day_count = day_count + 1
                    f.write(f"{day_count}:'{month}-{day + 1}',")
                else:
                    f.write(f"{day_count}:'{month}-{day}',")
            else:
                f.write(f"{day_count}:'{month}-{day}',")

f.write("}")

f.close()
