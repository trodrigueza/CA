n = int(input())
ans = []
for i in range(n):
    Wpawn_pos = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
    W_pos =  ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    Bpawn_pos = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
    B_pos = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    moves = [str(x) for x in input().split()]
    k = 1
    for move in moves:
        if move[0:2] == move[2:]:
            ans.append(k)
            break
        if k % 2 != 0:
            if move[0:2] not in W_pos and move[0:2] not in Wpawn_pos:
               ans.append(k)
               break
            if move[0:2] in Wpawn_pos:
                if int(move[1]) > int(move[3]):
                    ans.append(k)
                    break
                if int(move[1]) != 2 and (int(move[3]) - int(move[1]) != 1):
                    ans.append(k)
                    break
                elif k == 1 and (int(move[3]) - int(move[1]) > 2):
                    ans.append(k)
                    break
                if move[0:2] in B_pos or move[0:2] in Bpawn_pos:
                    if (ord(move[0]) - 1 == ord(move[2]) or ord(move[0]) + 1 == ord(move[2])) and int(move[1]) + 1 == int(move[3]):
                        if move[0:3] in B_pos:
                            B_pos.remove(move[0:3])
                        else:
                            Bpawn_pos.remove(move[0:3])
                if move[2] != move[0]:
                   if (move[2:] not in Bpawn_pos) and (move[2:] not in B_pos):
                      ans.append(k)
                      break
                   if int(move[1]) + 1 != int(move[3]):
                      ans.append(k)
                      break
                else:
                    if move[2:] in B_pos or move[2:] in Bpawn_pos:
                        ans.append(k)
                        break
                if move[1] == '2' and move[2]+str(int(move[3])-1) in W_pos:
                    ans.append(k)
                    break
                elif move[1]!= '2' and move[2:] in W_pos:
                    ans.append(k)
                    break    
                Wpawn_pos.remove(move[0:2])
                Wpawn_pos.append(move[2:])
            elif move[0:2] in Bpawn_pos:
                ans.append(k)
                break
            else:
                W_pos.append(move[2:])
                if move[0:2] in W_pos:
                    W_pos.remove(move[0:2])
        else:
            if move[0:2] not in B_pos and move[0:2] not in Bpawn_pos:
               ans.append(k)
               break          
            if move[0:2] in Bpawn_pos:
                if int(move[1]) < int(move[3]):
                    ans.append(k)
                    break
                if int(move[1]) != 7 and (int(move[1]) - int(move[3]) != 1):
                    ans.append(k)
                    break
                elif k == 2 and (int(move[1]) - int(move[3]) > 2):
                    ans.append(k)
                    break
                if move[0:2] in W_pos or move[0:2] in Wpawn_pos:
                    if (ord(move[0]) - 1 == ord(move[2]) or ord(move[0]) + 1 == ord(move[2])) and int(move[1]) - 1 == int(move[3]):
                        if move[0:3] in W_pos:
                            W_pos.remove(move[0:3])
                        else:
                            Wpawn_pos.remove(move[0:3])
                if move[2] != move[0]:
                   if (move[2:] not in Wpawn_pos) and (move[2:] not in W_pos):
                      ans.append(k)
                      break
                   if int(move[1]) - 1 != int(move[3]):
                      ans.append(k)
                      break
                else:
                    if move[2:] in W_pos or move[2:] in Wpawn_pos:
                        ans.append(k)
                        break
                if int(move[1]) == 7 and move[2]+str(int(move[3])+1) in B_pos:
                    ans.append(k)
                    break
                elif int(move[1]) != 7 and move[2:] in B_pos:
                    ans.append(k) 
                Bpawn_pos.remove(move[0:2])
                Bpawn_pos.append(move[2:])
            elif move[0:2] in Wpawn_pos:
                ans.append(k)
                break
            else:
                B_pos.append(move[2:])
                if move[0:2] in W_pos:
                    B_pos.remove(move[0:2])
        k += 1
    if len(ans)-1 < i:
        ans.append(0)
print(*ans)