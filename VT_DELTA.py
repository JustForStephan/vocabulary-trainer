#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import os
from pathlib import Path
killlist = []
list(killlist)
RightAnswerContainer = 0
FalseVokabulary = []
list(FalseVokabulary)
Exitextension = False
i = 0
# deletes all not-handable files
def notExecutable(Files,path):
    f = 0     
    while f < len(Files):
        if ".txt" in Files[f] or isFile(Files[f],path) == True:
            f = f +1
        else:
            del Files[f]
        
    return Files
    
# this function reads the file you chose, converts into an list, and remotes all whitspaces and void areas
def IFELSE(RightWord, answer):
    
    extension = False
    
    if(RightWord.find('/') > -1):
        Position = RightWord.find('/')
        word1 = RightWord[:Position]
        word2 = RightWord[Position+1:]
        
        word1 = word1.strip()
        word2 = word2.strip()
    
        changed = word2 + "/" + word1
    
        if answer == word1 or answer == word2 or answer == changed:
            extension = True
    
    return(extension)


def isFile(value,path):
    try: 
        os.chdir(path)
        os.chdir(value)
        return True
    except BaseException:
        return False
    
def filereader(File,path):
   
    #copy the content of the file
    os.chdir(path)
    f = open(File)
    file = f.read()
    f.close()
    
    #converts the content to an list        
    file = file.replace("=", "\n")
    file = file.split("\n")
    
    # remotes all whitspaces
    file = [x.strip() for x in file]
    
    lengh = len(file)
    ii = 0
    
    #remotes all void areas
    while ii < lengh:
        if file[ii] == "":
            del file[ii]
            lengh = lengh -1
        else:
            ii = ii +1 

    return(file)
    
def Controller(Answer, Files):
    try: 
        Answer = int(Answer)-1
        if Answer < 0 or Answer >= len(Files):
            print("The number \"",Answer,"\" is invalid")
            return False
        else: 
            return True
    except BaseException:
        print("The dicision \"",Answer,"\"is invalid")
        return False
    
while Exitextension == False:
    
    path = Path(__file__).parent.absolute()
    
    #search the suitable file
    while True:
        
        Files = os.listdir(path)
        Files = notExecutable(Files, path)
        i = 0
        print("\nThere are all executable files in actual directory:\n")
        while i < len(Files):
            print(i+1,": ",Files[i])
            i = i+1
        print(i +1,":  Go Back")
        answer = input("Decision: ")
        if int(answer) == len(Files)+1:
            path= path.joinpath("..")
            continue
        if Controller(answer, Files) == False:
            continue
        if isFile(Files[int(answer)-1], path) == True:
            path = path.joinpath(Files[int(answer)-1])
            print("You chose the directory: \"",Files[int(answer)-1],"\.")
            continue
        else:
            File = Files[int(answer)-1]
            break
        

        
    dictionary = filereader(File,path)
    Strings = len(dictionary)
    
    print('\n')    
    print('-----------------------------------------------------------')
    print('\nYou chose the file: ',Files[int(answer)-1],'\n')
    print('The file is loaded...\n')
        
    
    if dictionary == []:
        print('There are no content in the file you have chosen!')
        print('Please overwrite this file or take another file!')
        i = Strings
    
    else:
        print('Please enter the translation of the following words:\n')
        print('\n')
            
    l = []
    i = 0
    while i < Strings:
        
        randomgenerator = randint(0,Strings-1)
            
        if(randomgenerator in killlist):
            k = 2
            
        else:
            print('Given word: ',dictionary[randomgenerator])
            killlist.append(randomgenerator)
            Answer = input('Translation: ')
            Answer = Answer.strip()    
            
            try:
                if randomgenerator %2:
                    BeforeRandomgenerator = randomgenerator -1
                    Translation = dictionary[BeforeRandomgenerator]
                        
                else:
                    AfterRandomgenerator = randomgenerator +1
                    Translation = dictionary[AfterRandomgenerator]
            except BaseException:
                print("The content of the file is invalid, \"",dictionary[randomgenerator],"\" has no simular word!")
                break
                    
            if Answer == Translation or IFELSE(Translation, Answer):
                print('All right!')
                print('\n')
                
                RightAnswerContainer = RightAnswerContainer +1
                    
            
            else:
                print('False, try it later again!')
                FalseVokabulary.append(dictionary[randomgenerator])
                print('\n')

            i = i +1
                
                
                
            if(i == Strings):
                
                
                if (RightAnswerContainer != Strings):
                    print('Do you wand to repeat wrong words?')
                    
                    Answer = input('Press "y" to correct, else press "n". ')
                    
                    if Answer == "Y" or Answer == "y" or Answer == "yes" or Answer == "Yes":
                        print("\n")
                        print("Please translate the following words:")
                        print("\n")
                        
                        le = len(FalseVokabulary)
                        j = 0
                        while j < le:
                            print('Given word: ', FalseVokabulary[j])
                            Answer = input('Translation: ')
                            position = dictionary.index(FalseVokabulary[j])
                            
                            if position %2:
                                PAnswer = position -1
                                Translation = dictionary[PAnswer]
                    
                            else:
                                PAnswer = position +1
                                Translation = dictionary[PAnswer]
                            
                            if Answer == Translation or IFELSE(Translation,Answer):
                                print('\nAll right!')
                                print('\n')
                                print('\n')
                                RightAnswerContainer = RightAnswerContainer +1
                    
            
                            else:
                                print('\nThat is not true!')
                                print('the right answer would have been: ', Translation)
                                print('\n')
                                print('\n')
                                
                            j = j +1
            
                                              
                            
                #makes an relationship of the right translated vocabularies to all vocabularies
                print('\nYou did it!\n')
                print(RightAnswerContainer,'of',Strings ,'vocabulary where translated correctly.')
                Grade = RightAnswerContainer / Strings
                
                        
                # write the grade of learning in the terminal
                
                if Grade <= 25 / 100:
                    print('You must learn more! In a test this skill would be 0 points! (in Germany).')
                
                elif Grade <= 30 / 100 and Grade > 25 / 100:
                    print('You must learn more! In a test this skill would be 1 point (in Germany).')
    
                elif Grade < 35 / 100 and Grade > 30 / 100:
                    print('You must learn more! In a test this skill would be 2 points (in Germany).')
                
                elif Grade <= 40 / 100 and Grade > 35 / 100:
                    print('You must learn more! In a test this skill would be 3 points (in Germany).')
                
                elif Grade <= 45 / 100 and Grade > 40 / 100:
                    print('You must learn more! In a test this skill would be 4 points (in Germany).')
                            
                elif Grade <= 50 / 100 and Grade > 45 / 100:
                    print('You must learn more! In a test this skill would be 5 points (in Germany).')
    
                elif Grade < 55 / 100 and Grade > 50 / 100:
                    print('You must learn more! In a test this skill would be 6 points (in Germany).')
                
                elif Grade <= 60 / 100 and Grade > 55 / 100:
                    print('Not that sufficient. In a test this skill would be 7 (in Germany).')
                
                elif Grade <= 65 / 100 and Grade > 60 / 100:
                    print('Not that sufficient. In a test this skill would be 8 points (in Germany).')
                            
                elif Grade <= 70 / 100 and Grade > 65 / 100:
                    print('Not that sufficient. In a test this skill would be 9 points (in Germany).')
    
                elif Grade < 75 / 100 and Grade > 70 / 100:
                    print('In a test this skill would be 10 points (in Germany).')
                
                elif Grade <= 80 / 100 and Grade > 75 / 100:
                    print('In a test this skill would be 11 (in Germany).')
                
                elif Grade <= 85 / 100 and Grade > 80 / 100:
                    print('In a test this skill would be 12 points (in Germany).')
                            
                elif Grade <= 90 / 100 and Grade > 85 / 100:
                    print('In a test this skill would be 13 points (in Germany).')
    
                elif Grade < 95 / 100 and Grade > 90 / 100:
                    print('Close to perfect! In a test this skill would be 14 points (in Germany).')
                        
                else:
                    print('You have a great mind! In an test this skill would be 15 points (in Germany).')
    
                #if Grade <= 30 / 100:
                #    print('You must learn more! In an test this skill would be the grade 6 (in Germany).')
                                
                #elif Grade <= 50 / 100 and Grade > 30 / 100:
                #    print('Not really good! In an test this skill would be the grade 5 (in Germany).')
                
                #elif Grade <= 67 / 100 and Grade > 50 / 100:
                #    print('In an test this skill would be the grade 4 (in Germany).')
                            
                #elif Grade <= 81 / 100 and Grade > 67 / 100:
                #    print('It is sufficient! In an test this skill would be the grade 3 (in Germany).')
    
                #elif Grade <= 92 / 100 and Grade > 81 / 100:
                #    print('Close to perfect! In an test this skill would be the grade 2 (in Germany).')
                        
                #else:
                #    print('You have a great mind! In an test this skill would be the grade 1 (in Germany).')
    


                print('\n')
                print('-----------------------------------------------------')
                print('Thanks for using applications from Just for Stephan! ')
                print('-----------------------------------------------------\n')
                    
                print('Press "exit" to stop the training.')
                print('Press "home" to take another vocabulary file.')
                print('Press "enter" to restart the training.\n')
                Answer = input("decision: ")
                print('\n---------------------------------------------------')
                mAnswer = False
                while mAnswer == False:
                
                    if Answer == "exit" or Answer == "Exit":
                        print("\nThe program is terminated!\n")
                        Exitextension = True
                        k = True
                        mAnswer = True
            
                    elif Answer == "home" or Answer == "Home":
                        print('\nWelcome Home!\n')
                        
                        killlist = []
                        FalseVokabulary = []
                        
                        RightAnswerContainer = 0
                        j = 0 
        
                        mAnswer = True
        
                    elif Answer == 'enter' or Answer == 'Enter' or Answer == "":
                        print('\nThe training will restart!\n')
                        print('Please enter the translation of the following words:')
                        print('\n')
                        
                        killlist = []
                        FalseVokabulary = []    
                        
                        j = 0
                        i = 0
                        RightAnswerContainer = 0 
                        
                        mAnswer = True

                    else:
                        print('\nPlease take one of the given words!\n')                
                        print('Press "exit" to stop the training.')
                        print('Press "home" to take another vocabulary file.')
                        print('Press "enter" to restart the training.\n')
                        Answer = input('decision: ')
        
            else:
                kdfj = 1
