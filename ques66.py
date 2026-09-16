#WAP to input marks of 10 students. Store only valid marks between 0 and 100 in a list.Skip invalid marks.#
marks = []

for i in range(10):
    m = int(input("Enter marks: "))

    if m >= 0 and m <= 100:
        marks.append(m)
    else:
        print("Invalid marks skipped")

print("Valid marks: ", marks)