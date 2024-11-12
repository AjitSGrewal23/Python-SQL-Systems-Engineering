playlist = ["Another Brick in the Wall", "Comfortably Numb", "Echoes", 
    "Hey You", "High Hopes", "Money", 
    "Shine On You Crazy Diamond", "Wish You Were Here", "Young Lust"]         #playlist array is defined  
song = "Money"                                                                #searched song is initialized
left = 0                                                                      #left is defined as the first element 0
right = len(playlist) - 1                                                     #right is defined as the last element in the list

def ternarySearch(playlist, song, left, right):                               #function to ternary search
    if right >= left:                                                         #ensures validity
        sublist1 = left + (right - left) // 3                                 
        sublist3 = right - (right - left) // 3                                #sublist ranges
        if playlist[sublist1] == song:                                        #search first segment
            return sublist1                                                   #output sublist1
        if playlist[sublist3] == song:                                        #search third segment
            return sublist3                                                   #output sublist3
        if song < playlist[sublist1]:
            return ternarySearch(playlist, song, left, sublist1 - 1)          #search left segment if song comes before
        elif song > playlist[sublist3]:
            return ternarySearch(playlist, song, sublist3 +1, right)          #search right segment
        else: return ternarySearch(playlist, song, sublist1 +1, sublist3 - 1) #search middle segment
    return None                                                               #song is not found

index = ternarySearch(playlist, song, left, right)                            #call to the ternary search function
message = (f"Song '{song}' found index: {index}" if index is not None else f"Song '{song}' not in list")
print(message)                                                                #print message showing index