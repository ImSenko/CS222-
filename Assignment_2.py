def main():
    ###Getting Basic Info From User
    NP = int(input("Please enter the number of guests: "))
    HPP = int(input("Please enter the number of hotdogs each person will be given: "))

    # Calculate the total number of hotdogs needed
    HN = NP * HPP
    if HN % 10 == 0:
        PHD = HN // 10
    else:
        PHD = (HN // 10) + 1

    # Calculate the number of packages of buns needed
    if HN % 8 == 0:
        PB = HN // 8
    else:
        PB = (HN // 8) + 1

    # Calculate the number of hotdogs and buns left over
    HLO = (PHD * 10) - HN
    BLO = (PB * 8) - HN

    # Print the results
    print("The number of packages of hotdogs needed is:", PHD)
    print("The number of packages of buns needed is:", PB)
    print("The number of hotdogs left over is:", HLO)
    print("The number of buns left over is:", BLO)

main()