import random
import time
import tkinter as tk
from tkinter import messagebox, ttk

BASE_FARE = 20  
FARE_PER_KM = 10  

class RapidoRide:
    def __init__(self, customer_name, pickup_location, drop_location):
        self.customer_name = customer_name
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.distance = self.calculate_distance()
        self.fare = self.calculate_fare()
        self.status = "Booked"

    # Riders data
    riders = {
        "rider1": {
            'name': 'Rider1',
            'location': 14,
            'mobile no': 1234,
            "avaliable": True,
        },
        "rider2": {
            "name": "Rider2",
            "location": 2,
            "mobile no": 5678,
            "avaliable": True,
        },
        "rider3": {
            "name": "Rider3",
            "location": 5,
            "mobile no": 9101,
            "avaliable": False,
        },
        "rider4": {
            "name": "Rider4",
            "location": 4,
            "mobile no": 1121,
            "avaliable": True,
        }
    }

    def calculate_distance(self):
        return random.randint(2, 15)

    def calculate_fare(self):
        return BASE_FARE + (self.distance * FARE_PER_KM)


def find_closest_rider(riders):
    available_riders = {
        rider_id: details
        for rider_id, details in riders.items()
        if details["avaliable"]
    }
    
    if not available_riders:
        return None
    
    closest_rider = min(
        available_riders.items(),
        key=lambda item: abs(item[1]["location"])
    )
    
    return {
        "name": closest_rider[1]["name"],
        "mobile no": closest_rider[1]["mobile no"]
    }


def book_ride():
    customer_name = name_entry.get()
    pickup_location = pickup_var.get()
    drop_location = drop_var.get()

    if not customer_name or pickup_location == "Select" or drop_location == "Select":
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    ride = RapidoRide(customer_name, pickup_location, drop_location)

    closest_rider = find_closest_rider(RapidoRide.riders)
    if closest_rider is None:
        messagebox.showinfo("No Riders", "No riders available at the moment.")
        return

    ride_details = (
        f"Customer: {ride.customer_name}\n"
        f"Pickup: {ride.pickup_location}\n"
        f"Drop: {ride.drop_location}\n"
        f"Distance: {ride.distance} km\n"
        f"Estimated Fare: ₹{ride.fare}\n"
        f"Rider Assigned: {closest_rider['name']} (Mobile: {closest_rider['mobile no']})"
    )
    messagebox.showinfo("Ride Details", ride_details)

    progress_label["text"] = "On the Move: Your Status"
    for i in range(100):
        ride_progress["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.5)

    ride.status = "Completed"
    progress_label["text"] = "Ride Completed!"
    messagebox.showinfo("Ride Completed", f"Ride completed. Total fare: ₹{ride.fare}")


# GUI Setup
root = tk.Tk()
root.title("Rapido Ride Booking")
root.geometry("600x400")
root.configure(bg="#EAF6FF")

# Title Section
title_frame = tk.Frame(root, bg="#003366", height=60)
title_frame.pack(fill="x")
title_label = tk.Label(
    title_frame,
    text="🚴 Rapido Ride Booking 🚴",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="blue",
)
title_label.pack(pady=10)

# Input Section
form_frame = tk.Frame(root, bg="#EAF6FF")
form_frame.pack(pady=20)

tk.Label(form_frame, text="Customer Name:", font=("Arial", 12), bg="#EAF6FF").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(form_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Pickup Location:", font=("Arial", 12), bg="#EAF6FF").grid(row=1, column=0, padx=10, pady=5)
pickup_var = tk.StringVar(value="Select")
pickup_menu = ttk.Combobox(
    form_frame, textvariable=pickup_var, font=("Arial", 12), state="readonly"
)
pickup_menu["values"] = ["Warangal", "Hanamkonda", "Kazipet", "Hunter Road", "Subedari"]
pickup_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Drop Location:", font=("Arial", 12), bg="#EAF6FF").grid(row=2, column=0, padx=10, pady=5)
drop_var = tk.StringVar(value="Select")
drop_menu = ttk.Combobox(
    form_frame, textvariable=drop_var, font=("Arial", 12), state="readonly"
)
drop_menu["values"] = ["Warangal", "Hanamkonda", "Kazipet", "Hunter Road", "Subedari"]
drop_menu.grid(row=2, column=1, padx=10, pady=5)

# Book Ride Button
book_button = tk.Button(
    root,
    text="Book Ride",
    font=("Arial", 14, "bold"),
    bg="#00A86B",
    fg="white",
    relief="raised",
    command=book_ride,
)
book_button.pack(pady=20)

# Ride Progress
progress_label = tk.Label(root, text="", font=("Arial", 12), bg="#EAF6FF", fg="black")
progress_label.pack()

ride_progress = ttk.Progressbar(root, length=300, mode="determinate")
ride_progress.pack(pady=10)

# Run the application
root.mainloop()
