from flask import Flask, render_template, request
import pandas as pd
from markupsafe import Markup

app = Flask(__name__)

dfs = pd.read_excel("sampledata.xlsx", sheet_name=None)

print(dfs)

studentSheet = dfs["student answers"]
#studentSheet = studentSheet.loc[0]
print(studentSheet["Answer"])
studentSheet['Answer'] = (
    studentSheet['Answer'].fillna('').str.replace('\n', '<br>', regex=False)
)

rubricSheet = dfs["rubric"]
questionSheet = dfs["question versions"]

studentSheet["Teacher Score 1"] = studentSheet["Teacher Score 1"].astype(float)
studentSheet["Teacher Score 2"] = studentSheet["Teacher Score 2"].astype(float)
studentSheet["Teacher Score 3"] = studentSheet["Teacher Score 3"].astype(float)


#-------- Trying to make tables static this calling them outside of the routing and main flask as they dont need to change

rubric_table = dfs["rubric"].copy()
rubric_table = rubric_table.fillna('')
rubric_table = rubric_table.replace(r'\n', '<br>', regex=True)
STATIC_RUBRIC_HTML = Markup(rubric_table.to_html(index=False, border=0, escape=False))

question_table = dfs["question versions"].copy()
question_table = question_table.fillna('')
question_table = question_table.replace(r'\n', '<br>', regex=True)
question_table = question_table.rename(columns={"Unnamed: 0": " "})
STATIC_QUESTION_HTML = Markup(question_table.to_html(index=False, border=0, escape=False))

#--------


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    studentSheet = dfs["student answers"]
    
    studentSheet = studentSheet.drop(columns=['Q Title', 'Q Text', 'Difficulty', 'Bonus?', 'Answer Match'])

    print("hello")
    if request.method == "POST":
        print("hello2")
        for index in studentSheet.index:
            print(f"Teacher Score 1 {index}")
            print(request.form[f"Teacher Score 1 {index}"])
            studentSheet.loc[index, "Teacher Score 1"] = float(
                request.form[f"Teacher Score 1 {index}"]
            )

            studentSheet.loc[index, "Teacher Score 2"] = float(
                request.form[f"Teacher Score 2 {index}"]
            )

            studentSheet.loc[index, "Teacher Score 3"] = float(
                request.form[f"Teacher Score 3 {index}"]
            )

        message = "All teacher scores saved successfully."
    
    students = []

    
    for idx, row in studentSheet.iterrows():
        record = row.to_dict()
        record["row_index"] = idx
        students.append(record)

    return render_template(
        "table.html",
        students=students,
        message=message
    )

@app.route("/student/<int:index>", methods=["GET", "POST"])
def student(index):
    global STATIC_RUBRIC_HTML, STATIC_QUESTION_HTML
    
    message = ""
    
    student = studentSheet.loc[index]

    if request.method == "POST": 
       
        rubric1 = float(request.form["Teacher Score 1"]) 
        rubric2 = float(request.form["Teacher Score 2"]) 
        rubric3 = float(request.form["Teacher Score 3"]) 

       
        studentSheet.loc[index, "Teacher Score 1"] = rubric1 
        studentSheet.loc[index, "Teacher Score 2"] = rubric2 
        studentSheet.loc[index, "Teacher Score 3"] = rubric3 
        
        
        studentSheet.to_csv("students.csv", index=False)
        
        message = "Scores saved successfully."
        
    student = studentSheet.iloc[index]
    
 
    # student = {}

    # total_rows = len(dfs["student answers"])

    # for sheet_name in ["student answers", "rubric", "question versions"]:
    #     current_sheet = dfs[sheet_name]
    #     if index < len(current_sheet):
    #         student[sheet_name] = current_sheet.iloc[index].to_dict()
    #     else:
    #         student[sheet_name] = {}
#----------------------------------------------
    # This part acts to set up tables that import the entire rubric, question rubric, and indidivual student answers
    # total_rows = len(dfs["student answers"])

    #iloc only calls one of the cells at a time rather than the entire table, dont use for rubric or question
    # student_table = studentSheet.iloc[[index]]
    # student_table = student_table.replace(r'\n', ' ', regex=True)
    # student_table = student_table.map(lambda x: str(x).replace('\n','<br>' '\n') if isinstance(x, str) else x)
    # student_HTML = student_table.to_html(index=False, border=0)


    return render_template(
        "student.html",
        student=student,
        #student_table=Markup(student_HTML),
        rubric_table=STATIC_RUBRIC_HTML,
        question_table=STATIC_QUESTION_HTML,
        index=index,
        total=len(studentSheet),
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)