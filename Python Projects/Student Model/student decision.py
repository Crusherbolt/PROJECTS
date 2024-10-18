from tkinter import *
import numpy as np
import pandas as pd

FONT = ("Courier", 12, "bold")
FONT1 = ("Courier", 10, "bold")
FONT2 = ("Courier", 11, "bold")

l1=['Drawing','Dancing','Singing','Sports','Video Game','Acting','Travelling',
    'Gardening','Animals','Photography','Teaching',
    'Exercise','Coding','Electricity Components','Mechanic Parts','Computer Parts','Researching','Architecture',
    'Historic Collection','Botany','Zoology','Physics','Accounting','Economics','Sociology','Geography',
    'Psycology','History','Science','Bussiness Education','Chemistry','Mathematics','Biology','Makeup','Designing',
    'Content writing','Crafting','Literature','Reading','Cartooning','Debating','Asrtology',
    'Hindi','French','English','Other Language',
    'Solving Puzzles','Gymnastics','Yoga','Engeeniering','Doctor','Pharmisist','Cycling','Knitting',
    'Director','Journalism','Bussiness','Listening Music'
]

Course=['BBA- Bachelor of Business Administration',
'BEM- Bachelor of Event Management',
'Integrated Law Course- BA + LL.B',
'BJMC- Bachelor of Journalism and Mass Communication',
'BFD- Bachelor of Fashion Designing',
'BBS- Bachelor of Business Studies',
'BTTM- Bachelor of Travel and Tourism Management',
'BVA- Bachelor of Visual Arts',
'BA in History',
'B.Arch- Bachelor of Architecture',
'BCA- Bachelor of Computer Applications',
'B.Sc.- Information Technology',
'B.Sc- Nursing',
'BPharma- Bachelor of Pharmacy',
'BDS- Bachelor of Dental Surgery',
'Animation, Graphics and Multimedia',
'B.Sc- Applied Geology',
'B.Sc.- Physics',
'B.Sc. Chemistry',
'B.Sc. Mathematics',
'B.Tech.-Civil Engineering',
'B.Tech.-Computer Science and Engineering',
'B.Tech.-Electrical and Electronics Engineering',
'B.Tech.-Electronics and Communication Engineering',
'B.Tech.-Mechanical Engineering',
'B.Com- Bachelor of Commerce',
'BA in Economics',
'CA- Chartered Accountancy',
'CS- Company Secretary',
'Diploma in Dramatic Arts',
'MBBS',
'Civil Services',
'BA in English',
'BA in Hindi',
'B.Ed.'
]

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

df = pd.read_csv("stud_training.csv")   ##Training csv file

df.replace({'Courses':{'BBA- Bachelor of Business Administration':0,
'BEM- Bachelor of Event Management':1,
'Integrated Law Course- BA + LL.B':2,
'BJMC- Bachelor of Journalism and Mass Communication':3,
'BFD- Bachelor of Fashion Designing':4,
'BBS- Bachelor of Business Studies':5,
'BTTM- Bachelor of Travel and Tourism Management':6,
'BVA- Bachelor of Visual Arts':7,
'BA in History':8,
'B.Arch- Bachelor of Architecture':9,
'BCA- Bachelor of Computer Applications':10,
'B.Sc.- Information Technology':11,
'B.Sc- Nursing':12,
'BPharma- Bachelor of Pharmacy':13,
'BDS- Bachelor of Dental Surgery':14,
'Animation, Graphics and Multimedia':15,
'B.Sc- Applied Geology':16,
'B.Sc.- Physics':17,
'B.Sc. Chemistry':18,
'B.Sc. Mathematics':19,
'B.Tech.-Civil Engineering':20,
'B.Tech.-Computer Science and Engineering':21,
'B.Tech.-Electrical and Electronics Engineering':22,
'B.Tech.-Electronics and Communication Engineering':23,
'B.Tech.-Mechanical Engineering':24,
'B.Com- Bachelor of Commerce':25,
'BA in Economics':26,
'CA- Chartered Accountancy':27,
'CS- Company Secretary':28,
'Diploma in Dramatic Arts':29,
'MBBS':30,
'Civil Services':31,
'BA in English':32,
'BA in Hindi':33,
'B.Ed.':34
}},inplace=True)

X = df[l1]
y = df[["Courses"]]
np.ravel(y)

tr = pd.read_csv("stud_testing.csv", on_bad_lines='skip') # Testing csv file

tr.replace({'Courses':{'BBA- Bachelor of Business Administration':0,
'BEM- Bachelor of Event Management':1,
'Integrated Law Course- BA + LL.B':2,
'BJMC- Bachelor of Journalism and Mass Communication':3,
'BFD- Bachelor of Fashion Designing':4,
'BBS- Bachelor of Business Studies':5,
'BTTM- Bachelor of Travel and Tourism Management':6,
'BVA- Bachelor of Visual Arts':7,
'BA in History':8,
'B.Arch- Bachelor of Architecture':9,
'BCA- Bachelor of Computer Applications':10,
'B.Sc.- Information Technology':11,
'B.Sc- Nursing':12,
'BPharma- Bachelor of Pharmacy':13,
'BDS- Bachelor of Dental Surgery':14,
'Animation, Graphics and Multimedia':15,
'B.Sc- Applied Geology':16,
'B.Sc.- Physics':17,
'B.Sc. Chemistry':18,
'B.Sc. Mathematics':19,
'B.Tech.-Civil Engineering':20,
'B.Tech.-Computer Science and Engineering':21,
'B.Tech.-Electrical and Electronics Engineering':22,
'B.Tech.-Electronics and Communication Engineering':23,
'B.Tech.-Mechanical Engineering':24,
'B.Com- Bachelor of Commerce':25,
'BA in Economics':26,
'CA- Chartered Accountancy':27,
'CS- Company Secretary':28,
'Diploma in Dramatic Arts':29,
'MBBS':30,
'Civil Services':31,
'BA in English':32,
'BA in Hindi':33,
'B.Ed.':34
}},inplace=True)

X_test= tr[l1]
y_test = tr[["Courses"]]
np.ravel(y_test)

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
#     from sklearn.metrics import accuracy_score
#     y_pred=clf3.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    inter = [Interest1.get(),Interest2.get(),Interest3.get(),Interest4.get(),Interest5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in inter:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(Course)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, Course[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
#     from sklearn.metrics import accuracy_score
#     y_pred=clf4.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    inter = [Interest1.get(),Interest2.get(),Interest3.get(),Interest4.get(),Interest5.get()]

    for k in range(0,len(l1)):
        for z in inter:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(Course)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, Course[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")

def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
#     from sklearn.metrics import accuracy_score
#     y_pred=gnb.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    inter = [Interest1.get(),Interest2.get(),Interest3.get(),Interest4.get(),Interest5.get()]
    for k in range(0,len(l1)):
        for z in inter:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(Course)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, Course[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

root = Tk()
root.configure(background='#C4F5F8')

# entry variables
Interest1 = StringVar()
Interest1.set(None)
Interest2 = StringVar()
Interest2.set(None)
Interest3 = StringVar()
Interest3.set(None)
Interest4 = StringVar()
Interest4.set(None)
Interest5 = StringVar()
Interest5.set(None)
Name = StringVar()

# Heading
w2 = Label(root, justify=LEFT, text="Course Predictor using Machine Learning", fg="black", bg="#C4F5F8")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)
w2.config(font=("Aharoni", 30))
w2.grid(row=2, column=0, columnspan=2, padx=100)

# labels
NameLb = Label(root, text="Name of the Student", fg="yellow", bg="black", font=FONT1)
NameLb.grid(row=6, column=1, pady=15, sticky=W)


S1Lb = Label(root, text="Interest 1", fg="yellow", bg="black",font=FONT1)
S1Lb.grid(row=7, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="Interest 2", fg="yellow", bg="black", font=FONT1)
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="Interest 3", fg="yellow", bg="black", font=FONT1)
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root, text="Interest 4", fg="yellow", bg="black", font=FONT1)
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root, text="Interest 5", fg="yellow", bg="black", font=FONT1)
S5Lb.grid(row=11, column=1, pady=10, sticky=W)


lrLb = Label(root, text="DecisionTree", fg="black", bg="red", font=FONT2)
lrLb.grid(row=15, column=1, pady=10,sticky=W)

destreeLb = Label(root, text="RandomForest", fg="black", bg="red",font=FONT2)
destreeLb.grid(row=17, column=1, pady=10, sticky=W)

ranfLb = Label(root, text=" NaiveBayes ", fg="black", bg="red", font=FONT2)
ranfLb.grid(row=19, column=1, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name, font=FONT2)
NameEn.grid(row=6, column=1)

S1En = OptionMenu(root, Interest1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Interest2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Interest3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Interest4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Interest5,*OPTIONS)
S5En.grid(row=11, column=1)


dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="yellow",font=FONT)
dst.grid(row=8, column=3,padx=10)

rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow",font= FONT)
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text=" NaiveBayes ", command=NaiveBayes,bg="green",fg="yellow",font=FONT)
lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="black",font=FONT1)
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="white",fg="black",font=FONT1)
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="white",fg="black",font=FONT1)
t3.grid(row=19, column=1 , padx=10)

root.mainloop()