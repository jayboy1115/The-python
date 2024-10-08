import decimal

def get_student_scores(num_students, num_subjects):
    scores = []
    for count in range(num_students):
        student_scores = []
        print("Entering score for student", count + 1)
        for index in range(num_subjects):
            while True:
                score = int(input("Enter score for subject " + str(index + 1) + ": "))
                if 0 <= score <= 100:
                    student_scores.append(score)
                    print("Saving >>>>>>>>>>>>>>>>>>>>> saved successfully")
                    break
                else:
                    print("Invalid score. Please enter a score between 0 and 100.")
        scores.append(student_scores)
    return scores

def calculate_statistics(scores, num_subjects):
    totals = []
    averages = []
    for count, student_scores in enumerate(scores):
        total = sum(student_scores)
        average = decimal.Decimal(total) / decimal.Decimal(num_subjects)
        totals.append(total)
        averages.append(average)
    return totals, averages

def find_hardest_and_easiest_subjects(scores, num_subjects):
    hardest_subject = 0
    easiest_subject = 0
    hardest_subject_fails = 0
    easiest_subject_passes = 0
    for index in range(num_subjects):
        num_passes = 0
        num_fails = 0
        for count in range(len(scores)):
            if scores[count][index] >= 50:
                num_passes += 1
            else:
                num_fails += 1
        if num_fails > hardest_subject_fails:
            hardest_subject = index
            hardest_subject_fails = num_fails
        if num_passes > easiest_subject_passes:
            easiest_subject = index
            easiest_subject_passes = num_passes
    return hardest_subject, easiest_subject, hardest_subject_fails, easiest_subject_passes

def find_overall_highest_score(scores):
    overall_highest_score = 0
    overall_highest_score_student = 0
    overall_highest_score_subject = 0
    for count in range(len(scores)):
        for index in range(len(scores[count])):
            if scores[count][index] > overall_highest_score:
                overall_highest_score = scores[count][index]
                overall_highest_score_student = count
                overall_highest_score_subject = index
    return overall_highest_score, overall_highest_score_student, overall_highest_score_subject

def find_best_and_worst_graduating_students(totals):
    best_graduating_student = 0
    best_graduating_student_score = 0
    worst_graduating_student = 0
    worst_graduating_student_score = 0
    for count in range(len(totals)):
        if totals[count] > best_graduating_student_score:
            best_graduating_student = count
            best_graduating_student_score = totals[count]
        if totals[count] < worst_graduating_student_score or worst_graduating_student_score == 0:
            worst_graduating_student = count
            worst_graduating_student_score = totals[count]
    return best_graduating_student, best_graduating_student_score, worst_graduating_student, worst_graduating_student_score


num_students = int(input("How many students do you have? "))
num_subjects = int(input("How many subjects do they offer? "))
scores = get_student_scores(num_students, num_subjects)
totals, averages = calculate_statistics(scores, num_subjects)
hardest_subject, easiest_subject, hardest_subject_fails, easiest_subject_passes = find_hardest_and_easiest_subjects(scores, num_subjects)
overall_highest_score, overall_highest_score_student, overall_highest_score_subject = find_overall_highest_score(scores)
best_graduating_student, best_graduating_student_score, worst_graduating_student, worst_graduating_student_score = find_best_and_worst_graduating_students(totals)
print("\nThe hardest subject is subject", hardest_subject + 1, "with", hardest_subject_fails, "failures")
print("The easiest subject is subject", easiest_subject + 1, "with", easiest_subject_passes, "passes")
print("The overall highest score is scored by student", overall_highest_score_student + 1, "in subject", overall_highest_score_subject + 1, "scoring:", overall_highest_score)
print("\n============================================================== CLASS SUMMARY =======================================")
print("Best graduating student is: student", best_graduating_student + 1, "scoring:", best_graduating_student_score)
print("=============================================== !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Worst graduating student is: student", worst_graduating_student + 1, "scoring:", worst_graduating_student_score)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("===============================================================")
