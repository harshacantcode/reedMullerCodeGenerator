#Python code to print all the codewords of a binary (r,m) reed muller code

#PARAMETERS OF THE REED MULLER CODE

#The maximum degree of a monomial
r = 1
#The number of variables
m = 4

#Finds nCr
def nCr(n,r):
    return fact(n)/(fact(r)*fact(n-r))

#Factorial of the input
def fact(n):
    returnValue = 1
    for i in range(2,n+1):
        returnValue = returnValue*i
    return returnValue

#Calculates x^y
def xpowy(x,y):
    retVal = 1
    while(y > 0):
        if(y&1 == 1):
             retVal = retVal * x
        y = y >> 1
        x = x*x
    return retVal


def main():

    #Summation to find the dimension of the code
    dimensionOfTheCode = 0
    for i in range(r + 1):
        dimensionOfTheCode = dimensionOfTheCode + nCr(m,i)

    #Finding the cardinality of the code and the length of a codeword
    numOfCodewords = xpowy(2,int(dimensionOfTheCode))
    lengthOfCodeword = xpowy(2,m)

    #Generating all possible coefficients for the message polynomial
    for i in range(numOfCodewords):
        #Creating an array for the message vector
        #Each bit of the value of i corresponds to a coefficient of the message polynomial
        messageVector = [0]*int(dimensionOfTheCode)
        dummy = i
        pos = 0

        #Converting the decimal value for the message vector into binary
        while(pos < dimensionOfTheCode):
            if(dummy & 1 == 1):
                messageVector[pos] = 1
            else:
                messageVector[pos] = 0
            if(dummy == 0):
                break
            dummy = dummy >> 1
            pos = pos + 1

        #Multiplying the message vector with the polynomial evaluated at 2^m points
        for j in range(lengthOfCodeword):
            #Creating an array to store the binary representation of j
            #Each bit of the binary representation for j represents the values taken for the variables x1 x2 x3 x4
            evaluationVector = [0]*m
            #Allocating memory for the array that will be our codeword
            codeWord = [0]*lengthOfCodeword
            dummyPrime = j
            posPrime = 0

            #Converting the decimal value of the evaluation into binary
            while(posPrime < m):
                if(dummyPrime & 1 == 1):
                    evaluationVector[posPrime] = 1
                else:
                    evaluationVector[posPrime] = 0
                if(dummyPrime == 0):
                    break
                dummyPrime = dummyPrime >> 1
                posPrime = posPrime + 1

            codeWord[j] = ((1*messageVector[0])
                            ^(evaluationVector[0]*messageVector[1])
                            ^(evaluationVector[1]*messageVector[2])
                            ^(evaluationVector[2]*messageVector[3])
                            ^(evaluationVector[3]*messageVector[4]))

            print(codeWord[j],end = '')

        print('\n')

main()
