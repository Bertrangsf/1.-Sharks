def Year(Case_Number):
    """
    Enter the Case_Number from which you want to extract the year.

    This function takes the first for digits frome the entered data 
    
    """

    for x in Case_Number:
        return Case_Number[:4] 

import pycountry 

def get_alpha_3(Country):
    try:
        return pycountry.countries.get(name=Country).alpha_3
    except:
        return None

import regex as re

def shark(x):
    x = str(x)
    
    white = re.search(r"[Ww](hite|HITE)", x)
    tiger = re.search(r'[a-z ]*?[san]?[d]?tiger[a-z ]* ?\W?', x)
    mako = re.search(r'[a-z ]*?mako[a-z ]* ?\W?', x)
    blue = re.search(r'[a-z ]*?blue[a-z ]* ?\W?', x)
    bull = re.search(r'[a-z ]*?bull[a-z ]* ?\W?', x)
    lemon = re.search(r'[a-z ]*?lemon[a-z ]* ?\W?', x)
    blacktip = re.search(r'[a-z ]*?blacktip[a-z ]* ?\W?', x)
    nurse = re.search(r'[a-z ]*?nurse[a-z ]* ?\W?', x)
    goblin = re.search(r'[a-z ]*?goblin[a-z ]* ?\W?', x)
    spinner = re.search(r'[a-z ]*?spinner[a-z ]* ?\W?', x)
    wobbegong = re.search(r'[a-z ]*?wobbegong[a-z ]* ?\W?', x)
    grey = re.search(r'[a-z ]*?grey[a-z ]* ?\W?', x)
    grey1 = re.search(r'[a-z ]*?gray[a-z ]* ?\W?', x)
    reef = re.search(r'[a-z ]*?reef[a-z ]* ?\W?', x)
    galapagos = re.search(r'[a-z ]*?galapagos[a-z ]* ?\W?', x)
    dogfish = re.search(r'[a-z ]*?dogfish[a-z ]* ?\W?', x)
    hammerhead = re.search(r'[a-z ]*?hammerhead[a-z ]* ?\W?', x)
    bronze = re.search(r'[a-z ]*?bronze[a-z ]* ?\W?', x)
    zambesi = re.search(r'[a-z ]*?zambesi[a-z ]* ?\W?', x)
    zambezi = re.search(r'[a-z ]*?zambezi[a-z ]* ?\W?', x)
    dusky = re.search(r'[a-z ]*?dusky[a-z ]* ?\W?', x)
    leopard = re.search(r'[a-z ]*?leopard[a-z ]* ?\W?', x)
    raggedtooth = re.search(r'[a-z ]*?raggedtooth[a-z ]* ?\W?', x)
    carpet = re.search(r'[a-z ]*?carpet[a-z ]* ?\W?', x)
    angel = re.search(r'[a-z ]*?angel[a-z ]* ?\W?', x)
    banjo = re.search(r'[a-z ]*?banjo[a-z ]* ?\W?', x)
    copper = re.search(r'[a-z ]*?copper[a-z ]* ?\W?', x)
    cleucas = re.search(r'[a-z ]*?cleucas[a-z ]* ?\W?', x)
    spurdog = re.search(r'[a-z ]*?spurdog[a-z ]* ?\W?', x)
    invalid = re.search(r'[a-z ]*?invalid[a-z ]* ?\W?', x)
    questionable = re.search(r'[a-z ]*?questionable[a-z ]* ?\W?', x)
    doubt = re.search(r'[a-z ]*?doubt[a-z ]* ?\W?', x)
    unidentif = re.search(r'[a-z ]*?unidentif[a-z ]* ?\W?', x)
    unkno = re.search(r'[a-z ]*?unkno[a-z ]* ?\W?', x)
    other = re.search(r'[a-z ]*?other[a-z ]* ?\W?', x)
    porbeagle = re.search(r'[a-z ]*?porbeagle[a-z ]* ?\W?', x)
    thresher = re.search(r'[a-z ]*?thresher[a-z ]* ?\W?', x)
    not_confirmed = re.search(r'[a-z ]*?not confirmed[a-z ]* ?\W?', x)
    broadnose = re.search(r'[a-z ]*?broadnose[a-z ]* ?\W?', x)
    basking = re.search(r'[a-z ]*?basking[a-z ]* ?\W?', x)
    not_a_shark_attack = re.search(r'[a-z ]*?not a shark attack[a-z ]* ?\W?', x)
    small = re.search(r'[a-z ]*?small[a-z ]* ?\W?', x)
    unknown = re.search(r'[a-z ]*?unknown[a-z ]* ?\W?', x)
    soupfin = re.search(r'[a-z ]*?soupfin[a-z ]* ?\W?', x)
    gill = re.search(r'[a-z ]*?gill[a-z ]* ?\W?', x)
    not_a_shark_attack = re.search(r'[a-z ]*?no shark[a-z ]* ?\W?', x)
    unknown1 = re.search(r'[a-z ]*?determined[a-z ]* ?\W?', x)
    unknown2 = re.search(r'[a-z ]*?kg[a-z ]* ?\W?', x)
    unknown3 = re.search(r'[a-z ]*?determined[a-z ]* ?\W?', x)
    unknown4 = re.search(r'[a-z ]*?unconfirmed[a-z ]* ?\W?', x)
    unknown5 = re.search(r'[a-z ]*?lb[a-z ]* ?\W?', x)
    invalid1 = re.search(r'[a-z ]*?not a shark[a-z ]* ?\W?', x)
    invalid2 = re.search(r'[a-z ]*?cm[a-z ]* ?\W?', x)
    invalid3 = re.search(r'[a-z ]*?tooth[a-z ]* ?\W?', x)
    invalid4 = re.search(r'[a-z ]*?0.[a-z ]* ?\W?', x)
    other1 = re.search(r'[a-z ]*?sharks[a-z ]* ?\W?', x)
    little = re.search(r'[a-z ]*?little[a-z ]* ?\W?', x)
    little1 = re.search(r'[a-z ]*?young[a-z ]* ?\W?', x)
    little2 = re.search(r'[a-z ]*?juve[a-z ]* ?\W?', x)
    whale = re.search(r'[a-z ]*?whale[a-z ]* ?\W?', x)
    sand = re.search(r'[a-z ]*?sand[a-z ]* ?\W?', x)
    silky = re.search(r'[a-z ]*?silky[a-z ]* ?\W?', x)
    dog = re.search(r'[a-z ]*?dog[a-z ]* ?\W?', x)
    cookiecutte =re.search(r'[a-z ]*?cookiecutte[a-z ]* ?\W?', x)

    seis_m = re.search(r'[a-z ]*?6.\d m[a-z ]* ?\W?', x)
    seis_m1 = re.search(r'[a-z ]*?6 m[a-z ]* ?\W?', x)

    cinco_m = re.search(r'[a-z ]*?5.\d m[a-z ]* ?\W?', x)
    cinco_m1 = re.search(r'[a-z ]*?5 m[a-z ]* ?\W?', x)
    cinco_m2 = re.search(r'[a-z ]*?5m[a-z ]* ?\W?', x)
   


    cuatro_m = re.search(r'[a-z ]*?4.\d m[a-z ]* ?\W?', x)
    cuatro_m1 = re.search(r'[a-z ]*?4 m[a-z ]* ?\W?', x)
    cuatro_m2 = re.search(r'[a-z ]*?4m[a-z ]* ?\W?', x)
    cuatro_m3 = re.search(r'[a-z ]*?12[a-z ]* ?\W?', x)
    cuatro_m4 = re.search(r'[a-z ]*?13[a-z ]* ?\W?', x)
    cuatro_m5 = re.search(r'[a-z ]*?14[a-z ]* ?\W?', x)
    cuatro_m6 = re.search(r'[a-z ]*?15[a-z ]* ?\W?', x)
    cuatro_m7 = re.search(r'[a-z ]*?16[a-z ]* ?\W?', x)

    tres_m = re.search(r'[a-z ]*?3.\d m[a-z ]* ?\W?', x)
    tres1 = re.search(r'[a-z ]*?3m[a-z ]* ?\W?', x)
    tres2 = re.search(r'[a-z ]*?3 m[a-z ]* ?\W?', x)
    tres3 = re.search(r'[a-z ]*?10. [a-z ]* ?\W?', x)
    tres4 = re.search(r'[a-z ]*?3.5 m[a-z ]* ?\W?', x)
    tres5 = re.search(r'[a-z ]*?3. m[a-z ]* ?\W?', x)

    dos_m = re.search(r'[a-z ]*?2.\d m[a-z ]* ?\W?', x)
    dos1 = re.search(r'[a-z ]*?> 2m[a-z ]* ?\W?', x)
    dos2 = re.search(r'[a-z ]*?2m[a-z ]* ?\W?', x)
    dos3 = re.search(r'[a-z ]*?2 m[a-z ]* ?\W?', x)
    dos4 = re.search(r'[a-z ]*?8. [a-z ]* ?\W?', x)
    dos5 = re.search(r'[a-z ]*?2.5 m[a-z ]* ?\W?', x)
    dos6 = re.search(r'[a-z ]*?2+ m[a-z ]* ?\W?', x)
    dos7 = re.search(r'[a-z ]*?7. [a-z ]* ?\W?', x)
    dos8 = re.search(r'[a-z ]*?9. [a-z ]* ?\W?', x)

    uno_m = re.search(r'[a-z ]*?1.\d m[a-z ]* ?\W?', x)
    uno_m7 = re.search(r'[a-z ]*?1m[a-z ]* ?\W?', x)
    uno_m1 = re.search(r'[a-z ]*?1 m[a-z ]* ?\W?', x)
    uno_m2 = re.search(r'[a-z ]*?>1 m[a-z ]* ?\W?', x)
    uno_m3 = re.search(r'[a-z ]*?3. [a-z ]* ?\W?', x)
    uno_m4 = re.search(r'[a-z ]*?4. [a-z ]* ?\W?', x)
    uno_m5 = re.search(r'[a-z ]*?5. [a-z ]* ?\W?', x)
    uno_m6 = re.search(r'[a-z ]*?6. [a-z ]* ?\W?', x)

    if white:
        return "white"
    if tiger:
        return "tiger"
    if mako:
        return "mako"
    if blue:
        return "blue"
    if bull:
        return "bull"
    if lemon:
        return "lemon"
    if blacktip:
        return "blacktip"
    if nurse:
        return "nurse"
    if goblin:
        return "goblin"
    if spinner:
        return "spinner"
    if wobbegong:
        return "wobbegong"
    if grey:
        return "grey"
    if grey1:
        return "grey"
    if reef:
        return "reef"
    if galapagos:
        return "galapagos"
    if dogfish:
        return "dogfish"
    if hammerhead:
        return "hammerhead"  
    if bronze:
        return "bronze"
    if zambesi:
        return "zambesi"  
    if zambezi:
        return "zambesi" 
    if dusky:
        return "dusky" 
    if leopard:
        return "leopard" 
    if raggedtooth:
        return "raggedtooth" 
    if carpet:
        return "carpet"
    if angel:
        return "angel"
    if banjo:
        return "banjo"
    if copper:
        return "copper"
    if porbeagle:
        return "porbeagle"
    if thresher:
        return "thresher"
    if broadnose:
        return "broadnose"
    if basking:
        return "basking"
    if not_a_shark_attack:
        return "invalid"
    if small:
        return "small"
    if soupfin:
        return "soupfin"
    if tres_m:
        return "> 3m"
    if tres1:
        return "> 3m"
    if tres2:
        return "> 3m"
    if tres3:
        return "> 3m"
    if tres4:
        return "> 3m"
    if tres5:
        return "> 3m"
    if dos_m:
        return "> 2m"
    if dos1:
        return "> 2m"
    if dos2:
        return "> 2m"
    if dos3:
        return "> 2m"
    if dos4:
        return "> 2m"
    if dos5:
        return "> 2m"
    if dos6:
        return "> 2m"
    if dos7:
        return "> 2m"
    if dos8:
        return "> 2m"
    if cookiecutte:
        return "cookiecutte"
    if dog:
        return "dog"
    if uno_m:
        return "> 1m"
    if uno_m1:
        return "> 1m"
    if uno_m2:
        return "> 1m"
    if uno_m3:
        return "> 1m"
    if uno_m4:
        return "> 1m"
    if uno_m5:
        return "> 1m"
    if uno_m6:
        return "> 1m"
    if uno_m7:
        return "> 1m"
    if seis_m:
        return "> 6m"
    if seis_m1:
        return "> 6m"
    if silky:
        return "silky"
    if cinco_m:
        return "> 5m"
    if cinco_m1:
        return "> 5m"
    if cinco_m2:
        return "> 5m"
    if other1:
        return "other"
    if cuatro_m1:
        return "> 4m"
    if cuatro_m2:
        return "> 4m"
    if cuatro_m3:
        return "> 4m"
    if cuatro_m4:
        return "> 4m"
    if cuatro_m5:
        return "> 4m"
    if cuatro_m6:
        return "> 4m"
    if cuatro_m7:
        return "> 4m"
    if uno_m:
        return "> 1m"
    if gill:
        return "gill"
    if whale:
        return "whale"
    if sand:
        return "sand"
    if seis_m:
        return "seis_m"
    if little:
        return "small"
    if little1:
        return "small"
    if little2:
        return "small"
    if unknown:
        return "other"
    if unknown1:
        return "other"
    if unknown2:
        return "other"
    if unknown3:
        return "other"
    if unknown4:
        return "other"
    if unknown5:
        return "other"
    if invalid:
        return "invalid"
    if invalid1:
        return "invalid"
    if invalid2:
        return "invalid"
    if invalid3:
        return "invalid"
    if invalid4:
        return "invalid"
    if questionable:
        return "invalid"
    if doubt:
        return "invalid"
    if unidentif:
        return "invalid"
    if unkno:
        return "invalid"
    if other:
        return "other"
    if not_confirmed:
        return "invalid"
    else:
        return "other"
