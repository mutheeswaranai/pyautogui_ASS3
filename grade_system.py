def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

while True :
    try:
        mark = float(input("Enter Your Mark : "))
        if 0 <= mark <=100:
              grade=get_grade(mark)
              print( " Mark ", mark)
              print( f" Grade {grade}")
              break
              
        else:
                print(" Please enter mark between 0 and 100 .")

    except ValueError:
         print (" please enter a valid number ")