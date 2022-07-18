computer_parts = []
current_choice = '-'

while current_choice != '0':
    if current_choice in "12345":
        print(f"Adding parts {current_choice}")
        if current_choice == '1':
            computer_parts.append("CPU")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        elif current_choice == '3':
            computer_parts.append("mouse")
        elif current_choice == '4':
            computer_parts.append("Keyboard")
        elif current_choice == '5':
            computer_parts.append("HDMI")
    else:
        print("1. CPU")
        print("2. Monitor")
        print("3. mouse")
        print("4. keyboard")
        print("5. HDMI")
        print("0: finish")

    current_choice = input()

print(computer_parts)