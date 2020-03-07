a = 1

with open(f"data{a}.csv", 'r') as f:
    loss = int(f.readline())

print(f"loss: {loss}")

