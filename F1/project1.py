#Command Line agruments
import sys 
if len(sys.argv) < 2:
    print("Error:Please provide the valid file name.")
    sys.exit()
f1_drivers.txt =sys.argv[1]
try:
    with open(f1_drivers.txt, 'r') as file:
        lines =file.readlines()
except FileNotFoundError:
    print(f"Error: The file'{f1_drivers.txt}' does not exist.")
    sys.exit()

race_name = lines[0].strip()
print(f"Race Name: {race_name}")
#Storing driver data 
drivers = []
for line in lines[1:]:
    parts = line.strip().split(',')
    driver_code = parts[0]
    driver_name = parts[1]
    team =parts[2]
    lap_time = float(parts[3])
    drivers.append((driver_code, driver_name, team, lap_time))


#Finding the fastest time and average time 
fastest_time = float('inf')
fastest_driver =''
total_time = 0
driver_count =len(drivers)

for drive in drivers:
    total_time+= driver[3]
    if driver[3] < fastest_time:
        fastest_time =driver[3]
        fastest_driver= driver[0]
average_time = total_time /driver_count


print(f"Fastest Driver: {fastest_driver} with time {fastest_time:.2f} seconds")
print(f"Average Time for all drivers: {average_time:.2f} seconds")

#Sorting the drivers by their lap times in descending order 
sorted_drivers = sorted(drivers, key=lambda x: x[3], reverse=True)
print("Fastest times in descending order:")
for driver in sorted_drivers:
    print(f"{driver[0]}: {driver[3]:.2f} seconds")

#Display additional details along with the driver's code and lap time.
for driver in drivers:
    print(f"{driver[0]} ({driver[1]}, {driver[2]}): {driver[3]:.2f} seconds")

    