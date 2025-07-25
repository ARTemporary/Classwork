## Module 11 Lab Part 1

# almost exactly from instructions
def read_scores(filename):
    scores = []
    with open(filename, 'r', encoding= 'utf-8') as file:    # the default encoding could not read the special characters in the scores.txt so must encoded using utf-8
        for line in file:
            name, score = line.split(',')    # split and then stripped 
            scores.append((name.strip(), int(score.strip())))
    return scores

# testing the funciton
# print(read_scores('./Class/Module11Lab/scores.txt'))

def calculate_average(scores):
    total = sum(score for _, score in scores)
    return total / len(scores)

# # Test the function
# scores = read_scores('./Class/Module11Lab/scores.txt')
# print(f"Average score: {calculate_average(scores):.2f}")

def write_report(scores, average):
    with open('./Class/Module11Lab/report.txt', 'w', encoding= 'utf-8') as file:
        file.write("Test Results\n")
        file.write("=============================\n\n")
        for name, score in scores:
            file.write(f"{name}: {score}\n")
        file.write(f"\nClass Average: {average:.2f}")

# Generate the report
scores = read_scores('./Class/Module11Lab/scores.txt')
average = calculate_average(scores)
write_report(scores, average)
print("Report generated in 'report.txt'!")
