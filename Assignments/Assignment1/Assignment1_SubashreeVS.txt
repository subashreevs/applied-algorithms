from collections import defaultdict, deque
from typing import List

# Question 1 - IUB Free Time Fun

def processOperations(n: int, operations):
    hd = {}
    ac = defaultdict(int)
    ao = deque()
    t = 0
    res = []
    
    for op in operations:
        if op[0] == 1:
            mv = op[1]
            if mv in hd:
                ac[mv] += 1
                ao.append((mv, t))
                t += 1
                res.append(hd[mv][0])
            else:
                res.append(-1)
        elif op[0] == 2:
            mv, rt = op[1]
            if mv in hd:
                hd[mv] = (rt, ac[mv] + 1, t)
                ac[mv] += 1
                ao.append((mv, t))
                t += 1
            else:
                if len(hd) == n:
                    min_ac = min(ac.values())
                    cands = [m for m in hd if ac[m] == min_ac]
                    cands.sort(key=lambda x: hd[x][2])
                    rm = cands[0]
                    del hd[rm]
                    del ac[rm]
                hd[mv] = (rt, 1, t)
                ac[mv] = 1
                ao.append((mv, t))
                t += 1
    
    return res


# Question 3 - Combined Signals Strength

def combine_signals(sigs):
    res = []
    for i in range(len(sigs)-1):
        res.append(sigs[i] | sigs[i+1])
    return res


# Question 4 - Elite Teams

def numberOfTeams(ratings: List[int]) -> int:
    n = len(ratings)
    cnt = 0

    for j in range(n):
        l_s = l_l = r_l = r_s = 0

        for i in range(j):
            if ratings[i] < ratings[j]:
                l_s += 1
            if ratings[i] > ratings[j]:
                l_l += 1
        
        for k in range(j + 1, n):
            if ratings[k] > ratings[j]:
                r_l += 1
            if ratings[k] < ratings[j]:
                r_s += 1

        cnt += l_s * r_l
        cnt += l_l * r_s

    return cnt


# Question 5 - Pirate Crew Task

def findPowerLevels(pwr: list[int]) -> list[int]:
    res = []
    pre_prod = 1

    for i in range(len(pwr)):
        res.append(pre_prod)
        pre_prod *= pwr[i]

    suf_prod = 1
    for i in range(len(pwr)-1, -1, -1):
        res[i] *= suf_prod
        suf_prod *= pwr[i]

    return res


# Question 6 - Anagram Half Match

from collections import Counter

def decrypt(s: str) -> int:
    n = len(s)
    if n % 2 != 0:
        return -1

    mid = n // 2
    first, second = s[:mid], s[mid:]
    cnt1, cnt2 = Counter(first), Counter(second)

    changes = 0
    for ch in cnt2:
        if ch in cnt1:
            if cnt2[ch] > cnt1[ch]:
                changes += cnt2[ch] - cnt1[ch]
        else:
            changes += cnt2[ch]

    return changes


# Question 7 - Count and Say

def magicalScribe(n: int) -> str:
    prev = "1"

    for i in range(1, n):
        j, cnt, tmp = 0, 1, ""
        while j < len(prev) - 1:
            if prev[j] == prev[j+1]:
                cnt += 1
            else:
                tmp += str(cnt) + prev[j]
                cnt = 1
            j += 1
        tmp += str(cnt) + prev[j]
        prev = tmp
    
    return prev


# Question 8 - Vowel Sort Decode

def isVowel(c: str):
    return c in 'aeiouAEIOU'

def sortVowels(code: str) -> str:
    idx, vows = [], []

    for i, ch in enumerate(code):
        if isVowel(ch):
            idx.append(i)
            vows.append(ch)

    vows.sort()

    code_lst = list(code)
    for i, vow in zip(idx, vows):
        code_lst[i] = vow

    return ''.join(code_lst)


# Question 9 - Help Elara

def justifyLine(ln: list[str], w: int, last: bool) -> str:
    if last or len(ln) == 1:
        return ' '.join(ln).ljust(w)

    total_sp = w - sum(len(word) for word in ln)
    gaps = len(ln) - 1

    ev_sp = total_sp // gaps
    ext_sp = total_sp % gaps

    res_ln = ""
    for i in range(len(ln) - 1):
        res_ln += ln[i] + " " * (ev_sp + (1 if i < ext_sp else 0))

    res_ln += ln[-1]
    return res_ln

def helpElara(words: List[str], w: int) -> List[str]:
    res, curr_ln, curr_len = [], [], 0

    for word in words:
        if curr_len + len(word) + len(curr_ln) > w:
            res.append(justifyLine(curr_ln, w, False))
            curr_ln, curr_len = [], 0

        curr_ln.append(word)
        curr_len += len(word)

    if curr_ln:
        res.append(justifyLine(curr_ln, w, True))

    return res


# Question 10 - Cyclonia’s Quest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findTreasure(head):
    if head is None:
        return True

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return False

    return True
