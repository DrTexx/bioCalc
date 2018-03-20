"""
inheritance script, by Denver

SCRIPT IS CURRENTLY A BROKEN WIP
"""

from lib.dbi import dbi # import dbi for debugging
db = {'debug_active': True, 'verbosity_level': 3} # dictionary for dbi
dbi(db,3,"Successfully imported dbi!") # test dbi import

# define the person class
class Person:
    """
    Test gene inheritance based on different trait activation properties (e.g. linked to x chromosome)
    """
    def __init__(self,name,gender,chromosomes):
        self.name = name
        self.gender = gender
        self.chromosomes = chromosomes
        # bool for whether the first chromatid has an active or inactive version of the allele which causes the phenotype
        #self.chromatid1 = chromatid1
        #self.chromatid2 = chromatid2
    def testFor(self,trait):
        if (trait.sexLinked == False): #TEST IF LINKED TO X OR Y, THEN TEST IF DOMINANT, RETURN IF PHENOTYPE IS ACTIVE
            if (trait.dominant):
                if (self.chromatid1) or (self.chromatid2):
                    return True
                else:
                    return False
            else:
                if (not self.chromatid1) and (not self.chromatid2):
                    return True
                else:
                    return False
        elif (trait.sexLinked == 'x'):
            if (self.gender == 'male'):
                if (self.chromosomes[trait.name][cTid1]):
                    return True
                else:
                    return False
            elif (self.gender == 'female'):
                if (trait.dominant):
                    if (self.chromatid1) or (self.cTid2):
                        return True
                    else:
                        return False
                else:
                    if (not self.chromatid1) and (not self.cTid2):
                        return True
                    else:
                        return False
            else:
                print("Error: Gender invalid (this isn't Tumblr)")
        elif (trait.sexLinked == 'y'):
            if (self.gender == 'male'):
                if (trait.dominant):
                    if (self.chromatid2):
                        return True
                    else:
                        return False
                else:
                    if (not self.chromatid2):
                        return True
                    else:
                        return False
            elif (self.gender == 'female'):
                #Females cannot have an x-linked trait
                return False
            else:
                print("Error: Gender invalid (this isn't Tumblr)")
        else:
            print("ERROR: sexLinked is an invalid input")
    def calcGenotype(self,allele):
        chromatid1type = 'X'

        if (self.gender == 'male'):
            chromatid2type = 'Y'
        elif (self.gender == 'female'):
            chromatid2type = 'X'

        if (self.chromatid1):
            chromatid1power = allele.upper()
        else:
            chromatid1power = allele.lower()

        if (self.chromatid2):
            chromatid2power = allele.upper()
        else:
            chromatid2power = allele.lower()

        output = chromatid1type + chromatid1power + " " + chromatid2type + chromatid2power

        return output

class Phenotype:
    """
    Specify whether a trait is sexlinked or not (if so where) and whether it is dominant
    """
    def __init__(self,**kwargs):
        if 'name' in kwargs: self.name = kwargs['name']
        else: raise Exception("information in Phenotype class not specified")
        if 'sexLinked' in kwargs:
            if (kwargs['sexLinked'] is 'y' or 'x' or False):
                self.sexLinked = kwargs['sexLinked']
            else: raise Exception("sexLinked must be either 'male', 'female' or False")
        if 'dominant' in kwargs: self.dominant = kwargs['dominant']
        if 'allele' in kwargs: self.allele = kwargs['allele']

#script body
people = [
    Person(
        "John","male",chromosomes = {
            'haemophilia': {'trait': 'haemophilia','cTid1': True,'cTid2': False},
            'brownEyes': {'trait': 'brownEyes','cTid1': True,'cTid2': False},
            'maleInfertility': {'trait': 'maleInfertility','cTid1': True,'cTid2': False}
        }
    ),
    Person(
        "Jill","female",chromosomes = {
            'haemophilia': {'trait': 'haemophilia','cTid1': False,'cTid2': True},
            'brownEyes': {'trait': 'brownEyes','cTid1': False,'cTid2': True},
            'maleInfertility': {'trait': 'maleInfertility','cTid1': False,'cTid2': True}
        }
    ),
    Person(
        "Theodore","male",chromosomes = {
            'haemophilia': {'trait': 'haemophilia','cTid1': False,'cTid2': True},
            'brownEyes': {'trait': 'brownEyes','cTid1': False,'cTid2': True},
            'maleInfertility': {'trait': 'maleInfertility','cTid1': False,'cTid2': True}
        }
    ),
    Person(
        "Kanwal","male",chromosomes = {
            'haemophilia': {'trait': 'haemophilia','cTid1': True,'cTid2': True},
            'brownEyes': {'trait': 'brownEyes','cTid1': True,'cTid2': True},
            'maleInfertility': {'trait': 'maleInfertility','cTid1': True,'cTid2': True}
        }
    )
]

traits = {
    'haemophilia': Phenotype(name='haemophilia',sexLinked='x',dominant=False,allele='h'),
    'brownEyes': Phenotype(name='brownEyes',sexLinked=False,dominant=True,allele='b'),
    'maleInfertility': Phenotype(name='maleInfertility',sexLinked='y',dominant=True,allele='i')
}

for person in people:
    dbi(db,3,"root_object",str(type(person)))
    dbi(db,1,"name",person.name)
    dbi(db,1,"gender",person.gender)
    for chromosome in person.chromosomes:
        dbi(db,2,str(chromosome))
        dbi(db,1,str(person.chromosomes[chromosome]))
        #dbi(db,1,str(chromosome['trait']),str(chromosome['cTid1']),str(chromosome['cTid2']))


"""
tempName = raw_input("Person's name: ")
tempGender = raw_input("Are they male or female?: ")
tempChromatid1 = raw_input("First chromatid?: ")
tempChromatid2 = raw_input("Second chromatid?: ")
tempPerson = Person(tempName,tempGender,tempChromatid1,tempChromatid2)
people.append(tempPerson)
"""
for trait in traits:
    dbi(db,3,"root_object",str(type(trait)))
    dbi(db,2,"name",str(traits[trait].name))
    dbi(db,2,"sexLinked?:",str(traits[trait].sexLinked))
    dbi(db,2,"dominant?:",str(traits[trait].dominant))
    
    print(traits[trait])
    print(people[0].testFor(traits[trait]))
    
for person in people:
    print(str(person.name) + ":")
    for trait in traits:
        print(trait.name,"=",person.testFor(trait),"(",person.calcGenotype(trait.allele),")")