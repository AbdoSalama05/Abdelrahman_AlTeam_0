import numpy as np

grades =[[85, 78, 92, 88],
         [70, 76, 80, 65],
         [90, 88, 94, 91],
         [60, 65, 58, 62],
         [100, 95, 98, 97]]
grades_array = np.array(grades)
print("Shape:", grades_array.shape)

print("Mean per student:", np.mean(grades_array, axis=1))
print("Mean per subject:", np.mean(grades_array, axis=0))

average_grades = np.mean(grades_array, axis=1)
top_students = grades_array[average_grades > 85]
print("Top students:\n", top_students)

grades_array=grades_array+5
print("Grades after adding bonus:\n", grades_array)

min_val=np.min(grades_array)
max_val=np.max(grades_array)
grades_array=(grades_array-min_val)/(max_val-min_val)
print("Grades after normalization:\n", grades_array)

grades_array=np.reshape(grades_array, -1)
print("Flattened grades:\n", grades_array)

