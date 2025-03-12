#forloop, sum, find max value in array 

student_scores = [150,230,123,171,185,149,23,59,68,199,78,65,89,86]
total_score = sum(student_scores)
print(total_score)

sum=0
for score in student_scores:
    sum+=score
    
print(sum)

max_score=0
for score in student_scores:
    if score>max_score: 
     max_score=score 
    
print(max_score)
print(max(student_scores))
    
    