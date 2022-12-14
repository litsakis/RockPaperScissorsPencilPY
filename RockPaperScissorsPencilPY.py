import random
#Its the classic game Rock Paper Scissors. AI vs User
#The rules is that 
#Rock beats Paper Pencil and Scissors
#Paper beats Rock
#Scissors beats Paper and Pencil
#Pencil beats Paper 

def main():
    print ("Lets Play Rock Paper Scissors Pencil Game!")
    print ('can you win the AI?')
    
    random.seed(10)
    AiScore=0 # init the Score
    YourScore=0
    while (True):
        ai=random.randint(1,4) # AI make a random choice

        print ('--'*20) # printing a line
        inp =input ('''
        
        Press 1 to choose Rock
        Press 2 to choose Paper
        Press 3 to choose Scissors
        Press 4 to choose Pencil
        Press 0 to EXIT!
        ''')
        try: 
         if (int(inp) not in range(5)):# prevent wrong input
          print ('Please choose between  0-4!')
          continue
          
        except:# prevent null choice - case when user press only enter
         print ('Please make a choice!')
         continue
        gcase=int(inp)*10+ai #unify the options of User and AI into one int
        # e.g 11 gcase meaning that both user and ai choose rock (its tie)
        #12 meaning that user chose rock but the AI Paper. 
        
 #       print (gcase)
        
        
        if int(inp) == 0:#exit option
                break
        elif (int(inp)==ai):
                print (f"Ai Choose {option(ai)} - You Also choose {option(inp)} \n Its a tie!!")
                PrintScore(YourScore,AiScore)

                continue
        elif gcase==13 or gcase==14 or gcase==21 or gcase==32 or gcase==34 or gcase==42:
                print (f"Ai Choose {option(ai)} - You  choose {option(inp)} \n You Win!!")
                YourScore += 1
                PrintScore(YourScore,AiScore)
        else:
                print (f"Ai Choose {option(ai)} - You  choose {option(inp)} \n Ai Wins!!")
                AiScore += 1
                PrintScore(YourScore,AiScore)




def PrintScore(YourScore,AiScore):# just for printing the score!
    print (f'score is You-AI: {YourScore} - {AiScore}')
    
def option(opt): 
    tmp=int(opt)
    match tmp:
        case 1:
            return 'rock'
        case 2:
            return 'Paper'
        case 3:
            return 'Scissors'
        case default:
            return 'Pencil'
    
    
    


if __name__=='__main__': # is it  main?
    main()


    