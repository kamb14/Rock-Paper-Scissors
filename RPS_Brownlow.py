#PROGRAM THAT SIMULATES 2 PEOPLE PLAYING RPS
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")

ply1 = 0
ply2 = 0
numGames = 0 #TOTAL NUMBER OF TIMES PLAYED 

#WHILE LOOP TO PLAY RPS
while True:
    player1_ans = input("\n{} Would you like to choose rock, paper, or scissors? \nEnter the word below: ".format(player1)).lower()

    #CHANGES USER'S INPUT TO LOWERCASE
    player2_ans = input("\n{} Would you like to choose rock, paper, scissors? \nEnter the word below: ".format(player2)).lower()

    #COMPARES P1 AND P2 RESPONSES
    if player1_ans == "scissors" or player1_ans =="rock" or player1_ans =="paper":

        if player2_ans == "scissors" or player2_ans =="rock" or player2_ans =="paper":
            
            if player1_ans == player2_ans:
                print("It's a tie!!") 
                numGames +=1
            
            elif player1_ans == 'rock':
                numGames +=1
                
                if player2_ans == 'scissors':
                    print("{} wins! Rock beats scissors!".format(player1))
                    ply1 +=1

                else:
                    print("{} wins! Paper beats rock!".format(player2))
                    ply2 +=1

            elif player1_ans == "scissors":
                numGames +=1

                if player2_ans == "paper":
                    print("{} wins! Scissors beats paper!".format(player1))
                    ply1 +=1
                
                else:
                    print("{} wins! Rock beats scissors!".format(player2))
                    ply2 +=1

            elif player1_ans == "paper":
                numGames +=1

                if player2_ans == "rock":
                    print("{} wins! Rock beats paper!".format(player2))
                    ply1 +=1
            
            else: 
                print("{} wins! Scissors beats paper!".format(player1))
                ply2 +=1

        else:
            print("\nError--Invalid input.\nYou have not entered rock, paper or scissors! \nTry again.")

            break #ENDS WHILE LOOP

        response = int(input("\nWould you like to play again?\nEnter 1 for YES or -1 for NO: "))

        #IF STATEMENT TO END GAME
        if response == -1:
            print("You ended the game.")

            #NUMBER OF TIMES THE GAME RAN
            print("\nNumber of times played: ", numGames)
            
            #HOW MANY TIMES P1 PLAYED AND WINS
            print("{} number of wins: {}".format(player1,ply1))

            #HOW MANY TIMES P2 PLAYED AND WINS
            print("{} number of wins: {}".format(player2,ply2))

            break #ends the if loop

