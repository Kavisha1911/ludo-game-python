 #ludo
import random
import array

print("LUDO!")
print("you have one pawn and one chance")
   
#1 user 1 pawn move

# Creating an array of signed integers
position = array.array('i', [0, 0, 0, 0])
#print(position)


# while loop for chances
max_val=0
round_counter=0
while max_val!=56:
    round_counter+=1
    for user_counter in range(4):
        if position[user_counter]==0:
            dice=random.randint(1,6)
            int_pos=0
            print("user-"+str(user_counter+1)+" You got "+ str(dice))
            #position[counter]=0
            if dice==1:
                print("user-"+str(user_counter+1)+" Congo! Your pawn is opened.")
                int_pos=1
            elif dice==6:
                print("user-"+str(user_counter+1)+" Congo! Your pawn is opened. You get one more chance.")
                int_pos=1
                dice=random.randint(1,6)
                print("user-"+str(user_counter+1)+" You got "+ str(dice))

                if dice==1:
                    int_pos=7
                elif dice<=5:
                    int_pos=1+dice
                elif dice==6:
                    #intermediate position added
                    int_pos=7
                    print("user-"+str(user_counter+1)+" Congo! You get one more chance. If you get 6 again all your changes will be cancelled.")
                    dice=random.randint(1,6)
                    print("user-"+str(user_counter+1)+" You got "+ str(dice))

                    if dice<=5:
                        int_pos=7+dice
                        

                    elif dice==6:
                        int_pos=0
                        print("Since you got 6 three times your chance is cancelled.")

            position[user_counter]=position[user_counter]+int_pos
            print("user-"+str(user_counter+1)+"Your current position after "+str(round_counter)+ " round is: "+str(position[user_counter]))   
        else:
            dice=random.randint(1,6)
            print("user-"+str(user_counter+1)+" You got "+ str(dice))

            if dice<=5:
                int_pos1=dice
                
            elif dice==6:
                    int_pos1=6
                    print("user-"+str(user_counter+1)+" Congo! You get one more chance.")
                    dice=random.randint(1,6)
                    print("user-"+str(user_counter+1)+" You got "+ str(dice))

                    if dice<=5:
                        int_pos1=6+dice
                        
                    elif dice==6:
                        int_pos1=12
                        print("user-"+str(user_counter+1)+" If you get 6 again all your changes will be cancelled.")
                        if dice<=5:
                            int_pos1==12+dice
                        elif dice==6:
                            int_pos1=0
                            print("Since you got 6 three times your chance is cancelled.")

            if position[user_counter]+int_pos1<56:
                position[user_counter]=position[user_counter]+int_pos1
                print("user-"+str(user_counter+1)+"Your current position after "+str(round_counter)+ " round is: "+str(position[user_counter]))
                if max_val<position[user_counter]:
                    max_val=position[user_counter]

            elif position[user_counter]+int_pos1==56:
                print("user-"+str(user_counter+1)+" you won.")
                max_val=56
                break

            else:
                print("user-"+str(user_counter+1)+" invalid chance")

