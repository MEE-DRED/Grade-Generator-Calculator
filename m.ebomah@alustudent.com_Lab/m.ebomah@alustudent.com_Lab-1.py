class Assignment:
#input collection and assignment category
#FA = Formative
#SA = Summative
#A blueprint that has 4 properties and the assignment category will determine either Formative or Summative.

    def _init_(self, name, category, weight, grade):
        self.name = name
        self.category = category.lower()
        self.weight = weight
        self.grade = grade


class GradeCalculator:
#GradeCalculator
#Each assignment has a maximum grade of 100%.
    def _init_(self):
        self.assignments = []

#Category-wise Grade Totals
#The application will generate:
#The total grade obtained was in the formative category.
#The total grade obtained was in the summative category.
#Percentage is in 100s, so weight and grade must be within 0 and 100.
#Any grade less than zero and grater than 100 will output an error.
    def add_assignment(self, name, category, weight, grade):
        if weight < 0 or weight > 100:
            print("Error: Weight must be within 0 and 100.")
            return
        if grade < 0 or grade > 100:
            print("Error: Grade must be within 0 and 100.")
            return
        self.assignments.append(Assignment(name, category, weight, grade))

#Creating weighted final grade in percentage will output grade * weight / 100
    def calculate_final_grade(self):
        total_weighted_score = 0
        total_weight = 0
        for assignment in self.assignments:
            total_weighted_score += (assignment.grade * assignment.weight / 100)
            total_weight += assignment.weight
        return total_weighted_score if total_weight > 0 else 0

#GPA calculation
#The application will compute the GPA out of 5 based on the weighted grades.
#Convert percentage to GPA scale of 5
    def calculate_gpa(self):
        final_grade = self.calculate_final_grade()
        return round((final_grade / 100) * 5, 2)


#Category-wise Grade Totals
#This will seperate each category to either be Formative or Summative.
#The application will generate:
#The total grade obtained was in the formative category.
#The total grade obtained was in the summative category.


    def categorize_grades(self):
        formative_total = sum(a.grade * a.weight / 100 for a in self.assignments if a.category == "formative")
        summative_total = sum(a.grade * a.weight / 100 for a in self.assignments if a.category == "summative")
        return formative_total, summative_total

#Pass/Fail Decision
#The application will determine whether the student has passed or failed the course based on the following rules:
#Pass: The student must score at or above the average total grade for both the
#Formative and Summative categories.
#Fail and Repeat: The student fails and must repeat the course if:
#They score below the average total grade for either Formative or Summative categories.
#They score below the average total grade for both the Formative and Summative categories

#So, determining the average score for both Formative and Summative will determine pass_or_fail.
    def pass_fail_decision(self):
        formative_total, summative_total = self.categorize_grades()
        avg_formative = formative_total / len([a for a in self.assignments if a.category == "formative"]) if any(a.category == "formative" for a in self.assignments) else 0
        avg_summative = summative_total / len([a for a in self.assignments if a.category == "summative"]) if any(a.category == "summative" for a in self.assignments) else 0

        if avg_formative >= 50 and avg_summative >= 50:
            return "PASS"
        else:
            return "FAIL AND REPEAT!!!"

#To display Final Grade, gpa, formative, summative and pass_fail
    def display_results(self):
        final_grade = self.calculate_final_grade()
        gpa = self.calculate_gpa()
        formative_total, summative_total = self.categorize_grades()
        pass_fail = self.pass_fail_decision()

        print("\n--- FINAL GRADE REPORT ---")
        print(f"Final Grade: {final_grade:.2f}%")
        print(f"GPA: {gpa}/5.0")
        print(f"Formative Total: {formative_total:.2f}%")
        print(f"Summative Total: {summative_total:.2f}%")
        print(f"Result: {pass_fail}")

#Final output display
#Using loops will display results
# Initialize variables
assignments = []
formative_total = 0
summative_total = 0
formative_weight_total = 0
summative_weight_total = 0
total_weight = 0
final_grade = 0

# Start input loop
while total_weight < 100:
    name = input("Enter assignment name (or 'done' to finish): ").strip()
    if name.lower() == 'done':
        break

    category = input("Enter assignment category (Formative/Summative): ").strip().lower()
    if category not in ['fa', 'sa']:
        print("Invalid category! Enter 'fa' for Formative or 'sa' for Summative.")
        continue

    weight = float(input("Enter weight of assignment (%): "))

    # Check if adding the new weight exceeds 100%
    if total_weight + weight > 100:
        print("Total weight cannot exceed 100%! Please enter a valid weight.")
        continue

    grade = float(input("Enter grade obtained (%): "))

    # Store the assignment details
    assignments.append({
        'name': name,
        'category': category,
        'weight': weight,
        'grade': grade
    })

    # Update total weight
    total_weight += weight

# Calculate final grade
for assignment in assignments:
    weighted_score = (assignment['grade'] * assignment['weight']) / 100
    final_grade += weighted_score

    # Categorize as formative or summative
    if assignment['category'] == 'fa':
        formative_total += weighted_score
        formative_weight_total += assignment['weight']
    elif assignment['category'] == 'sa':
        summative_total += weighted_score
        summative_weight_total += assignment['weight']

# Calculate GPA (assuming a 5.0 scale)
gpa = (final_grade / 100) * 5

# Determine pass/fail status
result = "PASS" if final_grade >= 60 else "FAIL AND REPEAT!!!"

# Print final report
print("\n--- FINAL GRADE REPORT ---")
print(f"Total Formative Weight: {formative_weight_total:.2f}%")
print(f"Formative Grade Total: {formative_total:.2f}%")
print(f"Total Summative Weight: {summative_weight_total:.2f}%")
print(f"Summative Grade Total: {summative_total:.2f}%")
print(f"Total Weight: {total_weight:.2f}%")
print(f"Final Grade: {final_grade:.2f}%")
print(f"GPA: {gpa:.2f}/5.0")
print(f"Result: {result}")