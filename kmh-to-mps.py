def kmh_to_mps(kmh):
    mps = (kmh*10)/36
    return mps

def mps_to_kmh(mps):
    kmh = mps * 3.6
    return kmh

while True:
    choice = input("kmh to mps: 1\nmps to kmh: 2\nQuit: 3\nYour Choice: ")
    if choice == "1":
        kmh = int(input("Your Kmh: "))
        mps = kmh_to_mps(kmh)
        print(f"Your Mps: {mps}")
    elif choice == "2":
        mps = int(input("Your Mps: "))
        kmh = mps_to_kmh(mps)
        print(f"Your Kmh: {kmh}")
    elif choice == "3":
        print("Closing...")
        break
    else:
        print("Wrong choice\n\n\n")
