computer_parts = {"1": "Monitor",
                  "2": "Mouse",
                  "3": "CPU",
                  "4": "Keyboard",
                  "5": "mouse pad",
                  "6": "HDMI"}

current_choice = None

while current_choice != "0":
    if current_choice in computer_parts:
        print(f"adding computer part {computer_parts[current_choice]}")
    else:
        print("Available parts: ")
        for key, value in computer_parts.items():
            print(f"{key} : {value}")

    current_choice = input("> ")