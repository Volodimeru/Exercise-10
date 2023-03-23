def main():
    dro = input("What time is it? ")
    time = convert(dro)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
def convert(h):
    hh, mm = h.split(":")
    mm = float(mm) / 60
    return float(hh) + float(mm)
if __name__ == "__main__":
    main()