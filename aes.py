import math
import numpy

global SubByteTransformationTable
SubByteTransformationTable = [ 
[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76], 
[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0], 
[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15], 
[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75], 
[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84], 
[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf], 
[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8], 
[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2], 
[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73], 
[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb], 
[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79], 
[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08], 
[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a], 
[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e], 
[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf], 
[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

global invSubByteTransformationTable
invSubByteTransformationTable = [
[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
[0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
[0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
[0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
[0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
[0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
[0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
[0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
[0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
[0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
] 

global MixColumnsConstant
MixColumnsConstant = [
[0x02, 0x03, 0x01, 0x01], 
[0x01, 0x02, 0x03, 0x01], 
[0x01, 0x01, 0x02, 0x03], 
[0x03, 0x01, 0x01, 0x02]
]

global invMixColumnsConstant
invMixColumnsConstant = [ 
[0x0E, 0x0B, 0x0D, 0x09], 
[0x09, 0x0E, 0x0B, 0x0D], 
[0x0D, 0x09, 0x0E, 0x0B], 
[0x0B, 0x0D, 0x09, 0x0E]
]

global RCon
RCon = [
[0x01, 0x00, 0x00, 0x00],
[0x02, 0x00, 0x00, 0x00],
[0x04, 0x00, 0x00, 0x00],
[0x08, 0x00, 0x00, 0x00],
[0x10, 0x00, 0x00, 0x00],
[0x20, 0x00, 0x00, 0x00],
[0x40, 0x00, 0x00, 0x00],
[0x80, 0x00, 0x00, 0x00],
[0x1B, 0x00, 0x00, 0x00],
[0x36, 0x00, 0x00, 0x00]
]

def SubBytes(state):
    # Creates a new state
    newState = []
    for i in range(4):
        newState.append([])
        for j in range(4):
            newState[i].append(0)

    # Insert the value into the state, based on the passed state
    # Refers to the SubByte Transformation table
    col = 0
    while (col < 4):
        row = 0
        while (row < 4):
            strByte = str(state[col][row])

            if (len(strByte) == 4):
                LHSstrByte = int(int(strByte[2], 16))
                RHSstrByte = int(int(strByte[3], 16))
            else:
                LHSstrByte = 0
                RHSstrByte = int(int(strByte[2], 16))
            
            newState[col][row] = hex(SubByteTransformationTable[LHSstrByte][RHSstrByte])
            row +=1
        col += 1

    print("After SubByte    : ",  newState)
    return newState

def ShiftRows(state):
    newState = state
    
    i = 0
    while (i < 4):
        j = 0
        while (j < i):
            newState[i].append(newState[i].pop(0))
            j += 1
        i += 1
    
    print("After ShiftRows  : ",  newState)
    return newState

def MixColumnsMultiplication(stateByte, mixColumnsConstant):
    # Check the multiplier
    # If the multiplier is 1, return the multiplicand as it is.
    # If the multiplier is 2, check the MSB of the multiplicand,
    # - If the MSB is 1, 1 left binary shift on the multiplicand and XOR with 0x1B.
    # - Else (MSB is 0), only 1 left binary shift on the multiplicand.
    # If the multiplier is 3, multiply like the multiplier is 2, then XOR with the original multiplicand.
    #print("StateByte: ", hex(int(stateByte[2:], 16)))

    if (mixColumnsConstant == 1):
        return stateByte
    else:
        if (mixColumnsConstant == 2):
            # Converts the multiplicand to binary
            stateByteStr = stateByte[2:]
            stateByteBin = bin(int(stateByteStr, 16))
            
            # Gets the most significant bit (MSB) of the multiplicand
            stateByteStr = str(stateByteBin)
            if (len(stateByteStr) == 10):
                MSB = stateByteStr[2:3]
            else:
                MSB = "0"

            # Left binary shift by 1
            if (len(stateByteStr) == 10):
                newStateByte = int(stateByteStr[3:]+MSB[0], 2)
            else:
                stateByteStr = stateByteStr[:1] + "0" + stateByteStr[2:]
                newStateByte = int(stateByteStr[2:]+MSB[0], 2)
            
            # XOR with 0x1B
            if (MSB == "1"):
                newStateByte = hex(newStateByte ^ 0x1b)
            else:
                newStateByte = hex(newStateByte)
            
            return newStateByte
        else:
            # Converts the multiplicand to binary
            stateByteStr = stateByte[2:]
            stateByteBin = bin(int(stateByteStr, 16))
            
            # Gets the most significant bit (MSB) of the multiplicand
            stateByteStr = str(stateByteBin)
            if (len(stateByteStr) == 10):
                MSB = stateByteStr[2:3]
            else:
                MSB = "0"

            # Left binary shift by 1
            if (len(stateByteStr) == 10):
                newStateByte = int(stateByteStr[3:]+MSB[0], 2)
            else:
                stateByteStr = stateByteStr[:1] + "0" + stateByteStr[2:]
                newStateByte = int(stateByteStr[2:]+MSB[0], 2)
                
            # XOR with 0x1B
            if (MSB == "1"):
                newStateByte = hex(newStateByte ^ 0x1b)
            else:
                newStateByte = hex(newStateByte)

            # XOR with the original multiplicand
            newStateByte = hex(int(newStateByte[2:], 16) ^ int(stateByteBin[2:], 2))
            return newStateByte

def MixColumns(state):
    newState = state
    
    # Goes through each column
    i = 0
    while (i < 4):
        tempColumn = [[""], [""], [""], [""]]
        
        # Goes through each row
        j = 0
        while (j < 4):
            addend1 = MixColumnsMultiplication(newState[0][i], MixColumnsConstant[j][0])
            addend2 = MixColumnsMultiplication(newState[1][i], MixColumnsConstant[j][1])
            addend3 = MixColumnsMultiplication(newState[2][i], MixColumnsConstant[j][2])
            addend4 = MixColumnsMultiplication(newState[3][i], MixColumnsConstant[j][3])

            tempState = hex(int(addend1[2:], 16) ^ int(addend2[2:], 16) ^ int(addend3[2:], 16) ^ int(addend4[2:], 16))
            tempColumn[j][0] = tempState
            
            j += 1

        newState[i][0] = tempColumn[0][0]
        newState[i][1] = tempColumn[1][0]
        newState[i][2] = tempColumn[2][0]
        newState[i][3] = tempColumn[3][0]
        
        i += 1
    
    print("After MixColumns : ",  newState)
    return newState

def AddRoundKey(state, roundKey):
    newState = state

    i = 0
    j = 0
    while (i < 16):
        col = i % 4
        row = math.floor(i/4)
        addend1 = int(newState[col][row][2:], 16)
        addend2 = int(roundKey[col][row][2:], 16)
        newState[col][row] = hex(addend1 ^ addend2)
        i += 1
        j += 8
    
    print("After AddRoundKey: ",  newState)
    return newState

def preRoundTransformation(state, roundKey):
    newState = AddRoundKey(state, roundKey)

    print("After preRoundTfn: ",  newState)
    return newState

def roundN(state, roundKey):
    newState1 = SubBytes(state)
    newState2 = ShiftRows(newState1)
    newState3 = MixColumns(newState2)
    newState4 = AddRoundKey(newState3, roundKey)

    print("After RoundN     : ",  newState4)
    return newState4

# lastRound() is similar round(),
# the difference is lastRound() does not invoked MixColumns()
def lastRound(state, roundKey):
    newState1 = SubBytes(state)
    newState2 = ShiftRows(newState1)
    newState3 = AddRoundKey(newState2, roundKey)

    print("After lastRound  : ",  newState3)
    return newState3

def XORList(list1, list2):
    # - Creates a new word
    tempWord = []
    for i in range(1):
        tempWord.append([])
        for j in range(4):
            tempWord[i].append(0)

    k = 0    
    while (k < 4):
        tempWord[0][k] = hex(int(list1[k][2:], 16) ^ int(list2[k][2:], 16))
        k += 1

    convertWord = tempWord[0]
    return convertWord

def keyExpansion(roundKey, roundNumber):
    # Creates the temporary word
    # 1. Left shift by 1 byte
    tempWord = roundKey[3][0]
    roundKey[3][0] = roundKey[3][1]
    roundKey[3][1] = roundKey[3][2]
    roundKey[3][2] = roundKey[3][3]
    roundKey[3][3] = tempWord
    
    # 2. SubBytes Tranformation
    # - Creates a new word
    newWord = []
    for i in range(1):
        newWord.append([])
        for j in range(4):
            newWord[i].append(0)

    # - Insert the value into the word, based on the post-rot word
    # - Refers to the SubByte Transformation table
    col = 0
    while (col < 1):
        row = 0
        while (row < 4):
            strByte = str(roundKey[3][row])
            if (len(strByte) == 4):
                LHSstrByte = int(int(strByte[2], 16))
                RHSstrByte = int(int(strByte[3], 16))
            else:
                LHSstrByte = 0
                RHSstrByte = int(int(strByte[2], 16))
            
            newWord[col][row] = hex(SubByteTransformationTable[LHSstrByte][RHSstrByte])
            row +=1
        col += 1

    # 3. XOR with RCon
    tempWord = int(newWord[0][0][2:], 16) ^ RCon[roundNumber - 1][0]
    newWord[0][0] = hex(tempWord)
    word1 = XORList(newWord[0], roundKey[0])
    word2 = XORList(word1, roundKey[1])
    word3 = XORList(word2, roundKey[2])
    word4 = XORList(word3, roundKey[3])

    newRoundKey = [word1, word2, word3, word4]
    return newRoundKey

def encryption(plaintext, key):
    # Converts the plaintext into a data block
    # 1. Create a matrix of 4x4, filled with empty strings
    state = []
    for i in range(4):
        state.append([])
        for j in range(4):
            state[i].append(0)
    
    # 2. Insert the value of the double hexadecimal number into the data block
    #    - From top to bottom, starting from left to right
    k = 0
    l = 0
    while (k < 16):
        col = k % 4
        row = math.floor(k/4)
        state[col][row] = hex(int(plaintext[l:l+8], 2))
        k += 1
        l += 8
    
    print("initial State    : ",  state)
    
    # Determine the number of rounds based on key length
    numberOfRounds = 0
    if (len(key) == 128):
        numberOfRounds = 10
    else:
        if (len(key) == 192):
            numberOfRounds = 12
        else:
            numberOfRounds = 14

    # Converts the key into a data block
    # 1. Create a matrix of 4x4, filled with empty strings
    keyBlock = []
    for m in range(4):
        keyBlock.append([])
        for n in range(4):
            keyBlock[m].append(0)
    
    # 2. Insert the value of the double hexadecimal number into the data block
    #    - From top to bottom, starting from left to right
    o = 0
    p = 0
    while (o < 16):
        col = o % 4
        row = math.floor(o/4)
        keyBlock[col][row] = hex(int(key[p:p+8], 2))
        o += 1
        p += 8
    
    print("initial Key      : ",  keyBlock)

    state = preRoundTransformation(state, keyBlock)
    
    m = 1
    while (m <= numberOfRounds):
        newRoundKey = keyExpansion(keyBlock, m)
        
        if (m == numberOfRounds):
            state = lastRound(state, newRoundKey)
        else:
            state = roundN(state, newRoundKey)

        print("End of round", m)
        m += 1

    print("Final state:", state)
	
	# Convert the state into the ciphertext string
    ciphertext = ""
    for q in range(0, len(state)):
        for r in range(0, len(state[q])):
            ciphertext = ciphertext + format(int(state[q][r], 16), '0>8b')


    print("Ciphertext :", ciphertext)
    return ciphertext

'''


plaintext = "11001001110010011100100111001001110010011100100111001001110010011100100111001001110010011100100111001001110010011100100111001001"
plaintext = "00011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011011"
'''
plaintext = "00000000000000010000001000000011000001000000010100000110000001110000100000001001000010100000101100001100000011010000111000001111"
key       = "11001001110010011100100111001001110010011100100111001001110010011100100111001001110010011100100111001001110010011100100111001001"
encryption(plaintext, key)
