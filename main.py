#Gabriel Pérez Rivas A01644804
#Juan Pablo Guardado Báez A01644846
#Maximiliano Martínez Wirshup A01644198

import sys

mathConcepts=[]
mathBranch=[]

taskCompleted=False

class mElement():
    def __init__(self, name, explanation):
        self.conceptName=name
        self.explanation=explanation
    def giveExplanation(self):
        print("\n\n")
        print("------------------------------------------------------------------------------\n\n")
        print(self.conceptName.upper())
        print("------------------------------------------------------------------------------\n\n")
        print(self.explanation)
        print("\n¡Espero que te haya servido!\n")
        givenInput=""
        while (givenInput!="s") and (givenInput!="n"):
            givenInput=input("¿Necesitas que te ayude en algo más? (S/N): ").lower()
        if givenInput=="n":
            taskCompleted=True
            sys.exit(0)
        print("\n\n")

def printElements(elementType):
    for i in range(len(elementType)):
       print(f"{i+1} - {elementType[i].conceptName}")

def loadConceptList():
    concepts_name_file=open("concept_list.txt","r")
    concepts_definition=open("concept_definition.txt","r")
    nameList=concepts_name_file.readlines()
    definitionList=concepts_definition.readlines()
    for i in range(len(nameList)):
        mathConcepts.append(mElement(nameList[i],definitionList[i]))
    concepts_name_file.close()
    concepts_definition.close()

def loadBranchList():
    branch_name_file=open("branch_list.txt","r")
    branch_definition=open("branch_definition.txt","r")
    nameList=branch_name_file.readlines()
    definitionList=branch_definition.readlines()
    for i in range(len(nameList)):
        mathBranch.append(mElement(nameList[i],definitionList[i]))
    branch_name_file.close()
    branch_definition.close()

def getChosenElement():
    validInput=False
    while not (validInput):
        elementInput=input("¿Cómo te puedo ser de ayuda, quieres que te explique un concepto o una rama matemática? (Concepto/Rama/Nada): ").lower()
        if elementInput=="concepto":
         return mathConcepts
        elif elementInput=="rama":
         return mathBranch
        elif elementInput=="nada":
         taskCompleted=True
         validInput=True
        else:
            print("La entrada dada no es válida")
    
    if taskCompleted:
        sys.exit(0)

def getChosenTerm(_given_element):
    resultAttained=False
    givenTerm=""
    while not (resultAttained):
        givenTerm=input(f"Seleccione el número del elemento que quieres que explique [1-{len(_given_element)}]\n(En caso de un número fuera del rango se tomara el valor más cercano): ")
        try:
            int(givenTerm)
            resultAttained=True
        except:
            print("El número que seleccionó no es válido.")
    
    givenInput=min(max(1, int(givenTerm)), len(_given_element))-1
    print(f"El termino seleccionado fue el [{givenInput+1}] - {selectedElement[givenInput].conceptName}\n")
    return givenInput

loadConceptList()
loadBranchList()
while not (taskCompleted):
    selectedElement=getChosenElement()
    
    printElements(selectedElement)
    chosenTerm=getChosenTerm(selectedElement)
    selectedElement[chosenTerm].giveExplanation()

sys.exit(0)