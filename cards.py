import random
ordinary_card = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
special_card = ['小王','大王']
def create_poker():
    poker = []
    for i in ordinary_card:
        poker.append(i), poker.append(i),poker.append(i),poker.append(i)
    for i in special_card:
        poker.append(i)
    return poker
def shuffle_poker(poker):
    random.shuffle(poker)
    return poker
def deal_poker(poker):
    player1 = []
    player2 = []
    player3 = []
    remain_card = []
    for i in range(52):
        i_reflect= poker[i]
        if i_reflect < 17:
            player1.append(i_reflect)
        elif i_reflect < 34:
            player2.append(i_reflect)
        elif i_reflect < 51:
            player3.append(i_reflect)
        else:
            remain_card.append(i_reflect)
    return (player1,player2,player3,remain_card)
def sort_poker(poker):
    poker = create_poker()
    poker = shuffle_poker(poker)
    player1,player2,player3,remain_card = deal_poker(poker)
    for i in range(len(player1)):
        for j in range(i+1,len(player1)):
            if player1[i] > player1[j]:
                player1[i],player1[j] = player1[j],player1[i]
                return player1
    for i in range(len(player2)):
        for j in range(i+1,len(player2)):
            if player2[i] > player2[j]:
                player2[i],player2[j] = player2[j],player2[i]
                return player2
    for i in range(len(player3)):
        for j in range(i+1,len(player3)):
            if player3[i] > player3[j]:
                player3[i],player3[j] = player3[j],player3[i]
                return player3

sort_poker()
card_value = {
    '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14,'2':15,'小王':16,'大王':17
}
def get_card_value(cards):
    if cards is None or len(cards) == 0:
        return(None,None,None)
    values = []#存储并记录每张牌的点数
    for card in cards:
        if card in card_value:
            values.append(card_value[card])
        else:
            return None
    n = len(values)
    for i in range(n):#给牌手动排序
        for j in range(i+1,n):
            if values[i] > values[j]:
                values[i],values[j] = values[j],values[i]
    count_map= {}#创建空字典，用于统计每一种牌的数量
    for value in values:
        if value in count_map:
            count_map[value] += 1
        else:
            count_map[value] = 1
    
    # 修正王炸判断条件
    if n == 2 and 16 in values and 17 in values:
        return('Rocket',17,None)
    
    if n == 1:
        return('Single',values[-1],None)
    
    if n == 2:
        if len(count_map)== 1:#判断是否有对子
            return('Pair',values[-1],None)
        else:
            return None
    
    if n == 3:
        if len(count_map) == 1:#判断是否有三条
            return('triplet',values[-1],None)
        else:
            return None
    
    if n == 4:
        if len(count_map) == 1:#判断是否有炸弹
            return('Bomb',values[-1],None)
        elif len(count_map) == 2:#判断是否有三带一
            for value in count_map:
                if count_map[value] == 3:
                    key = value
                    return('triplet_with_single',key,None)
            return None
        else:
            return None
    
    if n == 5:
        if len(count_map) == 2:#判断是否有三带一对
            for value in count_map:
                if count_map[value] == 3:
                    key = value
                    for other_value in count_map:
                        if other_value != value and count_map[other_value] == 2:
                            return('triplet_with_pair',key,None)
            return None
        else:
            return None
    
    if n >= 5:#判断是否有顺子
        is_sequence = True#判断是否连续
        if len(count_map) != n:
            is_sequence = False
        else:
            for i in range(n-1):
                if values[i+1] != values[i]+1:
                    is_sequence = False
                    break
            for value in values:
                if value >= 15:#判断是否有2或者王牌
                    is_sequence = False
                    break
        if is_sequence:
            return('Sequence',values[-1],n)
        else:
            return None
    
    if n >= 6 and n % 2 == 0:#判断是否有连对
        pairs = []
        for value in count_map:
            if count_map[value] == 2:
                pairs.append(value)
        for i in range(len(pairs)):
            for j in range(i+1,len(pairs)):
                if pairs[i]>pairs[j]:
                    pairs[i],pairs[j] = pairs[j],pairs[i]
        is_pair = True
        if len(pairs)*2 != n:#不是所有的牌都组合成对子
            is_pair = False
        elif len(pairs) < 3:
            is_pair = False
        else:#检查是否连续#检查是否出现2或王牌
            for i in range(len(pairs)-1):
                if pairs[i+1] != pairs[i]+1:
                    is_pair = False
                    break
            for value in pairs:
                if value >= 15:
                    is_pair = False
                    break
        if is_pair:
            return('Pair_Sequence',pairs[-1],len(pairs))
    
    if n >= 6:
        triplets = []
        for value in count_map:
            if count_map[value] == 3:
                triplets.append(value)
        for i in range(len(triplets)):
            for j in range(i+1,len(triplets)):
                if triplets[i]>triplets[j]:
                    triplets[i],triplets[j] = triplets[j],triplets[i]
        is_air_plane = True
        if len(triplets) <= 1:
            is_air_plane = False
        else:
            for i in range(len(triplets)-1):
                if triplets[i+1] != triplets[i]+1:
                    is_air_plane = False
                    break
        if is_air_plane:#获取其他牌
            other_cards=[]
            for value in values:
                if value not in triplets or values.count(value) > 3:
                    other_cards.append(value)
            other_count = {}
            for card in other_cards:
                if card in other_count:
                    other_count[card] += 1
                else:
                    other_count[card] = 1
            if not other_cards:
                return('airplane',triplets[-1],len(triplets))
            elif len(other_cards) == len(triplets):
                all_single = True
                for count in other_count.values():
                    if count != 1:
                        all_single = False
                        break
                if all_single:
                    return('airplane_with_single',triplets[-1],len(triplets))
            elif len(other_cards) == 2 * len(triplets):
                all_pair = True
                for count in other_count.values():
                    if count != 2:
                        all_pair = False
                        break
                if all_pair:
                    return('airplane_with_pair',triplets[-1],len(triplets))
        
        is_triplet = True
        if len(triplets)*3 != n:#不是所有的牌都组合成三条
            is_triplet = False
        elif len(triplets) < 2:
            is_triplet = False
        else:#检查是否出现2或王牌
            for i in range(len(triplets)-1):
                if triplets[i+1] != triplets[i]+1:
                    is_triplet = False
                    break
            for value in triplets:
                if value >= 15:
                    is_triplet = False
                    break
        if is_triplet:
            return('triplet_sequence',triplets[-1],len(triplets))
    
    if n == 6:
        for value in count_map:
            if count_map[value] == 4:
                key = value
                other_cards=[]
                for card in values:
                    if card != value:
                        other_cards.append(card)
                if len(set(other_cards))==2:
                    return('quad_with_two_singles',value,None)
                if len(set(other_cards))==1:
                    return('quad_with_pair',key,None)
        return None
    
    if n == 8:
        has_four = False
        four_value = None
        rest_counts = []
        for value in count_map:
            if count_map[value] == 4:
                has_four = True
                four_value = value
            else:
                rest_counts.append(count_map[value])
        if has_four and len(rest_counts) == 2 and all(value == 2 for value in rest_counts):
            return('four_with_two_pairs',four_value,None)
        else:
            return None
    
    if n == 4 and len(count_map) == 1:
        return('bomb',values[0],None)
    
    return None

def compare_cards(cards1,cards2):
    # 检查空输入
    if cards1 is None or len(cards1) == 0:
        if cards2 is None or len(cards2) == 0:
            return 0
        else:
            return -1
    elif cards2 is None or len(cards2) == 0:
        return 1
    
    # 获取牌型信息
    result1 = get_card_value(cards1)
    result2 = get_card_value(cards2)
    
    if result1 is None or result2 is None:
        return None
    
    type1, key1, extra1 = result1
    type2, key2, extra2 = result2
    
    if type1 == 'Rocket':#先比王炸
        if type2 == 'Rocket':
            return 0
        else:
            return 1
    elif type2 == 'Rocket':
        return -1
    
    if type1 == 'Bomb' or type2 == 'Bomb':#先比炸弹
        if type1 == 'Bomb' and type2 == 'Bomb':
            if key1 > key2:
                return 1
            elif key1 < key2:
                return -1
            else:
                return 0
        elif type1 == 'Bomb':
            return 1
        else:
            return -1
    
    if type1 != type2:#类型不同，无法直接比较
        return None
    
    # 相同类型比较
    if key1 > key2:
        return 1
    elif key1 < key2:
        return -1
    else:
        # 关键牌相同，比较附加信息（如顺子长度）
        if extra1 is not None and extra2 is not None:
            if extra1 > extra2:
                return 1
            elif extra1 < extra2:
                return -1
            else:
                return 0
        else:
            return 0

def reveal_cards():
    # 获取用户输入，使用空格分隔每张牌
    cards1_input = input("请出第一手牌（用空格分隔每张牌，如：3 4 5 6 7）: ")
    cards2_input = input("请出第二手牌（用空格分隔每张牌，如：8 9 10 J Q）: ")
    
    # 处理空输入
    if cards1_input.strip() == "":
        cards1 = None
    else:
        cards1 = cards1_input.split()
    
    if cards2_input.strip() == "":
        cards2 = None
    else:
        cards2 = cards2_input.split()
    
    # 比较牌型
    result = compare_cards(cards1, cards2)
    
    # 输出结果
    if result is None:
        print("无法比较这两手牌")
    elif result == 1:
        print("第一手牌比第二手牌大")
    elif result == -1:
        print("第二手牌比第一手牌大")
    else:
        print("两手牌一样大")

if __name__ == '__main__':
    reveal_cards()

