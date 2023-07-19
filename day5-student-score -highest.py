student_scores=[75, 46, 88, 43, 99, 34, 20, 41, 17, 12, 85, 33, 12, 88, 115, 48, 47, 66, 70, 71, 96, 98, 81, 39, 84, 81, 12, 42, 49, 38, 30, 70, 75, 12, 11, 30, 61, 44, 12, 32, 49, 6, 58, 38, 0, 66, 82, 61, 20, 35]
#check the highest score
hightest_score=student_scores[0]
for i in student_scores:
    if i > hightest_score:
        hightest_score=i

print(hightest_score)