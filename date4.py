from datetime import datetime

def totalseconds(start,end):
     start_datetime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
     end_datetime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

     difference =end_datetime-start_datetime

     return difference.total_seconds()

start_date = "2024-02-10 08:00:00"
end_date = "2024-02-12 08:00:00"


difference_seconds = totalseconds(start_date, end_date)
print(f"The difference between the two dates in seconds is: {difference_seconds} seconds")