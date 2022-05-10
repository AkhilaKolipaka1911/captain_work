import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writerow(["Name", "Age", "Contact Number", "E-Mail ID"])
            
        writer.writerow(info_list)
if__name__=='__main__':
    condition = True
    student_num = 1
    
    while(condition):
            student_info = input("enter student information in the following formate (Name Age Contact_Number E-mail_id: ") ")

           # print("Entered information"+student_info)

            student_info_list = student_info.split('')
            #print("Entered split up information is: " str(student_info_list))
            printf("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nEmail ID: {}".formate(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]})
            choice_check = input("Is the entered information correct? (yes/no):")
            #write_into_csv(student_info_list)

            if choice_check == "yes":
                write_into_csv(student_info_list)

                condition_check = input("Enter (yes/no) if you want to enter information: ")
                if condition_check == "yes":
                    condition = True
                    student_num = student_num + 1
                elif condition_check == "no":
                    condition = False
            elif choice_check == "no":
                print("\nPlese re-enter the values!")
