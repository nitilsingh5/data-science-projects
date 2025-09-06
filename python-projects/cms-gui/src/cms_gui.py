import sys
sys.path.append(r'C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\data-science-projects\python-projects\cms\src')
from CMSusing_pickle_and_json import *
from tkinter import *




root=Tk()
root.title('Customer Management System')
root.geometry('600x500')

main_lbl=Label(root,text="Customer Management System",font=1)
main_lbl.place(relx=0.40)

id_lbl=Label(root,text="Enter Cust ID:",font=1)
id_lbl.place(relx=0.1,rely=0.1)
name_lbl=Label(root,text="Cust Name:",font=1)
name_lbl.place(relx=0.1,rely=0.2)
age_lbl=Label(root,text="Cust Age:",font=1)
age_lbl.place(relx=0.1,rely=0.3)
mob_lbl=Label(root,text="Cust Mob:",font=1)
mob_lbl.place(relx=0.1,rely=0.4)

var_id=StringVar()
id_ent=Entry(root,textvariable=var_id,font=1)
id_ent.place(relx=0.3,rely=0.1)
var_name=StringVar()
name_ent=Entry(root,textvariable=var_name,font=1)
name_ent.place(relx=0.3,rely=0.2)
var_age=StringVar()
age_ent=Entry(root,textvariable=var_age,font=1)
age_ent.place(relx=0.3,rely=0.3)
var_mob=StringVar()
mob_ent=Entry(root,textvariable=var_mob,font=1)
mob_ent.place(relx=0.3,rely=0.4)

add_btn=Button(root,text='ADD CUST',font=1,width=12)
add_btn.place(relx=0.01,rely=0.5)
search_btn=Button(root,text='SEARCH CUST',font=1,width=12)
search_btn.place(relx=0.25,rely=0.5)
del_btn=Button(root,text='DEL CUST',font=1,width=12)
del_btn.place(relx=0.49,rely=0.5)
mod_btn=Button(root,text='MODIFY CUST',font=1,width=12)
mod_btn.place(relx=0.73,rely=0.5)
view_btn=Button(root,text='View All',font=1,width=12)
view_btn.place(relx=0.01,rely=0.6)
sort_btn=Button(root,text='SORT CUST',font=1,width=12)
sort_btn.place(relx=0.25,rely=0.6)
save_btn=Button(root,text='SAVE CUST',font=1,width=12)
save_btn.place(relx=0.49,rely=0.6)
load_btn=Button(root,text='LOAD CUST',font=1,width=12)
load_btn.place(relx=0.73,rely=0.6)
clear_btn=Button(root,text='Clear',font=1,width=12)
clear_btn.place(relx=0.35,rely=0.7)
# add_btn=Button(root,text='ADD CUST',font=1)
# add_btn.place(relx=0.1,rely=0.5)
# add_btn=Button(root,text='ADD CUST',font=1)
# add_btn.place(relx=0.1,rely=0.5)


root.mainloop()