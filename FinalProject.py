import numpy as np  
import math
import sys

#sigmoid function
def nonlin(x, deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#learnFrom function using neural network
#inputs: size of the training list, and the training list itself
#output: A list of possible outputs which the computer will draw from as their guess of the player's move.
def learnFrom(size, trainingInput = []):
    #setup the input list as numpy matrix
    #and then seed random numbers for deterministic calculations
    #x will be in input dataset and y will be the output dataset
    x = np.array(trainingInput)
    X = np.reshape(x, (-1,size))
    y = np.array(trainingInput).T
    np.random.seed(1)

    #synapse zero: the weight matrix for the neural network
    syn0 = 2*np.random.random((size,size)) - 1
    
    #training the neural network based on training set.
    for iter in range(10000):
        #layer 1, the inputs
        l0 = X
        #layer 2, then hidden layer; prediction step
        l1 = nonlin(np.dot(l0,syn0))
        
        #error step, compares predicted output to actual output
        l1_error = y - l1
        #reduce error of high confidence predictions
        l1_delta = l1_error * nonlin(l1,True)
        #update the network with training example
        syn0 += np.dot(l0.T, l1_delta)

    return l1.tolist()
    
#Main method, simple game is here
if __name__ == "__main__":
    #Take Input
    print("Welcome, loading training set.")
    trainingInput = []
    with open("training/trainingSet8.txt") as file:
        for line in file:
            line = line.strip()
            trainingInput.append(line)
    trainingInput = list(map(int, trainingInput))
    print("Training set Loaded.")
   
    #GAME STARTS HERE
    print("\n\nWelcome to the Guessing Game!")
    print("You have 32 guesses. \n You guess whether the computer predicted a 1 or 0, each time you guess correctly, you earn points.\n")

    #points, turn ,and percent correct guesses, the game only has 32 turns.
    points = 0
    count = 0
    correct = 0

    #game loop
    while(count < 32):
        #use neural network to guess possible answers from training set.
        #output is the raw answer, prediction the raw answer rounded to a 0 or 1.
        output = learnFrom(len(trainingInput), trainingInput) 
        prediction = int(round(output[0][count]))
        
        #Showing turn and current score
        print("\nTurn " + str(count + 1) + "!")
        print("\nYou currently have " + str(points) + " Points!") 
        #user input and error checking.
        data = input("Make your guess: ")
        try:
            guess = int(data)
            #if input is 0 or 1, valid
            if guess == 0 or guess == 1:
                #if guess is right, reward player and increment turn
                if guess == prediction:
                    print("\nYou guessed correctly! +1 point!")
                    points += 1
                    count += 1
                    trainingInput.append(guess)

                else:
                    #if incorrect, just increment turn
                    print("\nYou guessed wrong! No points for you!")
                    count += 1
                    trainingInput.append(guess)
                
                #show result after guess, what you guessed compared to computer prediction.
                print("\nYou guessed: " + str(guess))
                print("Computer Predicted: " + str(prediction))
                correct = int(round((points * 100)/(count)))
                print("Percent of correct guesses: " + str(correct) +"%.")
            else:
                print("\nInvalid input, please enter a 0 or 1.")

        except ValueError:
            print("Invalid input, please enter a 0 or 1.")
    
    #turn 32 passed, game has now finished. 
    print("Game over! \nYou have scored " +str(points) + " points!")