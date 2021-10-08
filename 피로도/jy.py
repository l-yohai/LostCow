a, b, c, m = map(int, input().split())
exhaustion = 0
job = 0
for _ in range(24):
    if exhaustion+a<=m:
        job += b
        exhaustion += a
    else:
        exhaustion = max(0, exhaustion-c)

print(job)