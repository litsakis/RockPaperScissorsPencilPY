
def main():
    while (True):
        print ('--'*20)
        inp =input ('''
        Press 0 to EXIT!
        Press 1 for Rock
        Press 2 for Paper
        Press 3 For Scissors
        Press 4 For Pencil
        ''')
        if (inp not in range(4)):
          continue

        print (inp)


def PrintScore():
    print (f'score is')
    
    
    
    


if __name__=='__main__':
    main()


    