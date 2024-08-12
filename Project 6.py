"""
A program to determine the grade of a student using the rubric for Gettysburg College. 

@author: Sackitey Joseph

"""


# Defining function to calculate the numerical grade of coding assignment
def coding_assignment(scores):
    #list to store all the scored marks of the coding assignment
    coding = []
    #list to store all the total marks of the coding assignment
    total_marks=[]
    
    # This for loop iterate through the values in the assignment_grades list and append all the marks scored in coding[]
    # It appends the total marks in total_marks[]
    for value in assignment_grades:
        
        coding.append(value[0])
        total_marks.append(value[1])       
      
    total_score= sum(coding)
    tmarks= sum(total_marks)
    # To calculate the numerical percentage out of 40 percent
    assignment_percent=(total_score/tmarks)*40
       
    return assignment_percent



# Second function to calculate the numerical quiz score
def quiz_score(quiz_grades):
    #list to store all the scored marks for the quiz
    quiz_list=[]
    # list to store all the total of all the quizzes
    tquiz_list=[]
    
    for grade in quiz_grades:
        # to append the quiz scores into quiz_list and total marks into tquiz_list
        quiz_list.append(grade[0])
        tquiz_list.append(grade[1])
    
    # calculate the numerical value of the quiz out of 10 percent    
    total_score=sum(quiz_list)
    total_marks= sum(tquiz_list)
    quiz_percent=(total_score/total_marks)*10
    
    return quiz_percent  
     
# Defining third function to calculate exam score
def exam_score(exam_grades):
 # A list to store the difference between the marks and the total score for each exam to determine the max, min, and mid value
 # The index of the difference will point to the index of the highest mark, least marks and mid mark values in exam_score
    difference_list = []  
 # A list to store the overall marks of all the exams   
    texam_list=[]
    # a list to store the marks scored for each exam
    exam_list=[]
    
    for score in exam_grades:
        # the total scores are appended in texam_list for easy iteration
        texam_list.append(score[1])
        # the marks scored in each exam are appended in texam_list for easy iteration
        exam_list.append(score[0])
        
        difference = score[1] - score[0]
        
        difference_list.append(difference)
    # the exam with the max difference will be the least performed exam   
    max_difference = max(difference_list)
    
    index_of_max_difference = difference_list.index(max_difference)
    # the exam with the least diference will the best performed exam
    min_difference = min(difference_list)
    
    index_of_min_difference= difference_list.index(min_difference)
    
    # the exam with the mid_difference will be the second best exam
    mid_difference = sum(difference_list)-min_difference-max_difference
    
    index_of_mid_difference= difference_list.index(mid_difference)
    
    
    # calculating the numeric values of each set using the indfex of the differences
    exam_percentage_least = (exam_list[index_of_max_difference] /texam_list[index_of_max_difference]) *15
    
    exam_percent_highest= (exam_list[index_of_min_difference]/ texam_list[index_of_min_difference])*20
    
    exam_percent_mid = (exam_list[index_of_mid_difference]/texam_list[index_of_mid_difference])* 15
   
    
    total_exam_score = exam_percent_highest + exam_percent_mid + exam_percentage_least
    
    
    return total_exam_score
    
       
# to calculate and print the final grade and letter grade    
def final_grade(exam_score,quiz_score,coding_assignment):
    
    final_score = exam_score(exam_grades) + quiz_score(quiz_grades)+coding_assignment(assignment_grades)
    
    grade_message = f"\nFor a grade of {final_score:.2f}%\n\t"
    
    
    
    
    # >98* A+ 93 – 100 A 90 - 92 A 88 – 89 B+ 
    # 83 - 87 B 80 – 82 B 78 - 79 C+ 70 – 77 C 70 - 72 C
    # 70 – 76 D+ 60 - 67 D 0 – 59 F

    letter_grade = ""
    
    if final_score >= 98:
        letter_grade = "A+"
    elif final_score >= 93:
        letter_grade = "A"
    elif final_score >= 90:
        letter_grade = "A-"
    elif final_score >= 88:
        letter_grade = "B+"
    elif final_score >= 83:
        letter_grade = "B"
    elif final_score >= 80:
        letter_grade = "B-" 
    elif final_score >= 78:
        letter_grade = "C+"
    elif final_score >= 73:
        letter_grade = "C"
    elif final_score >= 70:
        letter_grade = "C-"       
    elif final_score >= 68:
        letter_grade = "D+"  
    elif final_score >= 60:
        letter_grade = "D"
        
    else:
        letter_grade = "F"
        
    grade_message += f"\n\tLetter grade: {letter_grade}"

    
    final_result = print(grade_message)
    
    return final_result


    
quiz_grades =        [[11, 14]
                     , [12, 13]
                     , [10, 10]
                     , [8, 10]
                     , [14, 14]
                     , [7, 10]
                     , [12, 15]
                     , [9, 9]
                     , [11, 12]]

assignment_grades = [[98, 100]
                     , [87, 100]
                     , [100, 100]
                     , [82, 100]
                     , [96, 100]
                     , [97, 100]
                     , [92, 100]
                     , [78, 100]
                     , [100, 100]]

exam_grades = [[52, 52]
               , [60, 68]
               , [60, 64]]    
    
final_grade(exam_score,quiz_score,coding_assignment)    
print(quiz_score(quiz_grades))
