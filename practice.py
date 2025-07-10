s, k, h = map(int, input().split())

if s + h + k >= 100:
    print("OK")
else:
    if (s < h < k) or (s < k < h):
        print("Soongsil")
    if (h < s < k) or (h < k < s):
        print("Hanyang")
    if (k < s < h) or (k < h < s):
        print("Korea")