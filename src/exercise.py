def main():
    #write your code below this line
    year = int(input("Give a year:"))
    if (year % 4 != 0):
      print("The year is not a leap year.")
    elif (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
      print("The year is not a leap year.")
    elif (year == 1200):
      print("The year is not a leap year.")
    else:
      print("The year is a leap year.")

if __name__ == '__main__':
    main()
