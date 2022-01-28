"""
Project Name: Yondu Udonta.py
Author: Alyssa Smederovac Simmonds
Due Date: 02/05/2022
Course: CS1400-002

ORIGINAL
"""

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        #input variables
        
        # This asks how much money they enter the port with.
        print("What is the plunder when the reavers enter the port?")
        initial_plunder = int(input(""))
        print(f"You have entered {initial_plunder} units.")
        
        # This asks how many crew members there are.
        print("How many reavers are on the ship? (Including Yondu & Peter)")
        crew_members = int(input(""))
        print(f"You have entered {crew_members} reavers.")
        
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if crew_members < 1 or initial_plunder < 1:
        print("Enter positive integers for reavers and units.")
        return

    if crew_members < 3:
        print("Not enough crew.")
        return

    if initial_plunder <= 3 * crew_members:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    # Total amount of units after the crew goes out to celebrate
    post_lotus_total = initial_plunder-(3*(crew_members-2))

    # Yondus initial share
    yondus_share = post_lotus_total * .13
    yondus_share = int(yondus_share)

    # The total amount remaining after yondu takes his intitial share
    plunder = post_lotus_total - yondus_share

    # Peters initial share
    peters_share = plunder * .11
    peters_share = int(peters_share)

    # The total amount remaining after peter takes his initial share
    plunder = plunder-peters_share

    # Crew members final share
    crews_share = plunder/crew_members
    crews_share = int(crews_share)

    # Peters final share
    yondus_share += crews_share

    # Peters final share
    peters_share += crews_share

    # The total amount given to the rbf
    rbf = plunder-(crews_share*crew_members)

    # Prints the results
    print("Yondu's Share: " + str(yondus_share))
    print("Peter's Share: " + str(peters_share))
    print("Crew's Share: " + str(crews_share))
    print("RBF Total: " + str(rbf))

if __name__ == "__main__":
    main()








