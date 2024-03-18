test_system_answer = int(input())
student_answer = int(input())

if test_system_answer == student_answer and test_system_answer != 1:
    print("YES")
elif test_system_answer != student_answer and (test_system_answer == 1 or student_answer == 1):
    print("NO")
else:
    print("YES")
