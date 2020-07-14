import random
def carte_to_chaine(di):
    s=""
    for el in di.keys():
        if el == 'valeur':
            s+=di['valeur']
        if el== 'couleur':
            e=di['couleur']
            if e=='P':
                e=chr(9824)
                s+=e
            elif e=='C':
                e= chr(9825)
                s+=e
            elif e=='K':
                e=chr(9826)
                s+=e
            else:
                e=chr(9827)
                s+=e
    return s

def afficher_reussite(l):
    for el in l:
        print(carte_to_chaine(el),end=" ")


def init_pioche_fichier(fail):
    d=dict()
    l = list()
    f = open(fail, 'r')
    s = ""
    for el in f:
        s += el
    for el in s:

        try:
            if int(el) or el == 'V' or el == 'D' or el == 'R' or el == 'A':
                d['valeur'] = el
                continue

        except:
            if el == 'V' or el == 'D' or el == 'R' or el == 'A':
                d['valeur'] = el
                continue
            elif el == '-':
                continue
            elif el == 'K' or el == 'P' or el == 'T' or el == 'C':
                d['couleur'] = el
                l.append(d)
                d = dict()
                continue
            else:
                pass
    f.close()
    return l


def forien(s):
    l=list()
    d=dict()
    for el in s:

        try:
            if int(el) or el == 'V' or el == 'D' or el == 'R' or el == 'A':
                d['valeur'] = el
                continue

        except:
            if el == 'V' or el == 'D' or el == 'R' or el == 'A':
                d['valeur'] = el
                continue
            elif el == '-':
                continue
            elif el == 'K' or el == 'P' or el == 'T' or el == 'C':
                d['couleur'] = el
                l.append(d)
                d = dict()
                continue
            else:
                pass

    return l
def ecrire_fichier_reussite(nom_fich, pioche):
    f = open(nom_fich, "w")
    for el in pioche:
        for el2 in el.keys():
            if el2 == 'valeur':
                f.write(str(el[el2]))
                f.write('-')
            else:
                f.write(str(el[el2]))
                f.write(" ")

    f.close()

def init_pioche_alea(nb_cartes):
    if nb_cartes==32:
        print("ici 32 cartes")
    elif nb_cartes==52:
        print("ici 52 cartes")
    else:
        print("il y a   ",nb_cartes," de cartes")
    votre_liste=input("donnez le nom du fichier pour ouvrir la liste\n")
    l=init_pioche_fichier(votre_liste)

    random.shuffle(l)

    return l


def alliance(carte1,carte2):
    if (carte1['valeur']==carte2['valeur']) or (carte1['couleur']==carte2['couleur']):

        return True
    else:
        return False
def saut_si_possible(liste_tas,num_tas):
    #print(liste_tas[num_tas],liste_tas[num_tas-1],liste_tas[num_tas+1])

    if alliance(liste_tas[num_tas-1],liste_tas[num_tas+1])==True:

        liste_tas[num_tas-1]=liste_tas[num_tas]
        liste_tas.pop(num_tas)
        #num_tas=num_tas-1
        #print("chislo ",num_tas)
        return True
    else:
        return False

def  une_etape_reussite(liste_tas,pioche,affiche):
    liste_tas.append(pioche.pop(0))
    if affiche:
        afficher_reussite(liste_tas)
    if saut_si_possible(liste_tas,(len(liste_tas)-2))==True:
        if affiche:
            afficher_reussite(liste_tas)
        try:
            for el in range(1,len(liste_tas)):
                if saut_si_possible(liste_tas,el)==True:
                    if affiche:
                        afficher_reussite(liste_tas)
                    break
                else:
                    continue
        except:
            pass

def reussite_mode_auto(pioche,affiche):
    if affiche:
        afficher_reussite(pioche)
        print("")
    p=list.copy(pioche)

    try:
        el=1
        while el<len(p)-1:
            if saut_si_possible(p,el)==True and affiche==True:
                afficher_reussite(p)
                if  el==1:
                    el=el-1
                else:
                    el=el-2
                print()
            else:
                if saut_si_possible(p,el):
                    if el==1:
                        el=el-1
                    else:
                        el=el-2
                    pass


            el=el+1


    except:

        pass


    return p

def reussite_mode_manuel(pioche,nb_tas_max):
    p=list.copy(pioche)
    print("Bonjour,bienvenu \n")
    file=input("Donnez le nom du fichier pour decouvrir touts les cartes \n")

    l=init_pioche_fichier(file)
    print("Voici,votre pioche initiale avec 3 cartes au debut \n")
    '''for el in range(3):

        print(carte_to_chaine(l[el]),end=" ")
    '''
    afficher_reussite(p)
    print()

    #afficher_reussite(p)
    reponse_menu(p,l)

    if nb_tas_max==len(p):
        print("Vous avez gagner \n")

    else:
        print("Vous etez perdu avec tas de nombre ",nb_tas_max)
    print("Au revoir!")
    return p



def reponse_menu(p,l):
    option=input("Vous choisissez 'P' pour decouvrir une carte, 'S' pour faire un saut,'F' pour laisser l'ordinateur finir la réussite ou 'Q' d'abandonner la partie \n")
    while option!="Q":
        if option=='P':
            p.append(l.pop(0))
            print("Apres modification ")

            afficher_reussite(p)
            print("")
            option=input("Vous choisissez 'P' pour decouvrir une carte, 'S' pour faire un saut,'F' pour laisser l'ordinateur finir la réussite ou 'Q' d'abandonner la partie \n")
        elif option=='S':
            demander_un_saut(p)
            option = input("Vous choisissez 'P' pour decouvrir une carte, 'S' pour faire un saut,'F' pour laisser l'ordinateur finir la réussite ou 'Q' d'abandonner la partie \n")
        elif option=='F':
            t=list()
            for el in range(len(l)):

                if l==list():
                    print("notre pioche de touts les cartes esst vide \n")
                    break

                p.append(l.pop(0))

                p=reussite_mode_auto(p,True)

            print("L'ordinateur  viens de firir ,tapez Q pour quitter")
            option = input("Vous choisissez 'P' pour decouvrir une carte, 'S' pour faire un saut,'F' pour laisser l'ordinateur finir la réussite ou 'Q' d'abandonner la partie \n")
        else:
            print("vous n'avez pas bien choisi la lettre ,essayez encore fois \n")
            option=input("Vous choisissez 'P' pour decouvrir une carte, 'S' pour faire un saut,'F' pour laisser l'ordinateur finir la réussite ou 'Q' d'abandonner la partie \n")
    if option=='Q' and len(l)>1:
        for el2 in range(len(l)):
            from time import sleep
            sleep(1)
            print(carte_to_chaine(l[el2]),end=" ")



def demander_un_saut(l):
    n=input("Votre indice de tas pour sauter .Attention, vous devez pas choisir un numero de tas sur le bord et un numero existant \n")
    while n==0 or n==(len(l)-1):
        n=input("Rechoisissez le numero")
    n=int(n)
    if saut_si_possible(l,n):
        print("Vous venez de sauter \n")
        afficher_reussite(l)
    else:
        print("Votre saute n'est pas autorisé")

def lance_reussite(mode,nb_cartes,affiche,nb_tas_max):
    p=init_pioche_alea(nb_cartes)

    if mode == 'manuel':
        return reussite_mode_manuel(p,nb_tas_max)
    elif mode == 'auto':
        return reussite_mode_auto(p,affiche)
    else:
        print("Vous avez pas bien choisi \n")
        mode=input("rechoisissez svp")

def res_multisimulation(nb_sim,nb_cartes):
    #l=init_pioche_alea(nb_cartes)
    l2=list()
    #print(l[0])
    #reussite_mode_manuel(l,False)
    for i in range(nb_sim):
        l = init_pioche_alea(nb_cartes)
        l3=list()
        l3=reussite_mode_auto(l,False)
        l2.append(len(l3))
    return l2

def statistiques_nb_tas(nb_sim,nb_cartes,):
    l=res_multisimulation(nb_sim,nb_cartes)
    print("le maximum du nombre de tas obtenus en jouant automatique est ",max(l))
    print("le minimum du nombre de tas obtenus en jouant automatique est ",min(l))
    s=0
    for i in range(len(l)):
       s+=l[i]
    print("la moyenne du nombre de tas obtenus en jouant automatique est ",s/len(l))




#f="V-C 8-P V-K A-C 10-P 8-T 8-K 9-T V-P A-P 10-K 9-P 7-T R-T 10-C 9-K 9-C D-T R-C 8-C D-K"
#forien(f)
s=init_pioche_fichier("data.txt")
#reussite_mode_auto(forien(f),True)
reussite_mode_manuel(s,2)

#print(res_multisimulation(3,32))








