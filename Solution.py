import math
# convert number into its prime divisors
def numToBlocks(piles):
    pblck=[]
    for n in piles:
        blocks=0
        if n == 1:
            pblck.append(0)
            continue
        while n % 2 == 0:
            blocks+= 1
            n = n // 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                blocks+= 1
                n = n // i
        if n > 2:
            blocks += 1
        pblck.append(blocks)
    return pblck
# method built upon symmetry and usage of xor to solve it
def main():
    piles = input("Enter your pile numbers: ")
    piles=list(piles.split(" "))
    for i in range(0, len(piles)):
        piles[i] = int(piles[i])
    piles=numToBlocks(piles)
    print(piles)
    result=0
    for x in piles:
        result= result^x
    if result==0:
        result=2
    else:
        result=1
    print('Player '+str(result)+' won')
if __name__ == "__main__":
    main()
