def protein_energy_temp():
    T = 70


    def calculate_free_energy(H,entropy):
        G = H-T*entropy
        return G

    result =calculate_free_energy(350, 10)

    if result < 0:
        return "stable"
    else:
        return "unstable"


print(protein_energy_temp())
