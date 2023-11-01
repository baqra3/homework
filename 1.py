score1 = int(input("Enter Score1:"))
score2 = int(input("Enter Score2:"))
score3 = int(input("Enter Score3:"))
score4 = int(input("Enter Score4:"))

avg_score = (score1 + score2 + score3 + score4 ) / 4
if avg_score > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")

elif avg_score < 5 :
    print("გილოცავ გაექეცი მატრიცას")

if (avg_score) > 5 and (avg_score) < 9:
    print("YOU ARE MID")

elif (avg_score) > 10 and (avg_score) < 0: 
    print("there is something wrong with you")




