# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2053782
# Date: 09.12.2023
#----------------------------------------------------------------------------------------------

from graphics import *

#Define variables
pass_credits=0
defer_credits=0
fail_credits=0
progress_module_trailer = 0
Progress = 0
Exclude = 0
Do_not_progress_module_retriever = 0

#create lists 
list1=[]
list2=[]
list3=[]
list4=[]

#define function for check the inputs
def value(prompt):
    while True:
        try:
            credit=int(input(prompt))
            credits_lists = [0, 20, 40, 60, 80, 100, 120]
            if credit in credits_lists:
                return credit
            else:
                print("Out of range")
                continue
        except ValueError:
            print("Invalid Integer")

#Histrogram part using graphics.py
#[Got the idea about graphics from YouTube(https://youtu.be/nYhxBVDW7sM?si=JkU4U5ZaI-SNuwc8)]
def graph(y1, y2, y3, y4, outcome):
    def text(c1, c2, size,R,G,B,text,):#Define function for create texts in histrogram
        txt = Text(Point(c1, c2), text)
        txt.setTextColor(color_rgb(R,G,B))
        txt.setSize(size)
        txt.setFace("helvetica")
        txt.setStyle("bold")
        txt.draw(win)

    def rect(c3, c4, c5, c6, c7, c8, c9):#Define function for draw bars in histrogram
        rect1 = Rectangle(Point(c3, c4), Point(c5, c6))
        rect1.setOutline("Black")
        rect1.setFill(color_rgb(c7, c8, c9))#81,81,81
        rect1.draw(win)

    win = GraphWin("Histrogram", 680, 520)
    win.setBackground(color_rgb(237, 242, 236))

    ln = Line(Point(30, 430), Point(650, 430))
    ln.setOutline("Black")
    ln.draw(win)

    rect(60, 430, 190, y1, 174, 250, 161)
    rect(200, 430, 330, y2, 160, 198, 138)
    rect(340, 430, 470, y3, 167, 188, 119)
    rect(480, 430, 610, y4, 210, 182, 181)

    text(170, 25, 28,81,81,81,"Histrogram Results")
    text(210, 485, 25,124,136,149,f"{outcome} Outcomes in total.")
    text(120, 450, 19,124,136,149,"Progress")
    text(265, 450, 19,124,136,149,"Trailer")
    text(410, 450, 19,124,136,149,"Retriever")
    text(550, 450, 19,124,136,149,"Excluded")

    def bar_count(c10, c11, dis):
        txt = Text(Point(c10, c11), dis)
        txt.setSize(23)
        txt.setTextColor("Dark Blue")
        txt.draw(win)

    bar_count(120, bar1, Progress)
    bar_count(265, bar2, progress_module_trailer)
    bar_count(410, bar3, Do_not_progress_module_retriever)
    bar_count(550, bar4, Exclude)

    win.getMouse()
    win.close()

while True:
    try:
        #prompt for inputs
        pass_credits=value("Please enter your credits at pass: ")
        defer_credits=value("Please enter your credit at defer: ")
        fail_credits=value("Please enter your credit at fail : ")

        total_credits = pass_credits+defer_credits+fail_credits
        if total_credits!= 120:
            print("Total Incorrect")
        elif pass_credits == 100:
            print("progress(module trailer)")
            progress_module_trailer += 1
            list2.append([pass_credits,defer_credits,fail_credits])
        elif pass_credits > 100:
            print("Progress")
            list1.append([pass_credits,defer_credits,fail_credits])
            Progress += 1
        elif fail_credits > 60:
            print("Exclude")
            Exclude += 1
            list4.append([pass_credits,defer_credits,fail_credits])
        else:
            print("Do not progress – module retriever")
            Do_not_progress_module_retriever += 1
            list3.append([pass_credits,defer_credits,fail_credits])
        
        
        resubmit = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        while resubmit.lower() not in ['y', 'q']:
            print("Please enter a valid input.")
            resubmit = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if resubmit == 'y':
            pass
        elif resubmit == 'q':
            totalcount = Progress+progress_module_trailer+Exclude+Do_not_progress_module_retriever
            Y1 = 430-(300*Progress/totalcount)
            Y2 = 430-(300*progress_module_trailer/totalcount)
            Y3 = 430-(300*Do_not_progress_module_retriever/totalcount)
            Y4 = 430-(300*Exclude/totalcount)

            bar1 = Y1-15
            bar2 = Y2-15
            bar3 = Y3-15
            bar4 = Y4-15
            graph(Y1, Y2, Y3, Y4, totalcount)
            print("------------------------------------------------------------------")
            print("Part 2:")
            file_name = 'Text File.txt'#[Got the idea about text files from (https://www.w3schools.com/python/python_file_open.asp)]
            file=open(file_name, 'w')
            file.write("Part 3:\n")
            for i in list1:
                print('Progress -',str(i)[1:len(str(i))-1])
                file.write('Progress - '+ str(i)[1:len(str(i))-1]+'\n')
            for i in list2:
                print('Progress (module trailer) -',str(i)[1:len(str(i))-1])
                file.write('Progress (module trailer) - '+ str(i)[1:len(str(i))-1] + '\n')
            for i in list3:
                print('Module retriever -',str(i)[1:len(str(i))-1])
                file.write('Module retriver-'+str(i)[1:len(str(i))-1]+'\n')
            for i in list4:
                print('Exclude – ',str(i)[1:len(str(i))-1])
                file.write('Exclude-'+str(i)[1:len(str(i))-1]+'\n')
            file.close()
            break

    except ValueError:
        print("Invalid Integer")
    except ZeroDivisionError:
        break
        
