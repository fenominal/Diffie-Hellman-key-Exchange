sharedPrime = int(input("enter the prime Number : "))
sharedBase = int(input("enter the base g: "))
aliceSecret = int(input("enter the alice x: "))
bobSecret = int(input("enter the bob y: "))
print("------------------------------")
print("--Publicly Shared Variables--")
print (" Publicly Shared Prime:", sharedPrime)
print (" Publicly Shared Base:", sharedBase)
print("------------------------------")

#caluclate A
A = (sharedBase**aliceSecret) % sharedPrime
print (" Alice Sends Over Public Chanel:" , A)

#calculate B
B = (sharedBase ** bobSecret) % sharedPrime
print (" Bob Sends Over Public Chanel:", B)

print("------------------------------")
print ("--Privately Calculated Shared Secret--")
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print (" Alice Shared Secret:", aliceSharedSecret)
bobSharedSecret = (A**bobSecret) % sharedPrime
print (" Bob Shared Secret:", bobSharedSecret )