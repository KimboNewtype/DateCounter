import datetime

def count_down(target_date):
    today = datetime.date.today()
    target = datetime.datetime.strptime(target_date, "%m/%d/%Y").date()

    if target < today:
        print("Target date has already passed.")
        return

    remaining_days = (target - today).days

    print("Countdown to", target_date)
    print("Today:", today.strftime("%m/%d/%Y"))
    print("Days remaining:", remaining_days)

# Main program
target_date = "09/24/2023"
count_down(target_date)
