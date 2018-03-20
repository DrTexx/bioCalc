"""
inheritance script, by Denver
"""

from lib.dbi import dbi
db = {'debug_active': True, 'verbosity_level': 3}

dbi(db,3,"Successfully imported dbi!")

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
        #TEST IF LINKED TO X OR Y, THEN TEST IF DOMINANT, RETURN IF PHENOTYPE IS ACTIVE
        if (sexLinked == False):
            if (dominant):
                if (self.chromatid1) or (self.chromatid2):
                    return True
                else:
                    return False
            else:
                if (not self.chromatid1) and (not self.chromatid2):
                    return True
                else:
                    return False
        elif (sexLinked == 'x'):
            if (self.gender == 'male'):
                if (self.chromatid1):
                    return True
                else:
                    return False
            elif (self.gender == 'female'):
                if (dominant):
                    if (self.chromatid1) or (self.chromatid2):
                        return True
                    else:
                        return False
                else:
                    if (not self.chromatid1) and (not self.chromatid2):
                        return True
                    else:
                        return False
            else:
                print("Error: Gender invalid (this isn't Tumblr)")
        elif (sexLinked == 'y'):
            if (self.gender == 'male'):
                if (dominant):
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
people = []
father = Person(
    "John",
    "male",
    chromosomes = [
        {'trait': 'haemophilia','cTid1': True,'cTid2': False},
        {'trait': 'brownEyes','cTid1': True,'cTid2': False},
        {'trait': 'maleInfertility','cTid1': True,'cTid2': False}
    ]
#True,False
)
people.append(father)

for person in people:
    print(person)
    print(person.name)
    print(person.gender)
    print(person.chromosomes)
    for chromosome in person.chromosomes:
        print(chromosome['trait'],chromosome['cTid1'],chromosome['cTid2'])
        
        
        


mother = Person(
    "Jill",
    "female",
    chromosomes = [
        {'trait': 'haemophilia','cTid1': False,'cTid2': True},
        {'trait': 'brownEyes','cTid1': False,'cTid2': True},
        {'trait': 'maleInfertility','cTid1': False,'cTid2': True}
    ]
)
grandpa = Person(
    "Theodore",
    "male",
    [
        {'trait': 'haemophilia','cTid1': False,'cTid2': True},
        {'trait': 'brownEyes','cTid1': False,'cTid2': True},
        {'trait': 'maleInfertility','cTid1': False,'cTid2': True}
    ]
)
kanwal = Person(
    "Kanwal",
    "male",
    [
        {'trait': 'haemophilia','cTid1': True,'cTid2': True},
        {'trait': 'brownEyes','cTid1': True,'cTid2': True},
        {'trait': 'maleInfertility','cTid1': True,'cTid2': True}
    ]
)
people.append(father)
people.append(mother)
people.append(grandpa)
people.append(kanwal)

traits = {
    'haemophilia': Phenotype(name='haemophilia',sexLinked='x',dominant=False,allele='h'),
    'brownEyes': Phenotype(name='brownEyes',sexLinked=False,dominant=True,allele='b'),
    'maleInfertility': Phenotype(name='maleInfertility',sexLinked='y',dominant=True,allele='i')
}

"""
tempName = raw_input("Person's name: ")
tempGender = raw_input("Are they male or female?: ")
tempChromatid1 = raw_input("First chromatid?: ")
tempChromatid2 = raw_input("Second chromatid?: ")
tempPerson = Person(tempName,tempGender,tempChromatid1,tempChromatid2)
people.append(tempPerson)
"""

for person in people:
    print("name:",person.name)
    print("gender:",person.gender)
    for trait in person.chromosomes:
        print("cTid1:",trait.cTid1)
        print("cTid2:",trait.cTid2)
    print
print("--------")
for trait in traits:
    print("name:",trait.name)
    print("sexLinked?:",trait.sexLinked)
    print("dominant?:",trait.dominant)
print("--------")
for person in people:
    print(str(person.name) + ":")
    for trait in traits:
        print(trait.name,"=",person.testInheritance(trait.sexLinked,trait.dominant),"(",person.calcGenotype(trait.allele),")")
    print
raw_input("PRESS <ENTER> TO CONTINUE")