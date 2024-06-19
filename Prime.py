'''Context:
A leading aerospace company, OrbitTech, is developing a satellite communication system that relles heavily on secure data transmission. 
The encryption keys used for securing communication between satellites and ground stations are generated based on prime numbers. 
To ensure the integrity and security of these keys, it is crucial to verify the primality of large numbers efficiently in real-time.

Scenarior
OrbitTech's satellite communication system requires real-time verification of prime numbers during the generation of encryption keys.
Given the high-stakes nature of satellite data transmission, any delay or error in prime verification could compromise the security and
efficiency of the system. Therefore, OrbitTech needs a reliable and efficient solution to check if given numbers are prise.'''
n=int(input('Enter the message ='))
f=0
if n<1:
    f=1
elif n==1:
    f=0
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            f+=1
            break
if f==0:
    print('Valid message')
else:
    print('Invalid message') 
