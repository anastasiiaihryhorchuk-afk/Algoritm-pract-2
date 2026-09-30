import random

def generate_matrix(m, n, min_value, max_value):
    matrix = []

    for i in range(m):
        row = []

        for j in range(n):
            row.append(random.randint(min_value, max_value))

        matrix.append(row)

    return matrix

def print_matrix(matrix):
    if not matrix:
        print("Матриця порожня")
        return

    print("\t", end="")

    for j in range(len(matrix[0])):
        print(f"стовпець {j + 1}\t", end="")

    print()

    for i in range(len(matrix)):
        print(f"рядок {i + 1}\t", end="")

        for value in matrix[i]:
            print(f"{value}\t", end="")

        print()


def copy_matrix(matrix):
    return [row[:] for row in matrix]

#завдання 1:
def subtract_row_average(matrix):
    result = copy_matrix(matrix)

    for i in range(len(result)):
        average = sum(result[i]) / len(result[i])

        for j in range(len(result[i])):
            result[i][j] -= average

    return result

#завдання 2:
def shift_matrix(matrix, k):
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    k_right = k % cols
    k_up = k % rows

    result = copy_matrix(matrix)

    for i in range(rows):
        result[i] = (
            result[i][-k_right:] + result[i][:-k_right]
            if k_right != 0
            else result[i]
        )

    result = result[k_up:] + result[:k_up]

    return result

#завдання 3:
def remove_max_rows_and_columns(matrix):
    if not matrix:
        return []

    max_value = max(max(row) for row in matrix)

    print("Максимальний елемент:", max_value)

    rows_to_remove = set()

    cols_to_remove = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max_value:
                rows_to_remove.add(i)
                cols_to_remove.add(j)

    result = []

    for i in range(len(matrix)):
        if i in rows_to_remove:
            continue

        new_row = []

        for j in range(len(matrix[i])):
            if j not in cols_to_remove:
                new_row.append(matrix[i][j])

        if new_row:
            result.append(new_row)

    return result


#завдання 4:
def rotate_90_clockwise(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix

schedule = [
    [
        ["Математика", "Програмування", "Фізика", "Вільне вікно"],
        ["Бази даних", "Програмування", "Вільне вікно", "Англійська"],
        ["Математика", "Фізика", "Програмування", "Бази даних"],
        ["Вільне вікно", "Англійська", "Фізика", "Вільне вікно"],
        ["Програмування", "Математика", "Бази даних", "Фізика"]
    ],

    [
        ["Математика", "Програмування", "Вільне вікно", "Фізика"],
        ["Бази даних", "Програмування", "Англійська", "Вільне вікно"],
        ["Вільне вікно", "Фізика", "Програмування", "Бази даних"],
        ["Математика", "Англійська", "Фізика", "Вільне вікно"],
        ["Програмування", "Математика", "Вільне вікно", "Фізика"]
    ],

    [
        ["Математика", "Вільне вікно", "Фізика", "Програмування"],
        ["Бази даних", "Програмування", "Вільне вікно", "Англійська"],
        ["Математика", "Фізика", "Програмування", "Вільне вікно"],
        ["Вільне вікно", "Англійська", "Фізика", "Бази даних"],
        ["Програмування", "Математика", "Бази даних", "Вільне вікно"]
    ]
]


days = [
    "Понеділок",
    "Вівторок",
    "Середа",
    "Четвер",
    "П'ятниця"
]


def print_schedule(group_number):
    group = schedule[group_number]

    print(f"\nРозклад групи {group_number + 1}:")

    for day in range(5):
        print(f"\n{days[day]}:")

        for lesson in range(4):
            print(f"  {lesson + 1} пара: {group[day][lesson]}")

def busiest_day(group_number):
    group = schedule[group_number]

    max_lessons = 0
    best_day = ""

    for day in range(5):
        lessons = 0

        for lesson in group[day]:
            if lesson != "Вільне вікно":
                lessons += 1

        if lessons > max_lessons:
            max_lessons = lessons
            best_day = days[day]

    print(
        f"\nНайбільше навантаження у групи {group_number + 1}: "
        f"{best_day} ({max_lessons} пар)"
    )

def find_day_with_gaps(group_number):
    group = schedule[group_number]

    print(f"\nДні з вільними вікнами у групи {group_number + 1}:")

    found = False

    for day in range(5):
        if "Вільне вікно" in group[day]:
            print(f"- {days[day]}")
            found = True

    if not found:
        print("Вільних вікон немає")

def find_stream_lessons():
    print("\nПотокові заняття:")

    found = False

    for day in range(5):
        for lesson in range(4):

            subjects = {}

            for group in range(3):
                subject = schedule[group][day][lesson]

                if subject != "Вільне вікно":
                    if subject not in subjects:
                        subjects[subject] = []

                    subjects[subject].append(group + 1)

            for subject in subjects:
                groups = subjects[subject]

                if len(groups) > 1:
                    print(
                        f"{days[day]}, {lesson + 1} пара: "
                        f"{subject} — групи {groups}"
                    )
                    found = True

    if not found:
        print("Потокових занять немає")


print("========================================")
print("ПОЧАТКОВА МАТРИЦЯ")
print("========================================")

matrix = generate_matrix(4, 4, 1, 10)

print_matrix(matrix)

print("\n========================================")
print("ЗАВДАННЯ 1")
print("========================================")

result1 = subtract_row_average(matrix)

print("Після віднімання середнього:")
print_matrix(result1)

print("\n========================================")
print("ЗАВДАННЯ 2")
print("========================================")

k = 1

result2 = shift_matrix(matrix, k)

print(f"Зсув на {k} позицію вправо та догори:")
print_matrix(result2)

print("\n========================================")
print("ЗАВДАННЯ 3")
print("========================================")

result3 = remove_max_rows_and_columns(matrix)

print("Початкова матриця:")
print_matrix(matrix)

print("\nПісля видалення рядків і стовпців:")
print_matrix(result3)

print("\n========================================")
print("ЗАВДАННЯ 4")
print("========================================")

matrix4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("До обертання:")
print_matrix(matrix4)

rotate_90_clockwise(matrix4)

print("\nПісля обертання на 90 градусів:")
print_matrix(matrix4)

print("\n========================================")
print("ДОДАТКОВЕ ЗАВДАННЯ")
print("========================================")

group_number = 0

print_schedule(group_number)

busiest_day(group_number)

find_day_with_gaps(group_number)

find_stream_lessons()