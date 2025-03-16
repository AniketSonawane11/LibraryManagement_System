from datetime import date


def show_present(book,book_list):
    book_found = False
    ind = 0
    for one_stud in book_list:
        ls = one_stud.split(",")
       
        if ls[1] == book:
            book_found = True
            break
        ind = ind + 1
    return book_found, ind, ls
   
def Issue_Book():
    std_f, enr =  Search_Student()
    if std_f == True:
     print("Enter Book Name: ")
     book_name = input()
     f = open("all_book","r")
     r = f.readlines()
     f.close()
     found , ind, ls = show_present(book_name,r)
     if found == False:
        print("Book Is Not Available")
     else:
        print("Book Is Available")
        print("BOOK INFO")
        print("|Book No|\tBook Title|\tBook Author|\tBook Publication|")
        print(ls[0],"\t\t",ls[1],"\t        ",ls[2],"\t   ",ls[3])
        ls = ls[0]
        f = open("all_issue","a")
        b = str(date.today())
        res_s =  enr+"," + ls +","+ b +","+ "NA" +"\n"
        print("Book Is Issued To",enr,"Student")
        f.write(res_s)
        f.close()
    else:
        print("-- This Student Is Not Available ---")
def Return_Book():
    found =  list(Search_Student())
    if found[0] == True:
        print("Enter Book No to Return: ")
        book = input()
        f = open("all_issue","r")
        r = f.readlines()
        f.close()
        book_found = False
        ind = 0
        for one_book in r:
          ls = one_book.split(",")
         
          if ls[2] == book+"\n":
            book_found = True
           
          ind = ind + 1
        if book_found == True:
              f = open("all_issue","r")
              all_bks = f.readlines()
              print(all_bks)
              f.close()

              for books in all_bks:
                lst = books.split(",")
                print(lst)
                if str(lst[1]) == str(found[1]) :
                    print("Book Returned By Enr No:",lst[1])
        elif book_found ==False:
            print("Book Not Found")
    else:
        print("Student Not Present")  
   
    pass
def Book_History():
    Search_Book()
    pass
def Student_History():
    pass
def Search_Student():
    print("Enter Enrollment Of Student:")
    enr = input()
    f = open("all_std","r")
    st_list = f.readlines()
    f.close()
    stud_found = False
    ind = 0
    for one_stud in st_list:
        ls = one_stud.split(",")
        if ls[0] == enr:
            stud_found = True
            break
        ind = ind + 1
    if stud_found == True:
        print("Student Is Present")
        print("STUDENT INFO")
        print("|Enrolment No| \tStudent Name| \tMobile No|\tEmail|   | \tClass|")
        print(" ",ls[0],"",ls[1],"  ",ls[2],"   ",ls[3]," ",ls[4])
    else:
        print("STUDENT NOT FOUND!!!!!")
    return stud_found, enr
def Search_Book():
    print("Enter Book Name: ")
    book_name = input()
    f = open("all_book","r")
    r = f.readlines()
    f.close()
    found , ind, ls = show_present(book_name,r)
    if found == False:
        print("Book Is Not Available")
    else:
        print("Book Is Available")
        print("BOOK INFO")
        print("|Book No|\tBook Title|\tBook Author|\tBook Publication|")
        print(ls[0],"\t\t",ls[1],"\t        ",ls[2],"\t   ",ls[3])
   
   

   
    pass
def Add_New_Book():
    f = open("all_book","a")
    print("Enter Book No: ")
    f.write(input())
    print("Enter Book Title: ")
    a = f.write("," + input())
    print("Enter Author: ")
    f.write("," + input())
    print("Enter Publication: ")
    f.write("," + input())
    f.write("\n")
    f.close()
   
def Add_New_Student():
    f = open("all_std","a")
    print("Enter Student Enrollment: ")
    f.write(input())
    print("Enter Student Name: ")
    a = f.write(",\t\t" + input())
    print("Enter Student Mobile: ")
    f.write(",\t" + input())
    print("Enter Student Email: ")
    f.write(",\t" + input())
    print("Enter Student Class: ")
    f.write(",\t" + input())
    f.write("\n")
    f.close()



    pass
def Show_Not_Return_Books():
    pass

def Show_All():
    print("|------------------------STUDENT INFO------------------|")
    print("| Enrollment\t|   Name\t|   Mobile\t\t|    Email\t\t|     Class\t| ")
    f = open("all_std","r")
    r = f.read()
    print(r)
    f.close()

    


while True:
    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Student History")
    print("4 - Book History")
    print("5 - Search Student")
    print("6 - Search Book")
    print("7 - Add New Book")
    print("8 - Add New Student")
    print("9 - Show Not Return Books")
    print("10 - Show All")
    print("11- Exit")
    ch = int(input("Select an option : "))
    if ch==1:
        Issue_Book()
    elif ch==2:
        Return_Book()
    elif ch==3:
        Student_History()
    elif ch==4:
        Book_History()
    elif ch==5:
        Search_Student()
    elif ch==6:
        Search_Book()
    elif ch==7:
        Add_New_Book()
    elif ch==8:
        Add_New_Student()
    elif ch==9:
        Show_Not_Return_Books()
    elif ch==10:
        Show_All()
    elif ch==11:
        exit(0)