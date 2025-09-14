import random
ordinary_card = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
special_card = ['小王','大王']
card_value = {
    '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14,'2':15,'小王':16,'大王':17
}#创建映射字典
def create_poker():
    poker = []#创建列表用来容纳扑克牌
    for i in ordinary_card:
        poker.append(i), poker.append(i),poker.append(i),poker.append(i)
        #普通牌各有4张
    for i in special_card:
        poker.append(i)#大小王各有1张
    return poker
def shuffle_poker(poker):#洗牌
    random.shuffle(poker)
    return poker
def deal_poker(poker):
    player1 = []
    player2 = []
    player3 = []
    remain_card = []#地主牌
    for i in range(51):
        i_reflect= poker[i]#对应到poker列表中的索引
        #按顺序分发牌，每3张一组，避免洗牌不干净
        if i%3 == 0:
            player1.append(i_reflect)
        elif i%3 == 1:
            player2.append(i_reflect)
        elif i%3 == 2:
            player3.append(i_reflect)
    for i in range(51,len(poker)):#剩余3张地主牌
        remain_card.append(poker[i])
    return (player1,player2,player3,remain_card)
def sort(cards):#冒泡排序
    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if card_value[cards[i]]>card_value[cards[j]]:
                cards[i],cards[j] = cards[j],cards[i]
    return cards
def sort_poker():#自动给三家的牌以及地主牌排序
    poker = create_poker()
    poker = shuffle_poker(poker)
    player1,player2,player3,remain_card = deal_poker(poker)
    player1_sort = sort(player1)
    player2_sort = sort(player2)
    player3_sort = sort(player3)
    remain_card_sort = sort(remain_card)
    return (player1_sort,player2_sort,player3_sort,remain_card_sort)
def get_card_value(cards):#识别牌型
    if cards is None or len(cards) == 0:#判断如果不出牌
        return (None, None, None)
    values = []#为每一轮的出牌创建副本用来判断牌型
    for card in cards:
        if card in card_value:
            values.append(card_value[card])
        else:
            return None
    n = len(values)
    values_sorted = sorted(values)
    count_map = {}
    for value in values_sorted:
        if value in count_map:
            count_map[value] += 1
        else:
            count_map[value] = 1
    
    # 火箭（王炸）
    if n == 2 and 16 in values_sorted and 17 in values_sorted:
        return ('Rocket', 17, None)
    
    # 单张
    if n == 1:
        return ('Single', values_sorted[0], None)
    
    # 对子
    if n == 2:
        if len(count_map) == 1:
            return ('Pair', values_sorted[0], None)
    
    # 三张
    if n == 3:
        if len(count_map) == 1:
            return ('triplet', values_sorted[0], None)
    
    # 炸弹
    if n == 4 and len(count_map) == 1:
        return ('Bomb', values_sorted[0], None)
    
    # 三带一
    if n == 4:
        for value, count in count_map.items():
            if count == 3:
                return ('triplet_with_single', value, None)
    
    # 三带一对
    if n == 5:
        triplet_value = None
        pair_value = None
        for value, count in count_map.items():
            if count == 3:
                triplet_value = value
            elif count == 2:
                pair_value = value
        if triplet_value and pair_value:
            return ('triplet_with_pair', triplet_value, None)
    
    # 顺子
    if n >= 5:
        # 检查是否所有牌都是单张
        if len(count_map) == n:
            # 检查是否连续
            is_sequence = True
            for i in range(n-1):
                if values_sorted[i+1] != values_sorted[i] + 1:
                    is_sequence = False
                    break
            # 检查是否有2或王牌
            if any(value >= 15 for value in values_sorted):
                is_sequence = False
            if is_sequence:
                return ('Sequence', values_sorted[-1], n)
    
    # 连对
    if n >= 6 and n % 2 == 0:
        pairs = []
        for value, count in count_map.items():
            if count == 2:
                pairs.append(value)
        if len(pairs) * 2 != n:  # 不是所有牌都是对子
            pass
        elif len(pairs) >= 3:  # 连对至少需要3对
            pairs_sorted = sorted(pairs)
            is_pair_sequence = True
            # 检查连续性
            for i in range(len(pairs_sorted)-1):
                if pairs_sorted[i+1] != pairs_sorted[i] + 1:
                    is_pair_sequence = False
                    break
            # 检查是否有2或王牌
            if any(value >= 15 for value in pairs_sorted):
                is_pair_sequence = False
            if is_pair_sequence:
                return ('Pair_Sequence', pairs_sorted[-1], len(pairs_sorted))
    
    # 飞机（不带牌）
    if n % 3 == 0 and n >= 6:
        triplets = []
        for value, count in count_map.items():
            if count == 3:
                triplets.append(value)
        if len(triplets) * 3 != n:  # 不是所有牌都是三张
            pass
        elif len(triplets) >= 2:  # 飞机至少需要2组
            triplets_sorted = sorted(triplets)
            is_airplane = True
            # 检查连续性
            for i in range(len(triplets_sorted)-1):
                if triplets_sorted[i+1] != triplets_sorted[i] + 1:
                    is_airplane = False
                    break
            # 检查是否有2或王牌
            if any(value >= 15 for value in triplets_sorted):
                is_airplane = False
            if is_airplane:
                return ('airplane', triplets_sorted[-1], len(triplets_sorted))
    
    # 飞机带单牌
    if n % 4 == 0 and n >= 8:  # 8, 12, 16等
        triplets = []
        for value, count in count_map.items():
            if count == 3:
                triplets.append(value)
        if len(triplets) < 2:  # 至少需要2组三张
            pass
        else:
            triplets_sorted = sorted(triplets)
            is_airplane = True
            # 检查连续性
            for i in range(len(triplets_sorted)-1):
                if triplets_sorted[i+1] != triplets_sorted[i] + 1:
                    is_airplane = False
                    break
            # 检查是否有2或王牌
            if any(value >= 15 for value in triplets_sorted):
                is_airplane = False
            if is_airplane:
                # 检查带牌是否都是单张
                other_cards = [v for v in values_sorted if v not in triplets_sorted]
                if len(other_cards) == len(triplets_sorted):
                    return ('airplane_with_single', triplets_sorted[-1], len(triplets_sorted))
    
    # 飞机带对子
    if n % 5 == 0 and n >= 10:  # 10, 15, 20等
        triplets = []
        for value, count in count_map.items():
            if count == 3:
                triplets.append(value)
        if len(triplets) < 2:  # 至少需要2组三张
            pass
        else:
            triplets_sorted = sorted(triplets)
            is_airplane = True
            # 检查连续性
            for i in range(len(triplets_sorted)-1):
                if triplets_sorted[i+1] != triplets_sorted[i] + 1:
                    is_airplane = False
                    break
            # 检查是否有2或王牌
            if any(value >= 15 for value in triplets_sorted):
                is_airplane = False
            if is_airplane:
                # 检查带牌是否都是对子
                other_cards = [v for v in values_sorted if v not in triplets_sorted]
                other_count_map = {}
                for v in other_cards:
                    other_count_map[v] = other_count_map.get(v, 0) + 1
                if all(count == 2 for count in other_count_map.values()):
                    return ('airplane_with_pair', triplets_sorted[-1], len(triplets_sorted))
    
    # 四带二单
    if n == 6:
        for value, count in count_map.items():
            if count == 4:
                return ('quad_with_two_singles', value, None)
    
    # 四带二对
    if n == 8:
        for value, count in count_map.items():
            if count == 4:
                # 检查其余4张牌是否组成2对
                other_values = [v for v in values_sorted if v != value]
                other_count_map = {}
                for v in other_values:
                    other_count_map[v] = other_count_map.get(v, 0) + 1
                if sum(1 for c in other_count_map.values() if c == 2) == 2:
                    return ('quad_with_two_pairs', value, None)
    
    return None
def compare_cards(cards1,cards2):
    if cards1 is None or len(cards1) == 0:
        if cards2 is None or len(cards2) == 0:
            return 0
        else:
            return -1
    elif cards2 is None or len(cards2) == 0:
        return 1
    
    result1 = get_card_value(cards1)
    result2 = get_card_value(cards2)
    
    if result1 is None or result2 is None:
        return None
    
    type1, key1, extra1 = result1
    type2, key2, extra2 = result2
    
    if type1 == 'Rocket':
        if type2 == 'Rocket':
            return 0
        else:
            return 1
    elif type2 == 'Rocket':
        return -1
    
    if type1 == 'Bomb' or type2 == 'Bomb':
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
    
    if type1 != type2:
        return None
    
    if key1 > key2:
        return 1
    elif key1 < key2:
        return -1
    else:
        if extra1 is not None and extra2 is not None:
            if extra1 > extra2:
                return 1
            elif extra1 < extra2:
                return -1
            else:
                return 0
        else:
            return 0

def abandon_card(player, card):
    player.remove(card)
    return player

def landlord_choose():
    while True:
        poker = create_poker()
        poker = shuffle_poker(poker)
        player1, player2, player3, remain_card = deal_poker(poker)
        player1 = sort(player1)
        player2 = sort(player2)
        player3 = sort(player3)
        remain_card = sort(remain_card)
        
        scores = [0, 0, 0]
        landlord_index = -1
        
        print("\n玩家1的牌是:", player1)
        while True:
            try:
                choose1 = int(input("玩家1请叫分（0:不叫,1:1分,2:2分,3:3分）: "))
                if 0 <= choose1 <= 3:
                    scores[0] = choose1
                    break
                else:
                    print("输入错误，请输入0-3的数字")
            except:
                print("输入错误，请输入0-3的数字")
        
        if scores[0] == 3:
            landlord_index = 0
            print("玩家1叫3分，直接成为地主")
        else:
            print(f"玩家1叫分: {scores[0]}分")
            print("玩家2的牌是:", player2)
            while True:
                try:
                    choose2 = int(input("玩家2请叫分（0:不叫,1:1分,2:2分,3:3分）: "))
                    if 0 <= choose2 <= 3:
                        scores[1] = choose2
                        break
                    else:
                        print("输入错误，请输入0-3的数字")
                except:
                    print("输入错误，请输入0-3的数字")
            
            if scores[1] == 3:
                landlord_index = 1
                print("玩家2叫3分，直接成为地主")
            else:
                print(f"玩家1叫分: {scores[0]}分, 玩家2叫分: {scores[1]}分")
                print("玩家3的牌是:", player3)
                while True:
                    try:
                        choose3 = int(input("玩家3请叫分（0:不叫,1:1分,2:2分,3:3分）: "))
                        if 0 <= choose3 <= 3:
                            scores[2] = choose3
                            break
                        else:
                            print("输入错误，请输入0-3的数字")
                    except:
                        print("输入错误，请输入0-3的数字")
                
                if scores[2] == 3:
                    landlord_index = 2
                    print("玩家3叫3分，直接成为地主")
        
        if landlord_index == -1:
            max_score = max(scores)
            
            if max_score == 0:
                print("所有玩家都不叫地主，重新发牌并重新开始叫分")
                continue
            
            if scores[2] == max_score:
                landlord_index = 2
            elif scores[1] == max_score:
                landlord_index = 1
            else:
                landlord_index = 0
        
        print(f"地主牌是: {remain_card}")
        if landlord_index == 0:
            player1.extend(remain_card)
            player1 = sort(player1)
            print("玩家1是地主")
        elif landlord_index == 1:
            player2.extend(remain_card)
            player2 = sort(player2)
            print("玩家2是地主")
        else:
            player3.extend(remain_card)
            player3 = sort(player3)
            print("玩家3是地主")
        
        return (player1, player2, player3, landlord_index)

def circle_abandon_card():
    poker = create_poker()
    poker = shuffle_poker(poker)
    player1, player2, player3, remain_card = deal_poker(poker)
    player1 = sort(player1)
    player2 = sort(player2)
    player3 = sort(player3)
    remain_card = sort(remain_card)
    
    # 接收4个返回值
    player1, player2, player3, landlord_index = landlord_choose()
    
    players = [player1, player2, player3]
    player_names = ["玩家1", "玩家2", "玩家3"]
    
    # 地主先出牌
    current_player = landlord_index
    print(f"游戏开始！{player_names[current_player]}（地主）先出牌")
    
    last_valid_cards = None
    consecutive_passes = 0
    game_over = False
    
    while not game_over:
        print(f"\n{player_names[current_player]}的手牌: {players[current_player]}")
        
        if last_valid_cards is None:
            print("你可以出任意牌型（输入'pass'表示不出）")
        else:
            last_type = get_card_value(last_valid_cards)[0]
            print(f"上一手牌: {last_valid_cards}，牌型: {last_type}")
            print("请出大于上一手的牌或输入'pass'表示不出")
        
        valid_input = False
        while not valid_input:
            choice = input("请选择要出的牌（用空格分隔）或输入'pass': ").strip()
            
            if choice.lower() == 'pass':
                print(f"{player_names[current_player]}选择不出")
                consecutive_passes += 1
                
                if consecutive_passes >= 2:
                    print("连续两家不出，重新开始出牌轮")
                    last_valid_cards = None
                    consecutive_passes = 0
                
                valid_input = True
                break
            
            cards_to_play = choice.split()
            
            invalid_cards = [card for card in cards_to_play if card not in card_value]
            if invalid_cards:
                print(f"错误：这些牌不是合法的牌面: {', '.join(invalid_cards)}")
                print("请重新输入或输入'pass'表示不出")
                continue
            
            player_hand = players[current_player][:]
            missing_cards = []
            for card in cards_to_play:
                if card in player_hand:
                    player_hand.remove(card)
                else:
                    missing_cards.append(card)
            
            if missing_cards:
                print(f"错误：你没有这些牌: {', '.join(missing_cards)}")
                print("请重新输入或输入'pass'表示不出")
                continue
            
            card_type = get_card_value(cards_to_play)
            if card_type is None:
                print("不合法的牌型组合")
                print("请重新输入或输入'pass'表示不出")
                continue
            
            if last_valid_cards is not None:
                comparison = compare_cards(cards_to_play, last_valid_cards)
                if comparison != 1:
                    if comparison == 0:
                        print("错误：不能出和上一手牌一样大的牌")
                    else:
                        print("错误：不能出比上一手牌小的牌")
                    print("请重新输入或输入'pass'表示不出")
                    continue
            
            for card in cards_to_play:
                players[current_player].remove(card)
            
            print(f"{player_names[current_player]}出牌: {cards_to_play}，牌型: {card_type[0]}")
            last_valid_cards = cards_to_play
            consecutive_passes = 0
            valid_input = True
            
            if len(players[current_player]) == 0:
                print(f"\n{player_names[current_player]}出完所有牌，游戏结束！")
                game_over = True
                break
        
        if game_over:
            break
        
        current_player = (current_player + 1) % 3

if __name__ == '__main__':
    circle_abandon_card()