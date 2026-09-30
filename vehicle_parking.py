# Vehicle Parking Management System
# Parking records are stored in parking_data.csv

import csv
import os

CSV_FILE = "parking_data.csv"
TOTAL_SLOTS = 10

FIELDNAMES = [
    "vehicle_number",
    "vehicle_type",
    "parking_slot",
    "parking_hours",
    "parking_fee",
    "status"
]

def create_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def load_data():
    create_csv()
    with open(CSV_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))

def save_data(data):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

def park_vehicle():
    data = load_data()
    active = [v for v in data if v["status"] == "Parked"]

    if len(active) >= TOTAL_SLOTS:
        print("\nParking is full!")
        return

    vehicle_number = input("Enter vehicle number: ").upper()
    vehicle_type = input("Enter vehicle type (Bike/Car): ").capitalize()

    if vehicle_type not in ["Bike", "Car"]:
        print("Invalid vehicle type!")
        return

    for vehicle in active:
        if vehicle["vehicle_number"] == vehicle_number:
            print("This vehicle is already parked.")
            return

    occupied_slots = [int(v["parking_slot"]) for v in active]

    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            data.append({
                "vehicle_number": vehicle_number,
                "vehicle_type": vehicle_type,
                "parking_slot": slot,
                "parking_hours": "",
                "parking_fee": "",
                "status": "Parked"
            })
            save_data(data)

            print("\nVehicle parked successfully!")
            print("Vehicle Number:", vehicle_number)
            print("Vehicle Type:", vehicle_type)
            print("Parking Slot:", slot)
            return

def view_parked_vehicles():
    data = load_data()
    active = [v for v in data if v["status"] == "Parked"]

    if not active:
        print("\nNo vehicles are currently parked.")
        return

    print("\n===== PARKED VEHICLES =====")
    for vehicle in active:
        print(
            "Vehicle:", vehicle["vehicle_number"],
            "| Type:", vehicle["vehicle_type"],
            "| Slot:", vehicle["parking_slot"]
        )

def view_available_slots():
    data = load_data()
    active = [v for v in data if v["status"] == "Parked"]
    occupied_slots = [int(v["parking_slot"]) for v in active]

    available_slots = [
        slot for slot in range(1, TOTAL_SLOTS + 1)
        if slot not in occupied_slots
    ]

    print("\nAvailable Slots:", available_slots)
    print("Number of Available Slots:", len(available_slots))

def vehicle_exit():
    data = load_data()
    vehicle_number = input("Enter vehicle number: ").upper()

    vehicle = None
    for item in data:
        if item["vehicle_number"] == vehicle_number and item["status"] == "Parked":
            vehicle = item
            break

    if vehicle is None:
        print("Vehicle not found in parking.")
        return

    try:
        hours = int(input("Enter parking duration in hours: "))
        if hours <= 0:
            print("Invalid number of hours.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    rate = 20 if vehicle["vehicle_type"] == "Bike" else 40
    fee = hours * rate

    vehicle["parking_hours"] = str(hours)
    vehicle["parking_fee"] = str(fee)
    vehicle["status"] = "Exited"
    save_data(data)

    print("\n===== PARKING RECEIPT =====")
    print("Vehicle Number:", vehicle_number)
    print("Vehicle Type:", vehicle["vehicle_type"])
    print("Parking Slot:", vehicle["parking_slot"])
    print("Parking Duration:", hours, "hour(s)")
    print("Parking Fee: Rs.", fee)
    print("Vehicle exited successfully!")

def view_total_collection():
    data = load_data()
    total = 0

    for vehicle in data:
        if vehicle["parking_fee"]:
            total += int(vehicle["parking_fee"])

    print("\nTotal Parking Collection: Rs.", total)

def main():
    create_csv()

    while True:
        print("\n===================================")
        print(" VEHICLE PARKING MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Park Vehicle")
        print("2. View Parked Vehicles")
        print("3. Vehicle Exit")
        print("4. View Available Slots")
        print("5. View Total Collection")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            view_parked_vehicles()
        elif choice == "3":
            vehicle_exit()
        elif choice == "4":
            view_available_slots()
        elif choice == "5":
            view_total_collection()
        elif choice == "6":
            print("\nThank you for using the Vehicle Parking Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
