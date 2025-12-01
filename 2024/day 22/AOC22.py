# def calculate_2000th_secret(initial_secret):
#     secret = initial_secret
#     for i in range(2000):
#         # Step 1: Multiply by 64, mix, and prune
#         step1 = (secret * 64) % 16777216
#         secret ^= step1
#         secret %= 16777216

#         # Step 2: Divide by 32 (rounded down), mix, and prune
#         step2 = (secret // 32) % 16777216
#         secret ^= step2
#         secret %= 16777216

#         # Step 3: Multiply by 2048, mix, and prune
#         step3 = (secret * 2048) % 16777216
#         secret ^= step3
#         secret %= 16777216

#         # Debug logging for each iteration
#         #print(f"Iteration {i + 1}: Step1={step1}, Step2={step2}, Step3={step3}, Secret={secret}")

#     return secret

# def sum_of_2000th_secrets(file_path):
#     total = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             buyer = int(line.strip())
#             #print(f"Processing buyer with initial secret: {buyer}")
#             final_secret = calculate_2000th_secret(buyer)
#             #print(f"2000th secret for buyer {buyer}: {final_secret}")
#             total += final_secret
#     return total


# file_path = 'hiding.txt'  # Replace with the name of your input file
# result = sum_of_2000th_secrets(file_path)
# print("The sum of the 2000th secret numbers is:", result)


def generate_secrets(initial_secret, count=2000):
    secrets = []
    secret = initial_secret
    for _ in range(count):
        # Step 1: Multiply by 64, mix, and prune
        step1 = (secret * 64) % 16777216
        secret ^= step1
        secret %= 16777216

        # Step 2: Divide by 32 (rounded down), mix, and prune
        step2 = (secret // 32) % 16777216
        secret ^= step2
        secret %= 16777216

        # Step 3: Multiply by 2048, mix, and prune
        step3 = (secret * 2048) % 16777216
        secret ^= step3
        secret %= 16777216

        secrets.append(secret)
    return secrets

def compute_prices(secrets):
    return [s % 10 for s in secrets]

def compute_price_changes(prices):
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]

def find_best_sequence(file_path):
    buyers_data = []
    with open(file_path, 'r') as file:
        for line in file:
            initial_secret = int(line.strip())
            secrets = generate_secrets(initial_secret)
            prices = compute_prices(secrets)
            changes = compute_price_changes(prices)
            buyers_data.append((prices, changes))

    # Find the best sequence of four price changes
    max_bananas = 0
    best_sequence = None

    # Iterate over all possible sequences of four changes
    for i in range(len(buyers_data[0][1]) - 3):
        sequence = buyers_data[0][1][i:i + 4]
        total_bananas = 0

        # Check this sequence for all buyers
        for prices, changes in buyers_data:
            for j in range(len(changes) - 3):
                if changes[j:j + 4] == sequence:
                    total_bananas += prices[j + 4]
                    break

        if total_bananas > max_bananas:
            max_bananas = total_bananas
            best_sequence = sequence

    return max_bananas, best_sequence

file_path = 'hiding.txt'  
max_bananas, best_sequence = find_best_sequence(file_path)
print("Maximum bananas:", max_bananas)
print("Best sequence of changes:", best_sequence)
