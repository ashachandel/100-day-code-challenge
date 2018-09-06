print("Enter 'x' for exit.");
len1 = input("Enter length of first side: ");
if len1 == 'x':
    exit();
else:
    len2 = input("Enter length of second side: ");
    len3 = input("Enter length of third side: ");
    length1 = int(len1);
    length2 = int(len2);
    length3 = int(len3);
    perimeter = length1 + length2 + length3;
    print("\nPerimeter of Triangle =", perimeter);
