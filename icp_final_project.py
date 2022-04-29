# Stable marriage problem using Gale-Shapley algorithm
# If woman prefers man1 (whom she is currently engaged with) to man2, return false, else return true
def checkIfWomanPrefersMan2toMan1(preferenceList, woman, man1, man2):
    # Check if woman prefers man2 to man1, whom she is currently engaged with
    # inv: 0 <= i <= n
    for i in range(n):
        # If man2 precedes man1 in woman's list of preferences, that implies woman is unhappy with man1, so she must be paired with man2 instead, whom she prefers
        if (preferenceList[woman][i] == man2):
            return True
        # If, on the other hand, man1 precedes man2 in woman's list of preferences, that implies woman is happy with man1, so nothing needs to be changed
        if (preferenceList[woman][i] == man1):
            return False
    # assert: i == n
# Print stable marriage arrangement for n men and n women, which makes a total of 2n people
# 0 to n - 1 are the men
# n to 2n - 1 are the women
def stableMarriages(preferenceList):
    # The value of partnerOfWomen[i] indicates the partner assigned to woman n+i. 
    # -1 as an element of the array indicates that the (n+i)-th woman is unengaged
    # Initialize the array such that all women are unengaged at first
    partnerOfWomen = [-1 for i in range(n)]
    # Stores the engagement status of men.
    # If isManEngaged[i] is false, then the i-th man is unengaged, otherwise engaged.
    isManEngaged = [False for i in range(n)]
    # All men are initially unengaged, so number of unengaged men is n
    numberOfUnengagedMen = n
    # Loop runs as long as there are unengaged men
    # assert: numberOfUnengagedMen == n
    # inv: 0 <= numberOfUnengagedMen <= n
    while (numberOfUnengagedMen > 0):
        man = 0 # Initialize to 0 to select the first unengaged man and pair him off, continue the cycle below
        # assert: man == 0
        # inv: 0 <= man <= n
        while (man < n):
            if (isManEngaged[man] == False):
                break
            man += 1
        # assert: man == n
        # Pair with each woman on the basis of the selected unengaged man's preference list to check compatibility
        i = 0
        # inv: 0 <= i < n
        # assert i == 0
        while i < n and isManEngaged[man] == False:
            woman = preferenceList[man][i] # Store the value of the preferred woman for man
            # If preferred woman is unengaged, man and woman become tentative partners, subject to change
            if (partnerOfWomen[woman - n] == -1): # If partner of woman is unengaged
                partnerOfWomen[woman - n] = man # Make man and woman tentative partners, based on woman's preferences but subject to change
                isManEngaged[man] = True # Update engagement status of man
                numberOfUnengagedMen -= 1 # Number of unengaged men decreases by 1
            else:
                # If woman is engaged, find the present engagement of woman
                presentEngagement = partnerOfWomen[woman - n] # Store the value of the man whom woman is currently engaged with
                # If woman prefers man over her present engagement presentEngagement, woman gets engaged to man instead
                if (checkIfWomanPrefersMan2toMan1(preferenceList, woman, man, presentEngagement) == False):
                    partnerOfWomen[woman - n] = man # Partner of woman is man now
                    isManEngaged[man] = True # Update engagement status of man
                    isManEngaged[presentEngagement] = False # Original engagement of woman is broken, thus that man is no longer engaged for now
            i += 1
    # assert numberOfUnengagedMen == 0
    # Display the stable arrangement of men/women
    # inv: n <= i < 2*n
    # assert i == n
    for i in range(n, 2*n):
        print(i, "is paired with", partnerOfWomen[i - n])
    # assert i == 2*n
# Main method that initializes the number of men/women, their preference lists and displays a stable arrangement on the basis of preferenceList
if __name__=='__main__':
    n = 4 # Equals the number of men and women each
    preferenceList = [ [7, 6, 4, 5], [4, 6, 5, 7], [6, 4, 7, 5], [6, 7, 5, 4], [1, 2, 0, 3], [3, 1, 2, 0], [3, 0, 2, 1], [2, 1, 0, 3] ]
    print("Stable marriage problem:\nMen are numbered from 0 to n - 1 and women are numbered from n to 2n - 1, where n is the number of men and women each\nThe number of men/women selected for demonstrating the program is 4\nTherefore, {0, 1, 2, 3} is the set of all men who are to be engaged to {4, 5, 6, 7} which is the set of all women\nThe preference list of each man and woman, from most preferred to least preferred, are as follows:")
    # inv: 0 <= i <= 2*n
    # assert: i == 0
    for i in range(2*n):
        print(i,  "-",  preferenceList[i])
    # assert: i == 2*n
    print("Stable marriage arrangements:")
    stableMarriages(preferenceList)
