
def slot(quart_count,mac1,mac2,mac3):
    play_count = 0
    while quart_count > 0:
        mac1 +=1
        quart_count-= 1
        play_count += 1
        if mac1 == 35:
            mac1 = 0
            quart_count += 30
        if quart_count > 0:
            mac2 += 1
            quart_count -=1
            play_count += 1
            if mac2 == 100:
                mac2 = 0
                quart_count += 60
        if quart_count > 0:
            mac3 += 1
            quart_count -=1
            play_count += 1
            if mac3 == 10:
                mac3 = 0
                quart_count += 9
    
    print("martha plays", play_count, "before going broke")
slot(77,4,9,3)
