from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("BILLZIEE")
        bg_color = "Black"
        title = Label(self.root, text="BILLZIEE", font=('Poppins', 30, 'bold'), pady=2, bd=12, bg="Black", fg="White", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.YardleyGold = IntVar()
        self.Khadilaj = IntVar()
        self.Nivea = IntVar()
        self.Bellavita_luxury = IntVar()
        self.Denver = IntVar()
        self.Zara = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.Besan = IntVar()
        self.Atta = IntVar()
        self.daal = IntVar()
        self.poha = IntVar()
        self.SoyaChunks = IntVar()
        #=============coldDtinks=============================
        self.RedBull = IntVar()
        self.Monster = IntVar()
        self.GluconD = IntVar()
        self.coke = IntVar()
        self.Roohafza = IntVar()
        self.Prime = IntVar()
    # ==============Total product price================
        self.perfume_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.perfume_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('Poppins', 15, 'bold'), bd=10, fg="White", bg="Black")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg='Yellow', font=('Poppins', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='Poppins 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="Yellow", font=('Poppins', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='Poppins 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="Yellow", font=('Poppins', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='Poppins 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", bg="Red", command=self.find_bill, width=10, bd=7, font=('Poppins', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Perfume====================================
        F2 = LabelFrame(self.root, text="Perfume & Deo", font=('Poppins', 15, 'bold'), bd=10, fg="White", bg="Black")
        F2.place(x=5, y=180, width=325, height=380)

        YardleyGold_lbl = Label(F2, text="Yardley Gold", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        YardleyGold_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        YardleyGold_txt = Entry(F2, width=10, textvariable=self.YardleyGold, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        YardleyGold_txt.grid(row=0, column=1, padx=10, pady=10)

        Khadilaj_lbl = Label(F2, text="Khadilaj", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Khadilaj_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Khadilaj_txt = Entry(F2, width=10, textvariable=self.Khadilaj, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Khadilaj_txt.grid(row=1, column=1, padx=10, pady=10)

        Nivea_lbl = Label(F2, text="Nivea", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Nivea_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Nivea_txt = Entry(F2, width=10, textvariable=self.Nivea, font=('Poppins', 16, 'bold'), bd=5, relief =GROOVE)
        Nivea_txt.grid(row=2, column=1, padx=10, pady=10)

        Bellavita_luxury_lbl = Label(F2, text="Bellavita Luxury", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Bellavita_luxury_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Bellavita_luxury_txt = Entry(F2, width=10, textvariable=self.Bellavita_luxury, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Bellavita_luxury_txt.grid(row=3, column=1, padx=10, pady=10)

        Denver_lbl = Label(F2, text="Denver", font =('Poppins', 16, 'bold'), bg = "Black", fg = "White")
        Denver_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Denver_txt = Entry(F2, width=10, textvariable=self.Denver, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Denver_txt.grid(row=4, column=1, padx=10, pady=10)

        Zara_lbl = Label(F2, text="Zara", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Zara_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Zara_txt = Entry(F2, width=10, textvariable=self.Zara, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Zara_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('Poppins', 15, 'bold'), bd=10, fg="White", bg="Black")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        Besan_lbl = Label(F3, text="Besan", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Besan_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Besan_txt = Entry(F3, width=10, textvariable=self.Besan, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Besan_txt.grid(row=1, column=1, padx=10, pady=10)

        Atta_lbl = Label(F3, text="Atta", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Atta_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Atta_txt = Entry(F3, width=10, textvariable=self.Atta, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Atta_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        poha_lbl = Label(F3, text="Poha", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        poha_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        poha_txt = Entry(F3, width=10, textvariable=self.poha, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        poha_txt.grid(row=4, column=1, padx=10, pady=10)

        SoyaChunks_lbl = Label(F3, text="Soya Chunks", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        SoyaChunks_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        SoyaChunks_txt = Entry(F3, width=10, textvariable=self.SoyaChunks, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        SoyaChunks_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('Poppins', 15, 'bold'), bd=10, fg="White", bg="Black")
        F4.place(x=670, y=180, width=325, height=380)

        RedBull_lbl = Label(F4, text="Red Bull", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        RedBull_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        RedBull_txt = Entry(F4, width=10, textvariable=self.RedBull, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        RedBull_txt.grid(row=0, column=1, padx=10, pady=10)

        Monster_lbl = Label(F4, text="Monster", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Monster_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Monster_txt = Entry(F4, width=10, textvariable=self.Monster, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Monster_txt.grid(row=1, column=1, padx=10, pady=10)

        GluconD_lbl = Label(F4, text="Glucon D", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        GluconD_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Atta_txt = Entry(F4, width=10, textvariable=self.GluconD, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Atta_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        Roohafza_lbl = Label(F4, text="Roohafza", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Roohafza_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Roohafza_txt = Entry(F4, width=10, textvariable=self.Roohafza, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Roohafza_txt.grid(row=4, column=1, padx=10, pady=10)

        Prime_lbl = Label(F4, text="Prime", font=('Poppins', 16, 'bold'), bg="Black", fg="White")
        Prime_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Prime_txt = Entry(F4, width=10, textvariable=self.Prime, font=('Poppins', 16, 'bold'), bd=5, relief=GROOVE)
        Prime_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='Poppins', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('Poppins', 14, 'bold'), bd=10, fg="White", bg="Black")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Perfume Price", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.perfume_price, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Perfume Tax", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.perfume_tax, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('Poppins', 14, 'bold'), bg="Black", fg="White")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='Poppins 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="Cyan", bd=2, fg="Black", pady=15, width=12, font='Poppins 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="Cyan", fg="Black", pady=12, width=12, font='Poppins 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="Cyan", bd=2, fg="Black", pady=15, width=12, font='Poppins 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="Cyan", fg="Black", pady=15, width=12, font='Poppins 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):
        self.m_h_g_p = self.Nivea.get()*350
        self.m_s_p = self.YardleyGold.get()*500
        self.m_m_p = self.Khadilaj.get()*1200
        self.m_d_p = self.Bellavita_luxury.get()*440
        self.m_n_p = self.Denver.get()*550
        self.m_t_g_p = self.Zara.get()*999
        self.total_perfume_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.perfume_price.set("Rs. "+str(self.total_perfume_price))
        self.c_tax = round((self.total_perfume_price*0.05), 2)
        self.perfume_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.Besan.get()*10
        self.g_w_p = self.Atta.get()*10
        self.g_d_p = self.daal.get()*6
        self.g_f_p = self.poha.get()*8
        self.g_m_p = self.SoyaChunks.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.RedBull.get()*100
        self.c_d_l_p = self.Monster.get()*120
        self.c_d_m_p = self.GluconD.get()*60
        self.c_d_c_p = self.coke.get()*45
        self.c_d_f_p = self.Roohafza.get()*50
        self.c_m_d = self.Prime.get()*150
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_perfume_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.perfume_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============perfume===========================
        if self.YardleyGold.get() != 0:
            self.txtarea.insert(END, f"\n YardleyGold\t\t{self.YardleyGold.get()}\t\t{self.m_s_p}")
        if self.Khadilaj.get() != 0:
            self.txtarea.insert(END, f"\n YardleyGold\t\t{self.Khadilaj.get()}\t\t{self.m_m_p}")
        if self.Nivea.get() != 0:
            self.txtarea.insert(END, f"\n Nivea\t\t{self.Nivea.get()}\t\t{self.m_h_g_p}")
        if self.Bellavita_luxury.get() != 0:
            self.txtarea.insert(END, f"\n BellavitaLuxury\t\t{self.Bellavita_luxury.get()}\t\t{self.m_d_p}")
        if self.Denver.get() != 0:
            self.txtarea.insert(END, f"\n Denver\t\t{self.Denver.get()}\t\t{self.m_n_p}")
        if self.Zara.get() != 0:
            self.txtarea.insert(END , f"\n Zara\t\t{self.YardleyGold.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.Besan.get() != 0:
            self.txtarea.insert(END, f"\n Besan\t\t{self.Besan.get()}\t\t{self.g_f_o_p}")
        if self.Atta.get() != 0:
            self.txtarea.insert(END, f"\n Atta\t\t{self.Atta.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.poha.get() != 0:
            self.txtarea.insert(END, f"\n Poha\t\t{self.poha.get()}\t\t{self.g_f_p}")
        if self.SoyaChunks.get() != 0:
            self.txtarea.insert(END, f"\n Soya Chunks\t\t{self.SoyaChunks.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.RedBull.get() != 0:
            self.txtarea.insert(END, f"\n RedBull\t\t{self.RedBull.get()}\t\t{self.c_d_s_p}")
        if self.Monster.get() != 0:
            self.txtarea.insert(END, f"\n Monster\t\t{self.Monster.get()}\t\t{self.c_d_l_p}")
        if self.GluconD.get() != 0:
            self.txtarea.insert(END, f"\n GluconD\t\t{self.GluconD.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.Roohafza.get() != 0:
            self.txtarea.insert(END, f"\n Roohafza\t\t{self.Denver.get()}\t\t{self.c_d_f_p}")
        if self.Prime.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.YardleyGold.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.perfume_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Perfume Tax\t\t\t{self.perfume_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.YardleyGold.set(0)
            self.Khadilaj.set(0)
            self.Nivea.set(0)
            self.Bellavita_luxury.set(0)
            self.Denver.set(0)
            self.Zara.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.Besan.set(0)
            self.Atta.set(0)
            self.daal.set(0)
            self.poha.set(0)
            self.SoyaChunks.set(0)
    # =============coldDrinks=============================
            self.RedBull.set(0)
            self.Monster.set(0)
            self.GluconD.set(0)
            self.coke.set(0)
            self.Roohafza.set(0)
            self.Prime.set(0)
    # ====================taxes================================
            self.perfume_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.perfume_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()