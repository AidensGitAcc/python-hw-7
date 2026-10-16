# Chapter 7, Problem 3 — Ball Bouncing Simulation (text / console)
# A ball returns to 60% of its previous height on each bounce.
# Count bounces until the bounce height drops below 1 mm (0.001 m).

def main():
    height = float(input("Enter the initial drop height in meters: "))

    bounceHeight = height
    bounces = 0

    while bounceHeight >= 0.001:
        bounceHeight = bounceHeight * 0.6
        bounces = bounces + 1

    print()
    print("The ball bounced", bounces, "time(s) before the height fell below 1 mm.")

main()
