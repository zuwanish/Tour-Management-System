from tkinter import *
import tkinter, threading
from tkinter import messagebox as tmsg
from tkinter import ttk
import random
import datetime
import imageio
import time
from PIL import Image, ImageTk
import smtplib as s
import config

root1 = Tk()
root1.geometry("1208x830")
root1.wm_iconbitmap("Artboard 1.ico")
root1.minsize(1208, 830)
root1.maxsize(1208, 830)
root1.title("ＲＹＯＣＯ ＴＯＵＲＳ© 2021")
video_name = "video1.mp4" #This is your video file path
video = imageio.get_reader(video_name)


def dr1():
    time.sleep(2)
    root1.destroy()


def login_window():
    root2 =Toplevel()
    # global dr1, root3
    root2.geometry("1202x802")
    root2.minsize(1202, 802)
    root2.maxsize(1202, 802)
    root2.wm_iconbitmap("Artboard 1.ico")
    root2.title("RYOCO SIGNIN")
    load = Image.open("LOGIN1.png")
    render = ImageTk.PhotoImage(load)
    jpg = Label(root2, image=render)
    jpg.place(x=0, y=0)

    #def statusr1():
        # for i in range(2):
        #     statusvar.set("Busy.")
        #     statusbar.update()
        #
        #     time.sleep(0.2)
        #     statusvar.set("Busy..")
        #     statusbar.update()
        #
        #     time.sleep(0.2)
        #     statusvar.set("Busy...")
        #     statusbar.update()
        #
        #     time.sleep(0.2)
        #     statusvar.set("Busy....")
        #     statusbar.update()
        #
        #     time.sleep(0.2)

        # x = 0
        # for i in range(101):
        #     statusvar.set(f"LOADING {x}%")
        #     statusbar.update()
        #     time.sleep(0.0000001)
        #     x += 1
        #
        # statusvar.set("READY TO USE")
        # statusbar.update()
        # time.sleep(0.5)
        # statusvar.set("PROCEED ENTERING YOUR DATA\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tＲＹＯＣＯ ＴＯＵＲＳ© 2021")



    def register():
        with open("ryoco_credentials.txt", 'r') as l:
            m = l.read()
            l.close()
        if reg_name_entry.get() == "" or reg_cnic_entry.get() == '' or reg_contact_entry == "" or reg_email_entry == "" or reg_password_entry == '' or reg_username_entry == '':
            tmsg.showerror('ENTRY INVALID', 'PLEASE ENTER COMPLETE DETAILS!', parent=root2)

        elif len(reg_cnic_entry.get()) != 13:
            tmsg.showerror('ENTRY INVALID', 'CNIC NOT VALID!', parent=root2)

        elif len(reg_contact_entry.get()) != 11:
            tmsg.showerror('ENTRY INVALID', 'CONTACT NOT VALID!', parent=root2)
        # elif reg_username_entry in m:
        #     tmsg.showerror('ENTRY INVALID', 'USERNAME ALREADY REGISTERED!', parent=root2)
        else:
            a = tmsg.showinfo("Registeration Successful", "Your information has been registered!", parent=root2)
            print(f'''
            ======================================================================================

            First Name:  {reg_name_entry.get()}
            CNIC No : \t {reg_cnic_entry.get()}

            Contact: \t {reg_contact_entry.get()}
            E-mail: \t {reg_email_entry.get()}
            \nCONFIDENTIAL DETAILS
            username:\t {reg_username_entry.get()}'
            Password: {reg_password_entry.get()}


            ''')

            with open(f"{reg_username_entry.get()}_Record.txt", "a") as f:
                try:
                    f.write(f'''
            =========================================================================
            First Name:  {reg_name_entry.get()}
            CNIC No : \t {reg_cnic_entry.get()}
            Contact: \t {reg_contact_entry.get()}
            E-mail: \t {reg_email_entry.get()}
            \nCONFIDENTIAL DETAILS
            username:\t {reg_username_entry.get()}
            Password: {reg_password_entry.get()}

        ''')
                    f.close()
                except:
                    pass
            with open("ryoco_credentials.txt", 'a') as j:
                j.write(f"{reg_username_entry.get()}:{reg_password_entry.get()}\n")
                j.close()

    def login():
        with open("ryoco_credentials.txt", 'r') as f:
            e = f.read().splitlines()
            f.close()
        usernames = []
        passwords = []
        for items in e:
            e1 = items.split(":")[0]
            e2 = items.split(":")[1]

            usernames.insert(1, e1)
            passwords.insert(1, e2)

        if username_entry.get() not in usernames:
            tmsg.showerror("ERROR", "INVALID USERNAME", parent=root2)

        elif password_entry.get() not in passwords:
            tmsg.showerror("ERROR", "INVALID PASSWORD", parent=root2)

        else:
            global render1
            c = tmsg.showinfo("LOGIN SUCCESSFUL", "LOGIN SUCCESSFUL",parent=root2)

            root3 = Toplevel()
            # root3.wm_iconbitmap("Artboard 1.ico")
            root3.geometry("1202x802")
            root3.minsize(1202, 802)
            root3.maxsize(1202, 802)
            root3.title("RYOCO BOOKING")


            def logout():
                root3.destroy()
                login_window()



            def LOCAL():
                tmsg.showinfo('DETAILS', '''
                    \nTOUR-I:\tKumrat Valley (3-Days)
                    \t\t\tvia-Jahaz Band, Katora Lake
                    \nTOUR-II:\tFairy Meadows (4-Days)
                    \t\t\tvia-Naran, Hunza
                    \nTOUR-III:\tHunza (5-Days)
                    \t\t\tvia-Swat, Khunjerab''', parent=root3)

            def INTERNATIONAL():
                tmsg.showinfo('DETAILS', ''' 
                TOUR-I:                                                     (14-DAYS)
                Russia, Turkey, Dubai (290,000 PKR Per Person)

                TOUR-II:                                                     (5-DAYS)
                    Mauritius Tour Package (225,000 PKR Per Person)

                TOUR-III:                                                   (05-Days) 
                    TURKEY (45,000 PKR Per Person)''', parent=root3)
            def dr3():
                root3.destroy()

            root2.destroy()

            load1 = Image.open("booking1.png")
            render1 = ImageTk.PhotoImage(load1)
            jpg1 = Label(root3, image=render1)
            jpg1.place(x=0, y=0)

            # def statusr2():
            #     x = 0
            #     for i in range(101):
            #         statusvar.set(f"LOADING {x}%")
            #         statusbar.update()
            #         time.sleep(0.000001)
            #         x += 1
            #     statusvar.set("READY TO USE")
            #     statusbar.update()
            #     time.sleep(0.5)
            #     statusvar.set(f"\t\t{date_of_booking}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tＲＹＯＣＯ ＴＯＵＲＳ© 2021")

            def BOOK():
                global listbox, login_window

                # ============================================ MAILING ===========================================================
                with open(f'{reg_username_entry}_trip.txt', "a") as b:
                    try:
                        b.write(f'''
                    
                    CLIENT:                 {reg_name_entry.get()}
                    CNIC:                   {reg_cnic_entry.get()}
                    USERNAME:               {reg_username_entry.get()}
                    PASSWORD:               {reg_password_entry.get()}
                    TOUR:                   {tour.get()}
                    TYPE:                   {type.get()}
                    DEPARTURE:              {departure.get()}
                    Time:                   {time_of_booking}, {date_of_booking}''')
                    except:
                        b.write(f'''
                        
                        TOUR:                   {tour.get()}
                        TYPE:                   {type.get()}
                        DEPARTURE:              {departure.get()}
                        Time:                   {time_of_booking}, {date_of_booking}''')
                    b.close()
                with open(f'Ryoco_records.txt', "w") as e:
                    try:
                        e.write(f'''
                Dear MR/MRS.{reg_name_entry.get()}, CNIC NO. {reg_cnic_entry.get()}
                    Your username is "{reg_username_entry.get()}" and password is "{reg_password_entry.get()}"
                    Contact: {reg_contact_entry.get()}


                    ---- Trip Details:
                    TOUR:                   {tour.get()}
                    TYPE:                   {type.get()}
                    DEPARTURE:              {departure.get()}
                    Time:                   {time_of_booking}, {date_of_booking}

                    YOUR TOUR HAS BEEN BOOKED, OUR ADMINISTRATION WILL CONTACT YOU SHORTLY.
                    THANK YOU FOR TRUSTING US! :)




                Regards,
                RYOCO Tours(PVT), Limited.

                    ''')
                    except:
                        print(username_entry.get())
                        e.write(f'''
                    Dear MR/MRS.{username_entry.get()}
                        Your username is "{username_entry.get()}" and password is "{password_entry.get()}"



                        ---- Trip Details:
                        TOUR:                   {tour.get()}
                        TYPE:                   {type.get()}
                        DEPARTURE:              {departure.get()}
                        Time:                   {time_of_booking}, {date_of_booking}

                        YOUR TOUR HAS BEEN BOOKED, OUR ADMINISTRATION WILL CONTACT YOU SHORTLY.
                        THANK YOU FOR TRUSTING US! :)




                    Regards,
                    RYOCO Tours(PVT), Limited.

                                            ''')
                e.close()
                if mail.get() == True:
                    print('EMAIL SELECTED')
                    with open('mailingaddress.txt', 'w') as t:
                        t.write(f'{reg_email_entry.get()}')
                        t.close()

                    x = open('mailingaddress.txt', 'r')
                    mailing = x.read()
                    x.close()

                    p = open('Ryoco_records.txt', 'r')
                    contents = p.read()
                    p.close()
                    try:
                        mailfrom = 'ryocotour@gmail.com'
                        mailto = mailing
                        subject = 'RYOCO: BOOKING DETIALS'
                        message = contents
                        msg = 'Subject: {}\n\n{}'.format(subject, message)

                        username = config.EMAIL_ADDRESS
                        password = config.PASSWORD

                        server = s.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login(username, password)
                        server.sendmail(mailfrom, mailto, msg)
                        server.quit()

                        print("Successfully mailed")

                    except:
                        print('Failed to mail details')
                else:
                    print('EMAIL NOT SELECTED')
                listbox = Text(root3, height=2, width=15, bg='#6F4624', fg="white", font=("Montserrat", 18))
                listbox.place(x=700, y=600)

                listbox.delete("1.0", END)

                if departure.get() == 'ISLAMABAD' and tour.get() == 'TOUR-I' and type.get() == 'local':
                    TotalCost1 = int('11499')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-I' and type.get() == 'local':
                    TotalCost1 = int('14999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-I' and type.get() == 'local':
                    TotalCost1 = int('19999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                    # =======================================TOUR-II=============================================================

                elif departure.get() == 'ISLAMABAD' and tour.get() == 'TOUR-II' and type.get() == 'local':
                    TotalCost1 = int('14999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-II' and type.get() == 'local':
                    TotalCost1 = int('15499')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-II' and type.get() == 'local':
                    TotalCost1 = int('21999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                    # ========================================= TOUR-III =======================================================

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-III' and type.get() == 'local':
                    TotalCost1 = int('19499')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-III' and type.get() == 'local':
                    TotalCost1 = int('19999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-III' and type.get() == 'local':
                    TotalCost1 = int('24999')
                    if class1.get() == 'business':
                        TotalCost1 += 5000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                    # =========================================== INTERNATIONAL ==============================================

                    # ==========================================TOUR-I========================================================


                elif departure.get() == 'ISLAMABAD' and tour.get() == 'TOUR-I' and type.get() == 'international':
                    TotalCost1 = int('299999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-I' and type.get() == 'international':
                    TotalCost1 = int('294999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-I' and type.get() == 'international':
                    TotalCost1 = int('289999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                    # ==========================================TOUR-II========================================================


                elif departure.get() == 'ISLAMABAD' and tour.get() == 'TOUR-II' and type.get() == 'international':
                    TotalCost1 = int('234999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-II' and type.get() == 'international':
                    TotalCost1 = int('229999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-II' and type.get() == 'international':
                    TotalCost1 = int('224999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                    # ==========================================TOUR-III========================================================


                elif departure.get() == 'ISLAMABAD' and tour.get() == 'TOUR-III' and type.get() == 'international':
                    TotalCost1 = int('54999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'LAHORE' and tour.get() == 'TOUR-III' and type.get() == 'international':
                    TotalCost1 = int('49999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')

                elif departure.get() == 'KARACHI' and tour.get() == 'TOUR-III' and type.get() == 'international':
                    TotalCost1 = int('44999')
                    if class1.get() == 'business':
                        TotalCost1 += 50000
                    Tax = int((TotalCost1 / 100) * 5)
                    SubTotal1 = int(Tax + TotalCost1)
                    print(f"Cost for trip: Rs{TotalCost1}(tax exclusive)")
                    print(f'Total Cost:    Rs{SubTotal1}')
                    listbox.insert(END, f'Rs.{TotalCost1}/-\n+{Tax}/-(tax)')




            local_button = Radiobutton(root3, text="LOCAL", font=("Montserrat Black", 18, "italic"), variable=type,
                                       value="local", bg="#FFAA00", fg="#623D28")
            local_button.place(x=30, y=580)
            international_button = Radiobutton(root3, text="INTERNATIONAL", font=("Montserrat Black", 18, "italic"),
                                               variable=type, value="international", bg="#FFAA00", fg="#623D28")
            international_button.place(x=165, y=580)

            type_entry = ttk.Combobox(root3, width=50, textvariable=tour)
            type_entry['value'] = ('TOUR-I', 'TOUR-II', 'TOUR-III')
            type_entry.place(x=65, y=630)

            departure_entry = ttk.Combobox(root3, width=30, textvariable=departure)
            departure_entry['value'] = ('ISLAMABAD', 'LAHORE', 'KARACHI')
            departure_entry.place(x=186, y=665)

            economy_button = Radiobutton(root3, text="ECONOMY", font=("Montserrat Black", 18, "italic"), variable=class1,
                                         value="economy", bg="#FFAA00", fg="#623D28")
            economy_button.place(x=435, y=602)

            business_button = Radiobutton(root3, text="BUSINESS", font=("Montserrat Black", 18, "italic"),
                                          variable=class1,
                                          value="business", bg="#FFAA00", fg="#623D28")
            business_button.place(x=435, y=650)


            book_button = Button(root3, text="BOOK RIDE", relief=FLAT, bg="#FCD34B", fg="#7F7F7F",
                                 font=("TrashHand", 40),
                                 command=BOOK)
            book_button.place(x=985, y=490)

            listbox = Text(root3, height=2, width=15, bg='#6F4624', fg="white", font=("Montserrat", 18))
            listbox.place(x=700, y=600)

            # listbox8.insert(END, time_of_booking)

            local_button = Button(root3, text="LOCAL  ", width=35, relief=FLAT, bg="#EA7415", fg="#6F4624",
                                  font=("Bahnschrift Light", 25), command=LOCAL)
            local_button.place(x=15, y=724)

            international_button = Button(root3, text="INTERNATIONAL", width=33, relief=FLAT, bg="#EA7415", fg="#6F4624",
                                          font=("Bahnschrift Light", 25), command=INTERNATIONAL)
            international_button.place(x=585, y=724)

            mailcheck = Checkbutton(root3, text="EMAIL BOOKING INFO", variable=mail, bg="#FFAA00", font=("Consolas", 13))
            mailcheck.place(x=980, y=665)

            logout_button = Button(root3, width=15, text="🔙 LOGOUT ", bg="#EA7415", font=("Montserrat SemiBold", 14),relief=FLAT,command=logout)
            logout_button.place(x=950, y=36)

        # statusvar = StringVar()
        # statusvar.set("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tＲＹＯＣＯ ＴＯＵＲＳ© 2021")
        # statusbar = Label(root3, textvariable=statusvar, bg="#FEEEC6", relief=GROOVE, anchor=W)
        # statusbar.pack(side=BOTTOM, fill=X)
        # statusr2()






    def admin():
        root4 = Toplevel()
        root4.geometry("1202x802")
        root4.minsize(1202, 802)
        root4.maxsize(1202, 802)
        root4.title("ADMIN CONSOLE")
        root2.destroy()

        root4.mainloop()


    # statusvar = StringVar()
    # statusvar.set("READY")
    # statusbar = Label(root2, textvariable=statusvar, bg="#FEEEC6", relief=GROOVE, anchor=W)
    # statusbar.pack(side=BOTTOM, fill=X)


    # ==========================================REGISTERIES========================================

    reg_name_entry = StringVar()
    reg_cnic_entry = StringVar()
    reg_contact_entry = StringVar()
    reg_email_entry = StringVar()
    reg_username_entry = StringVar()
    reg_password_entry = StringVar()
    username_entry = StringVar()
    password_entry = StringVar()
    CNIC = StringVar()
    CNIC.set("0")

    # ================================================LOGIN=================================================================

    username_entryx = Entry(root2, width=23, bg="#F8C43A", textvariable=username_entry, font=("Gill Sans MT", 12))
    username_entryx.place(x=985, y=667)

    password_entryx = Entry(root2, width=23, bg="#F8C43A", textvariable=password_entry, font=("Gill Sans MT", 12), show="*")
    password_entryx.place(x=985, y=720)

    # =============================================REGISERATION=============================================================

    reg_username_entryx = Entry(root2, width=25, bg="#F8C43A", textvariable=reg_username_entry, font=("Gill Sans MT", 12))
    reg_username_entryx.place(x=275, y=669)

    reg_password_entryx = Entry(root2, width=25, bg="#F8C43A", textvariable=reg_password_entry, font=("Gill Sans MT", 12))
    reg_password_entryx.place(x=275, y=723)

    reg_name_entryx = Entry(root2, width=25, bg="#F8C43A", textvariable=reg_name_entry, font=("Gill Sans MT", 12))
    reg_name_entryx.place(x=275, y=408)

    reg_cnic_entryx = Entry(root2, width=36, bg="#F8C43A", textvariable=reg_cnic_entry, font=("Montserrat SemiBold", 12))
    reg_cnic_entryx.place(x=80, y=500)

    reg_contact_entryx = Entry(root2, width=18, bg="#F8C43A", textvariable=reg_contact_entry, font=("Montserrat SemiBold", 12))
    reg_contact_entryx.place(x=275, y=560)

    reg_email_entryx = Entry(root2, width=22, bg="#F8C43A", textvariable = reg_email_entry, font=("Consolas", 12))
    reg_email_entryx.place(x=275, y=615)

    check = Radiobutton(root2, variable=CNIC, bg="#F7BA11", value="cnic")
    check.place(x=75, y=452)

    check1 = Radiobutton(root2, variable=CNIC, bg="#F7C235", value="passport")
    check1.place(x=235, y=452)



    login_button = Button(root2, width=16, text="LOGIN ", bg="#C6633C", font=("Montserrat SemiBold", 12), relief=FLAT,
                          command=login)
    login_button.place(x=880, y=756)

    reg_button = Button(root2, width=16, text="REGISTER ", bg="#C6633C", font=("Montserrat SemiBold", 12), relief=FLAT,
                        command=register)
    reg_button.place(x=164, y=756)

    # admin_button = Button(root2, width=16, text="ADMIN ", bg="#C6633C", font=("Montserrat SemiBold", 12), relief=FLAT,
    #                       command=admin)
    # admin_button.place(x=980, y=40)

    # statusr1()



    # ================================================ BOOKING TAB =========================================================

    mail = IntVar()
    local = StringVar()
    international = StringVar()
    class1 = StringVar()
    type = StringVar()
    tour = StringVar()
    departure = StringVar()
    type.set('0')
    class1.set('0')


    root2.mainloop()
    try:
        dr1()
    except:
        pass

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    #====================================== win-0 =====================================
time_of_booking = (time.strftime("%I:%M:%S %p"))
date_of_booking = (time.strftime("%d/%m/%Y"))

def begin():
    Button(text="BEGIN EXPLORING!", font=("TrashHand 29"), height=2, width=20, bg="#FFBB56", command=login_window, relief=FLAT).place(x=45, y=680)


my_label = Label(root1)
my_label.pack()
thread = threading.Thread(target=stream, args=(my_label,))
thread.daemon = 1
thread.start()
begin()
root1.mainloop()
