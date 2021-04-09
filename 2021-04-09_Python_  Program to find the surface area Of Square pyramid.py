#Python program to find the surface area Of Square pyramid
"Computer Programming Tutor_April 9,2021"

#Function to find the Surface area

def surfaceArea(b,s):
    return 2*b*s + pow(b,2)

if __name__=="__main__":
    b =float(input("Base Length of Square Pyramid: "))
    s =float(input("Slant Height of The Square Pyramid: "))

    # Surface area of the Square Pyramid
    print("Surface Area of The Square Pyramid", surfaceArea(b,s))
