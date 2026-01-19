from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

card_counter = Counter(cards)

m = int(input())
targets = list(map(int, input().split()))

print(' '.join(str(card_counter[x]) for x in targets))
