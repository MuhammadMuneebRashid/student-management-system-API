# Import the Random Module to work with rest APIS
import requests
# Base API URL
url="https://jsonplaceholder.typicode.com/posts"
# Request headers
headers={
    "Content-type":"application/json"
}
# Display the menu until the user chooses to exit
while True:
    # Show menu options
    print("=== Student Management System ===")
    print("1. Register Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Exit")
    # Get user's menu choice
    choice=int(input("Enter the choice :"))
    # Register a new student using POST request
    if (choice==1):
        # Collect student information
        name=input("Enter the student name:")
        roll_no=int(input("Enter the roll number:"))
        department=input("Enter the department:")
        semester=input("Enter the semester:")
        email=input("Enter the email id:")
        # Create JSON data send to the API
        data={
            "Name":name,
            "Roll_No":roll_no,
            "Department":department,
            "Semester":semester,
            "Email":email
        }
        try:
            # Send POST request to register student
            response=requests.post(url,headers=headers,json=data)
            print("Status Code:",response.status_code)
            if response.status_code==201:
                print("Student Registered Successfully ")
            else:
                print("Registration failed")
            Data=response.json()
            print("\n Server Response")
            print(Data)
        except requests.exceptions.RequestException:
            print("APIS Error")
    # Update existing student information using PUT request
    elif (choice==2):
         # Get student id and updated information
         student_id=int(input("Enter the student id:"))
         new_name=input("Enter the new name:")
         new_department=input("Enter the new department:")
         new_semester=input("Enter the new semester:")
         # Create updated JSON data
         new_data={
             "Student_ID":student_id,
             "New Name":new_name,
             "New Department":new_department,
             "New Semester":new_semester
        }
         # Create URL for the selected student
         updated_url=f"https://jsonplaceholder.typicode.com/posts/{student_id}"
         try:
             # Send PUT request to update student data
             response=requests.put(updated_url, headers=headers, json=new_data)
             print("Status_Code:",response.status_code)
             if response.status_code==200:
                 print(" Student info is successfully Updated")
             else:
                 print("Student info isn't updated")
             response_data=response.json()
             print("\n Server Response")
             print(response_data)
         except requests.exceptions.RequestException:
             print("APIS Error")
    # Delete a student using DELETE request
    elif (choice==3):
        # Get student ID to delete
        student_id=input("Enter the student id:")
        # Create URL for the selected student
        url=f"https://jsonplaceholder.typicode.com/posts/{student_id}"
        try:
            # Send DELETE request 
            response=requests.delete(url,headers=headers)
            print("Status Code:",response.status_code)
            if (response.status_code==200 or response.status_code==204):
                print("Student deleted successfully")
            else:
                print("Deletion failed")
        except  requests.exceptions.RequestException:
            print("Apis error")
    # Exit the application
    elif (choice==4):
        print("Thankyou for using Student Management System")
        break
    # Handle Invalid Choice
    else:
        print("Invalid Choice")




    

