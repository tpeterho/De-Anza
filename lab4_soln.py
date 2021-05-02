# This script is set up to solve linear equations through brute force .

def linear():
        x = -100
        while x < 100:
                if 2*x + 5 == 13:
                        print("The solution is")
                        print("   x =",x)
                        break
                x += 1

def double():
        x = 0.0
        while x < 100.0:
                y = 0.0
                while y < 100.0:
                        if 2.0*x+3.0*y == 20.0:
                                print("(R, \u0394V) =",(x,y),type=float)
                        y += 1
                x+=1
                
# tell script to run the function double()
double()
