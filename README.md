# Vehicle Parking Management System

A simple Python-based **Vehicle Parking Management System** designed to manage vehicles entering and leaving a parking area. The system keeps track of parked vehicles, parking slots, vehicle types, and parking charges through a menu-driven interface.

## Objectives

- Maintain vehicle parking records
- Assign available parking slots
- Keep track of parked vehicles
- Calculate parking charges
- Manage vehicle entry and exit
- Reduce manual calculation and record-keeping

## Features

- Park a vehicle
- Automatically assign an available parking slot
- View parked vehicles
- View available parking slots
- Remove a vehicle when it exits
- Calculate parking fees
- Display total parking collection
- Simple menu-driven interface
- Input validation for vehicle type and parking duration

## Technology Used

- **Programming Language:** Python
- **Development Environment:** Python IDLE / VS Code
- **Concepts Used:** Variables, Lists, Dictionaries, Functions, Loops, Conditional Statements, and Exception Handling

## Parking Rates

| Vehicle Type | Rate per Hour |
|--------------|---------------|
| Bike         | ₹20           |
| Car          | ₹40           |

The system supports a maximum of **10 parking slots**.

## How to Run the Program

1. Install Python on your computer.
2. Open VS Code, Python IDLE, or another Python editor.
3. Place `vehicle_parking.py` in your project folder.
4. Open a terminal in that folder.
5. Run the following command:

```bash
python vehicle_parking.py

===================================
 VEHICLE PARKING MANAGEMENT SYSTEM
===================================
1. Park Vehicle
2. View Parked Vehicles
3. Vehicle Exit
4. View Available Slots
5. View Total Collection
6. Exit

##Example output
Parking a Vehicle

Enter your choice: 1
Enter vehicle number: MP04AB1234
Enter vehicle type (Bike/Car): Car

Vehicle parked successfully!
Vehicle Number: MP04AB1234
Vehicle Type: Car
Parking Slot: 1

Vehicle Exit
Enter vehicle number: MP04AB1234
Vehicle Type: Car
Enter parking duration in hours: 3

===== PARKING RECEIPT =====
Vehicle Number: MP04AB1234
Vehicle Type: Car
Parking Slot: 1
Parking Duration: 3 hour(s)
Parking Fee: ₹ 120
Vehicle exited successfully!