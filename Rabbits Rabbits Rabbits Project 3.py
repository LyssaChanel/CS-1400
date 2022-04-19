
def do_research(cages, adults, babies):
    total_rab = adults + babies
    month = 1
    print(month, adults, babies, total_rab)
    while total_rab < cages:
        babies = adults
        adults = total_rab
        total_rab = babies + adults
        month += 1
        print(month, adults, babies, total_rab)
        # output_file = open("users/alyss/OneDrive/desktop/coding/python/rabbits.csv", "w")
        # output_file.writelines(month + ", " + adults + ", " + babies + ", " + total_rab)
        # output_file.close()
        
do_research(500, 1, 0)
