spektri = {
    "varcna": (np.array([59.0, 58.5, 56.4, 56.2, 55.5]), ["lightblue", "green", "yellow", "orange", "red"]),
    "volframska":  (np.array([58.5, 57.0, 56.7, 55.9]), ["lightblue", "green", "orange", "red"]),
    "NO_2":  (np.array([58.5, 58.7, 57.7, 57.3, 56.6, 56.5, 55.4, 55.1]), ["lightblue", "blue", "green", "lime","greenyellow", "yellow", "orange", "tomato", "red" ]),
    "He": (np.array([59.2, 58.6, 58.4, 56.2, 55.5, 54.4]), ["darkblue", "navy", "lightblue",  "orange", "red", "red"]),
    "Ne": (np.array([57.4, 57.1, 56.2, 55.9, 55.8]), ["lightblue", "green", "greenyellow", "orange", "red"])
}

rezultati = []

def izracun(sez, a = 10.4, b = -0.2, c = 170.7):
    vrednosti = []
    sez = np.abs(sez - 360)

    for i in sez:
        if a**2 - 4*b*(c-i) < 0:
            vrednosti.append(None)
            i +=1
        r_plus = ( (-a + np.sqrt( a**2 - 4*b*(c-i))) / (2*b))**2
        #r_minus = ( (-a - np.sqrt( a**2 - 4*b*(c-i))) / (2*b))**2

        vrednosti.append(r_plus)

    zao_vrednosti = [(round(el, 2)) for el in vrednosti]

    with open("varcna.txt", "w") as f:
        for i,el in enumerate(sez):
            f.write("{}".format(el) + "& " + "{}".format(zao_vrednosti[i]) + "\\" + "\\" + "\n")




    rezultati.append(vrednosti)
    return vrednosti
# spreminjaj parameter 
izracun(spektri["varcna"][0])

