N, M = map(int, input().split())
data = list(map(int, input().split()))

# ÀÌÁø Å½»öÀ» Àç±Í¸¦ ÅëÇØ ±¸Çö
def binary_search(array, target, start, end):
    if start > end:  # Å»Ãâ Á¶°Ç
        return None
    mid = (start + end) // 2
    result = 0
    for i in range(N):  # ¼øÈ¸ÇÏ¸ç °¢°¢ ¿ø¼Ò¿¡¼­ mid »©ÁÜ
        if data[i] - mid > 0:
            result += data[i] - mid
        else:
            continue
    if result == target:
        return mid
    elif result > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


data.sort()
end = max(data)
print(binary_search(data, M, 0, end))
