def main():
    choice = input('Press q to Quit or E to Enter:')

    while choice == "E"or choice=="e":
        deg_fahrenheit = float(input("Put fahrenheit to get degrees in celsius:"))
        deg_celsius = int((deg_fahrenheit - 32) / 1.8)
        print (deg_fahrenheit,"fahrenheit converts to", deg_celsius, "degrees Celsius .")
        choice = input('Press q to Quit or E to Enter:')

    if choice =="q":
        exit()
main()
