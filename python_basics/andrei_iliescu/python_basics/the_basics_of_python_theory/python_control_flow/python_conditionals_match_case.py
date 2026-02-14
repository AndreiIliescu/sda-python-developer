### match, case
# Pattern matching (Python 3.10+): permite casarea valorilor complexe similar cu switch-case.
# Exemplu 1:
zi = "marți"
match zi:
    case "luni":
        print("Este luni")
    case "marți":
        print("Este marți")
    case _:
        print("Este altă zi")


# Exemplu 2, cu destructurare și pattern-uri:
date = (2025, 6, 26)
match date:
    case (2025, 6, _) as today:
        print(f"Data este {today}, restul lunilor viitoare")
    case (an, luna, zi):
        print(f"Data este {zi:02d}/{luna:02d}/{an}")
