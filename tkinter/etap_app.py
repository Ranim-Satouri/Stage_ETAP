import tkinter.font as tkFont
from tkinter import*
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def home_wind():
    home =Tk()
    home.title("Home")
    # full screan tkinter
    width= home.winfo_screenwidth()
    height= home.winfo_screenheight()
    #setting tkinter window size
    home.geometry("%dx%d" % (width, height))
    #wallpaper color
    home.configure(bg='#336699')
    #logo etap------------
    img=Image.open("etap.jpg")
    imag=img.resize((300, 150))
    my_img = ImageTk.PhotoImage(imag)
    my_label=Label(image=my_img)
    my_label.place(x=0,y=0)
    def user_log_in():
        home.destroy()
        root = Tk()
        # full screan tkinter
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        #setting tkinter window size
        root.geometry("%dx%d" % (width, height))
        root.title("user_log_in")
        #wallpaper color
        root.configure(bg='#336699')
        #logo etap------------
        img=Image.open("etap.jpg")
        imag=img.resize((300, 150))
        my_img = ImageTk.PhotoImage(imag)
        my_label=Label(image=my_img)
        my_label.place(x=0,y=0)
        def accueil(id_value):
            try:
                root.destroy()
            except Exception:
                pass   
            acc =Tk()
            acc.title("Accueil")
            # full screan tkinter
            width= acc.winfo_screenwidth()
            height= acc.winfo_screenheight()
            #setting tkinter window size
            acc.geometry("%dx%d" % (width, height))
            #wallpaper color
            acc.configure(bg='#336699')
            #logo etap------------
            img=Image.open("etap.jpg")
            imag=img.resize((300, 150))
            my_img = ImageTk.PhotoImage(imag)
            my_label=Label(image=my_img)
            my_label.place(x=0,y=0)
            

            def facture():
                acc.destroy()
                #acc.destroy()
                fac =Tk()
                fac.title("Ajouter une Facture")
                # full screan tkinter
                width= fac.winfo_screenwidth()
                height= fac.winfo_screenheight()
                #setting tkinter window size
                fac.geometry("%dx%d" % (width, height))
                #wallpaper color
                fac.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                def load_districts():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT district FROM district"
                        cursor.execute(query)
                        districts = cursor.fetchall()
                        # Convert the result to a list of strings
                        district_names = [row[0] for row in districts]
                        return district_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def load_local_items(selected_district):
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        query = "SELECT libellelocal FROM locaux " \
                                "JOIN district ON locaux.codedistrict = district.codedistrict " \
                                "WHERE district = %s"
                        cursor.execute(query, (selected_district,))
                        local_items = cursor.fetchall()
                        # Convert the result to a list of strings
                        local_item_names = [row[0] for row in local_items]
                        return local_item_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def load_compteur_items(selected_local):
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query = "select reference from compteur join locaux where locaux.codelocal=compteur.codelocal and libellelocal=%s";
                        cursor.execute(query, (selected_local,))
                        local_items = cursor.fetchall()
                        # Convert the result to a list of strings
                        local_item_names = [row[0] for row in local_items]
                        return local_item_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                
                def update_local_combobox():
                    selected_district = district_combobox.get()
                    local_item_names = load_local_items(selected_district)
                    local_combobox['values'] = local_item_names
                    if local_item_names:
                        local_combobox.set(local_item_names[0])
                    local_combobox['state']='readonly'
                def update_compteur_combobox():
                    selected_local = local_combobox.get()
                    compteur_item_names = load_compteur_items(selected_local)
                    comp['values'] = compteur_item_names
                    if compteur_item_names:
                        comp.set(compteur_item_names[0])
                    comp['state']='readonly'    

                def controle_month_year(month,year,montant,newindex):
                    if montant>=0 and newindex>=0:
                        if not (month>0 and month<13) and not (year>1999 and year<2100):
                            messagebox.showinfo("Message", "verifier le mois et l'année")
                            E_month.delete(0,END)
                            E_year.delete(0,END)
                            return False
                        if not (month>0 and month<13):
                            messagebox.showinfo("Message", "verifier le mois")
                            E_month.delete(0,END)
                            return False
                        if not (year>1999 and year<2100):
                            messagebox.showinfo("Message", "verifier l'année")
                            E_year.delete(0,END)
                            return False 
                    elif montant<0:
                        messagebox.showinfo("Message", "montant invalid")
                        E_montant.delete(0,END)
                        return False
                    elif newindex <0:
                        messagebox.showinfo("Message", "nouveau indice invalide")
                        E_newindex.delete(0,END)
                        return False

                    return True

                def insert_data():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            q="select numerofacture,month,year,newindex,montant,referencecompteur from facture"
                            cursor.execute(q)
                            list=cursor.fetchall()
                            
                            try:
                                oldindex="select year,month,newindex from facture where facture.numerofacture = %s "
                                cursor.execute(oldindex,(int(E_numfac.get()),))
                                index_list=cursor.fetchall()
                                max_index=max(index_list)
                                old_index=max_index[2]
                            except:
                                old_index=0
                            try:
                                if controle_month_year(int(E_month.get()),int(E_year.get()),float(E_montant.get()),int(E_newindex.get())):
                                    if(E_numfac.get(),int(E_month.get()),int(E_year.get()),int(E_newindex.get()),float(E_montant.get()),int(comp.get())) not in list:
                                        query = "insert into facture(numerofacture,month,year,oldindex,newindex,montant,referencecompteur,userid)"\
                                        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
                                        my_data=(E_numfac.get(),E_month.get(),E_year.get(),old_index,E_newindex.get(),E_montant.get(),comp.get(),id_value)
                                        cursor.execute(query,my_data)
                                        connection.commit()
                                        messagebox.showinfo("Message",  "envoyé avec succés")
                                    else:
                                        messagebox.showinfo("Message",  "Facture existe deja !")    
                            except :
                                messagebox.showinfo("Message", "une erreur est survenue.Veillez réessayer ultérieurement !")
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                font = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                font4 = tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)

                user_label=Label(fac,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                l_district=Label(fac,text="District :",bg='#336699',fg="#660033")
                l_district.place(x=440,y=80)
                l_district.configure(font=font)

                l_local=Label(fac,text="Local :",bg='#336699',fg="#660033")
                l_local.place(x=455,y=150)
                l_local.configure(font=font)

                l_compteur=Label(fac,text="Compteur :",bg='#336699',fg="#660033")
                l_compteur.place(x=410,y=220)
                l_compteur.configure(font=font)

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")

                # Create the district combobox
                district_combobox = ttk.Combobox(fac)
                district_combobox.place(x=550, y=80, width=300, height=35)
                district_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                district_combobox['values'] = load_districts()
                district_combobox.set(district_combobox['values'][0])  # Set the default value
                district_combobox['state']='readonly'
                # Create the local combobox
                local_combobox = ttk.Combobox(fac)
                local_combobox.place(x=550, y=150, width=300, height=35)
                local_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))

                comp=ttk.Combobox()
                comp.place(x=550,y=220,width=300,height=35)
                comp.configure(font=font)

                update_local_button = Button(fac, text="OK", command=update_local_combobox)
                update_local_button.place(x=850, y=81, width=29, height=34)

                update_compteur_button = Button(fac, text="OK", command=update_compteur_combobox)
                update_compteur_button.place(x=850, y=151, width=29, height=34)

                
                l_numfac=Label(fac,text="Numéro De Facture :",bg='#336699',fg="#660033")
                l_numfac.place(x=90,y=350)
                l_numfac.configure(font=font)
                
                E_numfac=Entry(fac,bg="#AFAFC2",font=font4)
                E_numfac.place(x=300,y=350, width=300, height=35)

                l_montant=Label(fac,text="Montant :",bg='#336699',fg="#660033")
                l_montant.place(x=800,y=350)
                l_montant.configure(font=font)
                
                E_montant=Entry(fac,bg="#AFAFC2",font=font4)
                E_montant.place(x=920,y=350, width=300, height=35)

                l_year=Label(fac,text="Année :",bg='#336699',fg="#660033")
                l_year.place(x=810,y=500)
                l_year.configure(font=font)
                
                E_year=Entry(fac,bg="#AFAFC2",font=font4)
                E_year.place(x=920,y=500, width=300, height=35)

                l_month=Label(fac,text="Mois :",bg='#336699',fg="#660033")
                l_month.place(x=230,y=500)
                l_month.configure(font=font)
                
                E_month=Entry(fac,bg="#AFAFC2",font=font4)
                E_month.place(x=300,y=500, width=300, height=35)

                l_index=Label(fac,text="Nouvel Indice :",bg='#336699',fg="#660033")
                l_index.place(x=420,y=430)
                l_index.configure(font=font)
                
                E_newindex=Entry(fac,bg="#AFAFC2",font=font4)
                E_newindex.place(x=600,y=430, width=300, height=35)

                
                b_emv=Button(fac,text="Envoyer",bg='#B04BE3',fg="#000066",bd=5,command =insert_data)
                b_emv.place(x=610,y=650,width=150, height=30)
                b_emv.configure(font=font)

                def exit():
                    fac.destroy()

                b_exit=Button(fac,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font)
                def retour_a_laccueil():
                    fac.destroy()
                    accueil(id_value)
                b_accueil=Button(fac,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)
                fac.mainloop()            
            def afficher_fact_user():
                acc.destroy()
                home=Tk()
                home.title("Consulter Les Factures")
                # full screan tkinter
                width= home.winfo_screenwidth()
                height= home.winfo_screenheight()
                #setting tkinter window size
                home.geometry("%dx%d" % (width, height))
                #wallpaper color
                home.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_table():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        query = '''SELECT 
                                    d.district,
                                    lo.libellelocal,
                                    lo.adresselocal,
                                    f.referencecompteur,
                                    tc.typecompteur,
                                    f.numerofacture,
                                    f.month,
                                    f.year,
                                    f.oldindex,
                                    f.newindex,
                                    f.montant
                                FROM
                                    facture f
                                JOIN
                                    compteur c ON c.reference = f.referencecompteur
                                JOIN
                                    typecompteur tc ON tc.codetype = c.codetypecompteur
                                JOIN
                                    locaux lo ON lo.codelocal = c.codelocal
                                JOIN 
                                    district d ON d.codedistrict=lo.codedistrict  
                                JOIN
                                    user u ON u.userid=f.userid    where u.userid=%s;'''

                        cursor.execute(query,(id_value,))
                        T = cursor.fetchall()
                        return T
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(home,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)               

                # Créer le widget Treeview pour afficher les données
                columns = ("District","Libellé Local", "Adresse Local", "Référence Compteur", "Type Compteur","Numéro Facture", "Mois", "Année", "Ancien Indice", "Nouvel Indice", "Montant" )
                tree = ttk.Treeview(home, columns=columns, show="headings")
                # Configurer les en-têtes de colonne
                for col in columns:
                    tree.heading(col, text=col)
                
                # Charger les données depuis la base de données
                data = load_table()
                
                # Insérer les données dans le Treeview
                for row in data:
                    tree.insert("", "end", values=row)

                tree.column("Numéro Facture", width=120)
                tree.column("Mois", width=100)
                tree.column("Année", width=100)
                tree.column("Ancien Indice", width=100)
                tree.column("Nouvel Indice", width=100)
                tree.column("Montant", width=100)
                tree.column("Adresse Local", width=150)
                tree.column("District", width=150)
                tree.column("Libellé Local", width=150)
                tree.column("Référence Compteur", width=150)
                tree.column("Type Compteur", width=150)

                Style=ttk.Style()
                Style.theme_use("clam")
                Style.configure("Treeview",
                                background="silver",
                                foreground="black",
                                rowheight=25,
                                fieldbackground="#336699")
                Style.map("Treeview",background=[('selected','green')])
                # Afficher le Treeview
                tree.place(x=0,y=150, height=600)
                font = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")

                def retour_a_laccueil():
                    home.destroy()
                    accueil(id_value)
                b_accueil=Button(home,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=80,y=650,width=150, height=30)
                b_accueil.configure(font=font)
                home.mainloop()

            def facture_supression():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                sup =Tk()
                sup.title("Supprimer Une Facture")
                # full screan tkinter
                width= sup.winfo_screenwidth()
                height= sup.winfo_screenheight()
                #setting tkinter window size
                sup.geometry("%dx%d" % (width, height))
                #wallpaper color
                sup.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_facture():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT numerofacture,month,year FROM facture where userid=%s"
                        cursor.execute(query,(id_value,))
                        f = cursor.fetchall()
                        # Convert the result to a list of strings
                        facture = [f"Reference = {row[0]} , Mois = {row[1]} , Année = {row[2]}" for row in f]
                        return facture
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def delete_facture():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        facture=load_facture()
                        try:
                            msg_box=messagebox.askquestion('Supprimer',"êtes-vous sûr de supprimer la facture ?",icon='warning')
                            if msg_box == 'yes':
                                query = "delete from facture where numerofacture = %s and month=%s and year=%s"
                                cursor.execute(query,(fact_combobox.get().split()[2],fact_combobox.get().split()[6],fact_combobox.get().split()[10]))
                                connection.commit()
                                messagebox.showinfo('Done', 'Supprimer Avec succés')
                                sup.destroy()
                                facture_supression()                    
                        except Exception:
                            pass

                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()            

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                fact_combobox = ttk.Combobox(sup)
                fact_combobox.place(x=30, y=300, width=1300, height=50)
                fact_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                fact_combobox['values'] = load_facture()
                try:
                    fact_combobox.set(fact_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                fact_combobox['state']='readonly'
                font=tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                
                delete_button=Button(sup,text="Supprimer",bg='#B04BE3',fg="#000066",bd=5,command =delete_facture)
                delete_button.place(x=610,y=650,width=150, height=30)
                delete_button.configure(font=font)
                def exit():
                    sup.destroy()
                exit_button=Button(sup,text="Exit",bg='#B04BE3',fg="#000066",bd=5,command =exit)
                exit_button.place(x=1150,y=650,width=150, height=30)
                exit_button.configure(font=font)

                def retour_a_laccueil():
                    sup.destroy()
                    accueil(id_value)
                b_accueil=Button(sup,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font)

                #user_name_au_fond_de_la_page
                font2 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(sup,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font2)

                sup.mainloop()

            def update_facture():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                upd =Tk()
                upd.title("Modifier une Facture")
                # full screan tkinter
                width= upd.winfo_screenwidth()
                height= upd.winfo_screenheight()
                #setting tkinter window size
                upd.geometry("%dx%d" % (width, height))
                #wallpaper color
                upd.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                def load_factures():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT key_facture,numerofacture,month,year,newindex,montant FROM facture where userid=%s"
                        cursor.execute(query,(id_value,))
                        f = cursor.fetchall()
                        # Convert the result to a list of strings
                        facture=[f"{row[0]} ) Reference = {row[1]} , Mois = {row[2]} , Année = {row[3]}  , Nouveau Indice = {row[4]} , Montant = {row[5]}" for row in f]
                        return facture
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                def afficher_fac():
                    try:
                        global key
                        global id
                        key=fact_combobox.get().split()[0]    
                        id=fact_combobox.get().split()[4]
                    except:
                        return
                    try:
                        upd.destroy()
                    except Exception:
                        pass    
                    up =Tk()
                    up.title("Modifier Une Facture")
                    # full screan tkinter
                    width= up.winfo_screenwidth()
                    height= up.winfo_screenheight()
                    #setting tkinter window size
                    up.geometry("%dx%d" % (width, height))
                    #wallpaper color
                    up.configure(bg='#336699')
                    #logo etap------------
                    img=Image.open("etap.jpg")
                    imag=img.resize((300, 150))
                    my_img = ImageTk.PhotoImage(imag)
                    my_label=Label(image=my_img)
                    my_label.place(x=0,y=0)

                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        query = "SELECT month,year,newindex,montant from facture where key_facture=%s"
                        cursor.execute(query,(int(key),))
                        info = cursor.fetchall()
                        # Convert the result to a list of strings
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                    def update():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            try:
                                m=int(E_month.get())
                                y=int(E_year.get())
                                nx=int(E_new_index.get())
                                mo=float(E_montant.get())
                                if(m>0 and m<13 and y<2100 and y>2000):
                                    q="select  MIN(key_facture) from facture where key_facture > %s and numerofacture = %s"
                                    cursor.execute(q,(int(key),id))
                                    a=cursor.fetchall()
                                 
                                    msg_box=messagebox.askquestion('Supprimer',"êtes-vous sûr de Modifier la facture ?",icon='warning')
                                    if msg_box == 'yes':
                                        query = """update facture SET 
                                                    month=%s,
                                                    year=%s,
                                                    newindex=%s,
                                                    montant=%s
                                                    where key_facture=%s"""
                                        cursor.execute(query,(m,y,nx,mo,key))
                                
                                        query2 = """update facture SET 
                                                    oldindex=%s
                                                    where key_facture=%s"""
                                        cursor.execute(query2,(nx,a[0][0]))
                                        connection.commit()
                                        messagebox.showinfo("Message", "Modifier Avec Succée")             
                                else:
                                    messagebox.showinfo("Message", "ERREUR: Verifier le mois et l'année")
                            except :
                                messagebox.showinfo("Message", "ERREUR , Verifier les champs")
                                
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()


                    font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                    l_month=Label(up,text="Mois:",bg='#336699',fg="#130D41")
                    l_month.place(x=350,y=130,width=300,height=30)
                    l_month.configure(font=font4)

                    E_month=Entry(up,bg="#ccffff",font=font4)
                    E_month.place(x=600,y=120,width=500,height=50)

                    l_year=Label(up,text="Année:",bg='#336699',fg="#130D41")
                    l_year.place(x=340,y=230,width=300,height=30)
                    l_year.configure(font=font4)

                    E_year=Entry(up,bg="#ccffff",font=font4)
                    E_year.place(x=600,y=220,width=500,height=50)

                    l_new_index=Label(up,text="Nouvel Indice:",bg='#336699',fg="#130D41")
                    l_new_index.place(x=300,y=330,width=300,height=30)
                    l_new_index.configure(font=font4)

                    E_new_index=Entry(up,bg="#ccffff",font=font4)
                    E_new_index.place(x=600,y=320,width=500,height=50)


                    l_montant=Label(up,text="Montant:",bg='#336699',fg="#130D41")
                    l_montant.place(x=290,y=430,width=300,height=30)
                    l_montant.configure(font=font4)

                    E_montant=Entry(up,bg="#ccffff",font=font4)
                    E_montant.place(x=600,y=420,width=500,height=50)

                    button=Button(up,text="Modifier",bg='#B04BE3',fg="#000066",bd=5,command =update)
                    button.place(x=610,y=650,width=150, height=30)
                    button.configure(font=font4)
                    

                    E_month.insert(0,info[0][0])
                    E_year.insert(0,info[0][1])
                    E_new_index.insert(0,info[0][2])
                    E_montant.insert(0,info[0][3])

                    def exit():
                        up.destroy()
                    b_exit=Button(up,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                    b_exit.place(x=1150,y=650,width=150, height=30)
                    b_exit.configure(font=font4)

                    def retour_a_laccueil():
                        up.destroy()
                        update_facture()
                    b_accueil=Button(up,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                    b_accueil.place(x=65,y=650,width=150, height=30)
                    b_accueil.configure(font=font4)

                    font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                    get_user_name(id_value)
                    user_label=Label(up,text=user_name,fg="black",bg='#336699')
                    user_label.place(x=1200,y=20)
                    user_label.configure(font=font3)

                    up.mainloop()
                
                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
                
                msg_label=Label(upd, text="Choisissez La Facture A Modifier ",bg='#336699',fg="#130D41")
                msg_label.place(x=500,y=200)
                msg_label.configure(font=font4)
                
                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                fact_combobox = ttk.Combobox(upd)
                fact_combobox.place(x=30, y=350, width=1300, height=50)
                fact_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                fact_combobox['values'] = load_factures()
                try:
                    fact_combobox.set(fact_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                fact_combobox['state']='readonly'
                open_button=Button(upd,text="Modifier",bg='#B04BE3',fg="#000066",bd=5,command =afficher_fac)
                open_button.place(x=610,y=650,width=150, height=30)
                open_button.configure(font=font4)

                def exit():
                    upd.destroy()
                b_exit=Button(upd,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)

                def retour_a_laccueil():
                    upd.destroy()
                    accueil(id_value)
                b_accueil=Button(upd,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)

                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                get_user_name(id_value)
                user_label=Label(upd,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)
                upd.mainloop()
  
            font=tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")

            var = IntVar()
            R1 = Radiobutton(acc, text="Consulter les factures ajoutées", bg="#CBA1C5", variable=var, value=1,
                            command=afficher_fact_user )
            R1.place( anchor = W ,x=80,y=200 ,width=300,height=35 )

            R2 = Radiobutton(acc, text="Supprimer Une Facture", bg="#CBA1C5", variable=var, value=2,
                            command=facture_supression)
            R2.place( anchor = W ,x=530,y=200,width=300,height=35)

            R3 = Radiobutton(acc, text="Modifier une facture", bg="#CBA1C5", variable=var, value=3,
                        command=update_facture)
            R3.place( anchor = W,x=80,y=300,width=300,height=35)

            R4 = Radiobutton(acc, text="Ajouter Une Facture", bg="#CBA1C5", variable=var, value=1,
                        command=facture )
            R4.place( anchor = W ,x=980,y=200 ,width=300,height=35)

            '''R5 = Radiobutton(acc, text="Ajouter Un Utilisateur", bg="#CBA1C5", variable=var, value=2,
                            )
            R5.place( anchor = W ,x=600,y=300,width=300,height=35)'''

            """R6 = Radiobutton(dis, text="ajouter un compteur", variable=var, value=3,
                        )
            R6.place( anchor = W,x=200,y=400,width=300,height=35)"""
            #get user name 
            def get_user_name(id_value):
                try:
                    # Establish a connection to the MySQL server
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='112713',
                        database='etapproject'
                    )
                    
                    # Create a cursor
                    c = connection.cursor()
                    # Construct the INSERT query
                    q = "select nom,prenom from user where userid=%s"
                    # Execute the query
                    c.execute(q,(id_value,))
                    r=c.fetchall() 
                    global user_name
                    user_name=r[0][0] +' '+ r[0][1]
                       
                    # Commit the changes to the database
                    connection.commit()

                except mysql.connector.Error as error:
                    print("Error:", error)

                finally:
                    # Close the cursor and connection
                    if c:
                        c.close()
                    if connection:
                        connection.close()
            font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
            get_user_name(id_value)
            user_label=Label(acc,text=user_name,fg="black",bg='#336699')
            user_label.place(x=1200,y=20)
            user_label.configure(font=font3)

            def retour_a_laccueil():
                acc.destroy()
                home_wind()
            b_accueil=Button(acc,text='Déconnecter',bg='#336699',fg="#000066",bd=5,command=retour_a_laccueil)
            b_accueil.place(x=1150,y=650,width=150, height=30)
            b_accueil.configure(font=font)
            home.mainloop()


            acc.mainloop()

        def log_in():
            try:
                # Establish a connection to the MySQL server
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='112713',
                    database='etapproject'
                )
                id_value = E_id.get()
                password = E_pass.get()
                # Create a cursor
                c = connection.cursor()
                q = f"SELECT userid,password from user"
                # Execute the query
                c.execute(q)
                r=c.fetchall() 
                font2 = tkFont.Font(family="Times New Roman", size=8, weight="bold", slant="italic")
                try:
                    if (int(id_value),password) not in r or (int(id_value),password) == (159,"ranim0000") :
                        E_id.delete(0,END)
                        E_pass.delete(0,END)
                        messagebox.showinfo("Message", "Le mot de passe ou l'ID entré est incorrect \n Vous pouvez essayer une autre foix!")
                    else:    
                        accueil(id_value)
                except Exception:
                    pass
                    

                connection.commit()
            except mysql.connector.Error as error:
                print("Error:", error)
            finally:
                # Close the cursor and connection
                if c:
                    c.close()
                if connection:
                    connection.close()
        
        #create labels
        l_id=Label(root,text="Id de L'Employé   :",bg='#336699',fg="#660033")
        E_id=Entry(root,bg='#9C9398',font=font2)
        l_pass=Label(root,text="Mot de passe  :",bg='#336699',fg="#660033")
        E_pass=Entry(root,bg='#9C9398',font=font2,show="*")

        #police ecriture
        font = tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
        l_id.configure(font=font)
        l_pass.configure(font=font)
        l_id.place(x=450,y=250)
        E_id.place(x=650,y=250,width=200, height=30)
        l_pass.place(x=450,y=350)
        E_pass.place(x=650,y=350,width=200, height=30)

        b_login=Button(root,text='Se Connecter',bg='#B04BE3',fg="#000066",bd=5,command=log_in)
        b_login.place(x=610,y=650,width=150, height=30)
        b_login.configure(font=font)

        def exit():
            root.destroy()

        b_exit=Button(root,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
        b_exit.place(x=1150,y=650,width=150, height=30)
        b_exit.configure(font=font)

        font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
        def retour_a_laccueil():
            root.destroy()
            home_wind()
        b_accueil=Button(root,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
        b_accueil.place(x=65,y=650,width=150, height=30)
        b_accueil.configure(font=font4)

        root.mainloop()

    def admin_log_in():
        home.destroy()
        root = Tk()
        # full screan tkinter
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        #setting tkinter window size
        root.geometry("%dx%d" % (width, height))
        root.title("Admin_Log_In")
        #wallpaper color
        root.configure(bg='#336699')
        #logo etap------------
        img=Image.open("etap.jpg")
        imag=img.resize((300, 150))
        my_img = ImageTk.PhotoImage(imag)
        my_label=Label(image=my_img)
        my_label.place(x=0,y=0)
        def accueil(id_value):
            try:
                root.destroy()
            except Exception:
                pass    
            acc =Tk()
            acc.title("Accueil")
            # full screan tkinter
            width= acc.winfo_screenwidth()
            height= acc.winfo_screenheight()
            #setting tkinter window size
            acc.geometry("%dx%d" % (width, height))
            #wallpaper color
            acc.configure(bg='#336699')
            #logo etap------------
            img=Image.open("etap.jpg")
            imag=img.resize((300, 150))
            my_img = ImageTk.PhotoImage(imag)
            my_label=Label(image=my_img)
            my_label.place(x=0,y=0)
            
            def facture():
                acc.destroy()
                #acc.destroy()
                fac =Tk()
                fac.title("Ajouter une Facture")
                # full screan tkinter
                width= fac.winfo_screenwidth()
                height= fac.winfo_screenheight()
                #setting tkinter window size
                fac.geometry("%dx%d" % (width, height))
                #wallpaper color
                fac.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                def load_districts():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT district FROM district"
                        cursor.execute(query)
                        districts = cursor.fetchall()
                        # Convert the result to a list of strings
                        district_names = [row[0] for row in districts]
                        return district_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def load_local_items(selected_district):
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        query = "SELECT libellelocal FROM locaux " \
                                "JOIN district ON locaux.codedistrict = district.codedistrict " \
                                "WHERE district = %s"
                        cursor.execute(query, (selected_district,))
                        local_items = cursor.fetchall()
                        # Convert the result to a list of strings
                        local_item_names = [row[0] for row in local_items]
                        return local_item_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def load_compteur_items(selected_local):
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query = "select reference from compteur join locaux where locaux.codelocal=compteur.codelocal and libellelocal=%s";
                        cursor.execute(query, (selected_local,))
                        local_items = cursor.fetchall()
                        # Convert the result to a list of strings
                        local_item_names = [row[0] for row in local_items]
                        return local_item_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                
                def update_local_combobox():
                    selected_district = district_combobox.get()
                    local_item_names = load_local_items(selected_district)
                    local_combobox['values'] = local_item_names
                    if local_item_names:
                        local_combobox.set(local_item_names[0])
                    local_combobox['state']='readonly'
                def update_compteur_combobox():
                    selected_local = local_combobox.get()
                    compteur_item_names = load_compteur_items(selected_local)
                    comp['values'] = compteur_item_names
                    if compteur_item_names:
                        comp.set(compteur_item_names[0])
                    comp['state']='readonly'    

                def controle_month_year(month,year,montant,newindex):
                    if montant>=0 and newindex>=0:
                        if not (month>0 and month<13) and not (year>1999 and year<2100):
                            messagebox.showinfo("Message", "verifier le mois et l'année")
                            E_month.delete(0,END)
                            E_year.delete(0,END)
                            return False
                        if not (month>0 and month<13):
                            messagebox.showinfo("Message", "verifier le mois")
                            E_month.delete(0,END)
                            return False
                        if not (year>1999 and year<2100):
                            messagebox.showinfo("Message", "verifier l'année")
                            E_year.delete(0,END)
                            return False 
                    elif montant<0:
                        messagebox.showinfo("Message", "montant invalid")
                        E_montant.delete(0,END)
                        return False
                    elif newindex <0:
                        messagebox.showinfo("Message", "nouveau indice invalide")
                        E_newindex.delete(0,END)
                        return False

                    return True

                def insert_data():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            q="select numerofacture,month,year,newindex,montant,referencecompteur from facture"
                            cursor.execute(q)
                            list=cursor.fetchall()
                            
                            try:
                                oldindex="select year,month,newindex from facture where facture.numerofacture = %s "
                                cursor.execute(oldindex,(int(E_numfac.get()),))
                                index_list=cursor.fetchall()
                                max_index=max(index_list)
                                old_index=max_index[2]
                            except:
                                old_index=0
                            try:
                                if controle_month_year(int(E_month.get()),int(E_year.get()),float(E_montant.get()),int(E_newindex.get())):
                                    if(E_numfac.get(),int(E_month.get()),int(E_year.get()),int(E_newindex.get()),float(E_montant.get()),int(comp.get())) not in list:
                                        query = "insert into facture(numerofacture,month,year,oldindex,newindex,montant,referencecompteur,userid)"\
                                        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
                                        my_data=(E_numfac.get(),E_month.get(),E_year.get(),old_index,E_newindex.get(),E_montant.get(),comp.get(),id_value)
                                        cursor.execute(query,my_data)
                                        connection.commit()
                                        messagebox.showinfo("Message",  "envoyé avec succés")
                                    else:
                                        messagebox.showinfo("Message",  "Facture existe deja !")    
                            except :
                                messagebox.showinfo("Message", "une erreur est survenue.Veillez réessayer ultérieurement !")
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                font = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                font4 = tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)

                user_label=Label(fac,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                l_district=Label(fac,text="District :",bg='#336699',fg="#660033")
                l_district.place(x=440,y=80)
                l_district.configure(font=font)

                l_local=Label(fac,text="Local :",bg='#336699',fg="#660033")
                l_local.place(x=455,y=150)
                l_local.configure(font=font)

                l_compteur=Label(fac,text="Compteur :",bg='#336699',fg="#660033")
                l_compteur.place(x=410,y=220)
                l_compteur.configure(font=font)

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")

                # Create the district combobox
                district_combobox = ttk.Combobox(fac)
                district_combobox.place(x=550, y=80, width=300, height=35)
                district_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                district_combobox['values'] = load_districts()
                district_combobox.set(district_combobox['values'][0])  # Set the default value
                district_combobox['state']='readonly'
                # Create the local combobox
                local_combobox = ttk.Combobox(fac)
                local_combobox.place(x=550, y=150, width=300, height=35)
                local_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))

                comp=ttk.Combobox()
                comp.place(x=550,y=220,width=300,height=35)
                comp.configure(font=font)

                update_local_button = Button(fac, text="OK", command=update_local_combobox)
                update_local_button.place(x=850, y=81, width=29, height=34)

                update_compteur_button = Button(fac, text="OK", command=update_compteur_combobox)
                update_compteur_button.place(x=850, y=151, width=29, height=34)

                
                l_numfac=Label(fac,text="Numéro De Facture :",bg='#336699',fg="#660033")
                l_numfac.place(x=90,y=350)
                l_numfac.configure(font=font)
                
                E_numfac=Entry(fac,bg="#AFAFC2",font=font4)
                E_numfac.place(x=300,y=350, width=300, height=35)

                l_montant=Label(fac,text="Montant :",bg='#336699',fg="#660033")
                l_montant.place(x=800,y=350)
                l_montant.configure(font=font)
                
                E_montant=Entry(fac,bg="#AFAFC2",font=font4)
                E_montant.place(x=920,y=350, width=300, height=35)

                l_year=Label(fac,text="Année :",bg='#336699',fg="#660033")
                l_year.place(x=810,y=500)
                l_year.configure(font=font)
                
                E_year=Entry(fac,bg="#AFAFC2",font=font4)
                E_year.place(x=920,y=500, width=300, height=35)

                l_month=Label(fac,text="Mois :",bg='#336699',fg="#660033")
                l_month.place(x=230,y=500)
                l_month.configure(font=font)
                
                E_month=Entry(fac,bg="#AFAFC2",font=font4)
                E_month.place(x=300,y=500, width=300, height=35)

                l_index=Label(fac,text="Nouvel Indice :",bg='#336699',fg="#660033")
                l_index.place(x=420,y=430)
                l_index.configure(font=font)
                
                E_newindex=Entry(fac,bg="#AFAFC2",font=font4)
                E_newindex.place(x=600,y=430, width=300, height=35)

                
                b_emv=Button(fac,text="Envoyer",bg='#B04BE3',fg="#000066",bd=5,command =insert_data)
                b_emv.place(x=610,y=650,width=150, height=30)
                b_emv.configure(font=font)

                def exit():
                    fac.destroy()

                b_exit=Button(fac,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font)
                def retour_a_laccueil():
                    fac.destroy()
                    accueil(id_value)
                b_accueil=Button(fac,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)
                fac.mainloop()            
        
            def afficher_fact_admin():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                home=Tk()
                home.title("Consulter Les Factures")
                # full screan tkinter
                width= home.winfo_screenwidth()
                height= home.winfo_screenheight()
                #setting tkinter window size
                home.geometry("%dx%d" % (width, height))
                #wallpaper color
                home.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_factures():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        q1="select distinct numerofacture from facture"
                        cursor.execute(q1)
                        list_of_facture = cursor.fetchall()
                        return list_of_facture
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                def delete_row():
                    for item in tree.get_children():
                        tree.delete(item)      
                def load_table():
                    delete_row()
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query = '''SELECT 
                                    d.district,
                                    lo.libellelocal,
                                    lo.adresselocal,
                                    f.referencecompteur,
                                    tc.typecompteur,
                                    f.numerofacture,
                                    f.month,
                                    f.year,
                                    f.oldindex,
                                    f.newindex,
                                    f.montant,
                                    u.nom,
                                    u.prenom
                                FROM
                                    facture f
                                JOIN
                                    compteur c ON c.reference = f.referencecompteur
                                JOIN
                                    typecompteur tc ON tc.codetype = c.codetypecompteur
                                JOIN
                                    locaux lo ON lo.codelocal = c.codelocal
                                JOIN 
                                    district d ON d.codedistrict=lo.codedistrict
                                JOIN
                                    user u ON u.userid=f.userid where numerofacture=%s ;'''

                        cursor.execute(query,(fact_combobox.get(),))
                        T = cursor.fetchall()
                    
                        for row in T:
                            tree.insert("", "end", values=row)
                        return T
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()            
                
                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                fact_combobox = ttk.Combobox(home)
                fact_combobox.place(x=1255, y=100, width=100, height=50)
                fact_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                fact_combobox['values'] = load_factures()
                try:
                    fact_combobox.set(fact_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                fact_combobox['state']='readonly'
                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
                b_aff=Button(home,text='Afficher',command=load_table,bg='#B04BE3',fg="#000066",bd=5)
                b_aff.place(x=1155,y=100,width=95,height=50)
                b_aff.configure(font=font4)
                # Créer le widget Treeview pour afficher les données
                columns = ("District","Libellé Local", "Adresse Local", "Référence Compteur", "Type Compteur","Numéro Facture", "Mois", "Année", "Ancien Indice", "Nouvel Indice", "Montant","nom","prenom" )
                tree = ttk.Treeview(home, columns=columns, show="headings")
                # Configurer les en-têtes de colonne
                for col in columns:
                    tree.heading(col, text=col)
                
                tree.column("Numéro Facture", width=120)
                tree.column("Mois", width=50)
                tree.column("Année", width=50)
                tree.column("Ancien Indice", width=100)
                tree.column("Nouvel Indice", width=100)
                tree.column("Montant", width=80)
                tree.column("Adresse Local", width=150)
                tree.column("District", width=130)
                tree.column("Libellé Local", width=150)
                tree.column("Référence Compteur", width=150)
                tree.column("Type Compteur", width=150)
                tree.column("nom", width=50)
                tree.column("prenom", width=80)

                Style=ttk.Style()
                Style.theme_use("clam")
                Style.configure("Treeview",
                                background="silver",
                                foreground="black",
                                rowheight=30,
                                fieldbackground="#336699")
                Style.map("Treeview",background=[('selected','green')])
                # Afficher le Treeview
                tree.place(x=0,y=150, height=600)

                def retour_a_laccueil():
                    home.destroy()
                    accueil(id_value)
                b_accueil=Button(home,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=80,y=650,width=150, height=30)
                b_accueil.configure(font=font4)
                def exit():
                    home.destroy()

                b_exit=Button(home,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)

                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)

                user_label=Label(home,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                home.mainloop()
  
            def afficher_user():
                acc.destroy()
                us=Tk()
                us.title("Consulter Les Employés")
                # full screan tkinter
                width= us.winfo_screenwidth()
                height= us.winfo_screenheight()
                #setting tkinter window size
                us.geometry("%dx%d" % (width, height))
                #wallpaper color
                us.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                font=tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(us,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                def load_table():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query = '''SELECT 
                                    userid,
                                    nom,
                                    prenom,
                                    password
                                FROM
                                    user u'''
                        cursor.execute(query)
                        T = cursor.fetchall()
                        # Convert the result to a list of strings
                        
                        return T
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                # Créer le widget Treeview pour afficher les données
                columns = ("Identifiant","Nom", "Prenom", "Mot de Passe")
                tree = ttk.Treeview(us, columns=columns, show="headings")
                # Configurer les en-têtes de colonne
                for col in columns:
                    tree.heading(col, text=col)
                
                # Charger les données depuis la base de données
                data = load_table()
                
                # Insérer les données dans le Treeview
                for row in data:
                    tree.insert("", "end", values=row)

                tree.column("Identifiant", width=340)
                tree.column("Nom", width=340)
                tree.column("Prenom", width=340)
                tree.column("Mot de Passe", width=335)

                Style=ttk.Style()
                Style.theme_use("clam")
                Style.configure("Treeview",
                                background="silver",
                                foreground="black",
                                rowheight=25,
                                fieldbackground="#336699")
                Style.map("Treeview",background=[('selected','green')])
                # Afficher le Treeview
                tree.place(x=0,y=150, height=600)
                
                def exit():
                    us.destroy()
                exit_button=Button(us,text="Exit",bg='#B04BE3',fg="#000066",bd=5,command =exit)
                exit_button.place(x=1150,y=650,width=150, height=30)
                exit_button.configure(font=font)


                def retour_a_laccueil():
                    us.destroy()
                    accueil(id_value)
                b_accueil=Button(us,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font)
                us.mainloop()

            def add_district():
                acc.destroy()
                dis=Tk()
                dis.title("Ajouter Un District")
                # full screan tkinter
                width= dis.winfo_screenwidth()
                height= dis.winfo_screenheight()
                #setting tkinter window size
                dis.geometry("%dx%d" % (width, height))
                #wallpaper color
                dis.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                
                def add_dis():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query="select district from district"
                        cursor.execute(query)
                        district_items = cursor.fetchall()
                        # Convert the result to a list of strings
                        district_item_names = [row[0] for row in district_items]
                        #return district_item_names
                        if  E.get().strip()!="":
                            if E.get() not in district_item_names:
                                q="insert into district(district) values (%s)"
                                cursor.execute(q,(E.get(),))
                                connection.commit()
                                E.delete(0,END)
                                messagebox.showinfo("Message", "Ajouté avec succés")    
                            else:
                                messagebox.showinfo("Message", "ce district exist déjà") 
                        else:           
                            pass 
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
                l=Label(dis,text="Ajouter Un District :",bg='#336699',fg="#130D41")
                l.place(x=260,y=330,width=300,height=30)
                l.configure(font=font4)

                E=Entry(dis,bg="#ccffff",font=font4)
                E.place(x=560,y=320,width=500,height=50)

                B=Button(dis,text="Ajouter",command=add_dis,bd=5,bg='#B04BE3',fg="#000066")
                B.place(x=610,y=650,width=150,height=30)
                B.configure(font=font4)
                
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(dis,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                def exit():
                    dis.destroy()
                b_exit=Button(dis,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)
                def retour_a_laccueil():
                    dis.destroy()
                    accueil(id_value)
               
                b_accueil=Button(dis,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)

                dis.mainloop()
   
            def add_user():
                    acc.destroy()
                    usr=Tk()
                    usr.title("Ajouter Un Employé")
                    # full screan tkinter
                    width= usr.winfo_screenwidth()
                    height= usr.winfo_screenheight()
                    #setting tkinter window size
                    usr.geometry("%dx%d" % (width, height))
                    #wallpaper color
                    usr.configure(bg='#336699')
                    #logo etap------------
                    img=Image.open("etap.jpg")
                    imag=img.resize((300, 150))
                    my_img = ImageTk.PhotoImage(imag)
                    my_label=Label(image=my_img)
                    my_label.place(x=0,y=0)
                    
                    def add_usr():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            query="select nom,prenom from user"
                            cursor.execute(query)
                            user_name = cursor.fetchall()
                            
                            # Retrieve local items based on the selected district
                            query="select userid,password from user"
                            cursor.execute(query)
                            user_info = cursor.fetchall()
                            user_id=[i[0] for i in user_info]

                            def password_controle(password):
                                if not(len(password)>6):
                                    messagebox.showinfo("Message", "nombre de caracteres invalide ")
                                else:
                                    if  password.isnumeric() or password.isalpha():
                                        messagebox.showinfo("Message", "le mot de passe doit etre composée des chiffres et des lettres  ")
                                    else:
                                        return True
                                return False   
                            
                            try:    
                                if E_name.get().strip()!="" and E_prenom.get().strip()!="":
                                    if (E_name.get(),E_prenom.get()) not in user_name:
                                        try:
                                            int(E_ID.get())
                                        except:    
                                            messagebox.showinfo("Message", "Verifier l'ID ")
                                        if int(E_ID.get()) not in user_id :
                                            if password_controle(E_PASSWORD.get()):
                                                q="insert into user values (%s,%s,%s,%s)"
                                                data_list=(E_ID.get(),E_name.get(),E_prenom.get(),E_PASSWORD.get())
                                                cursor.execute(q,data_list)
                                                connection.commit()   
                                                E_ID.delete(0,END) 
                                                E_name.delete(0,END)
                                                E_prenom.delete(0,END)
                                                E_PASSWORD.delete(0,END)
                                                messagebox.showinfo("Message", "Ajouté avec succés ")
                                        else:
                                            messagebox.showinfo("Message", "ID exist deja ")
                                            E_ID.delete(0,END)  
                                    else:
                                        messagebox.showinfo("Message", "l'Employé existe deja !")    
                                        E_name.delete(0,END)
                                        E_prenom.delete(0,END)
                                else:
                                    pass        
                            except:
                                pass
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                    font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                    l_name=Label(usr,text="Nom :",bg='#336699',fg="#130D41")
                    l_name.place(x=310,y=190,width=300,height=30)
                    l_name.configure(font=font4)

                    E_name=Entry(usr,bg="#ccffff",font=font4)
                    E_name.place(x=560,y=180,width=500,height=50)

                    l_prenom=Label(usr,text="Prénom :",bg='#336699',fg="#130D41")
                    l_prenom.place(x=290,y=290,width=300,height=30)
                    l_prenom.configure(font=font4)

                    E_prenom=Entry(usr,bg="#ccffff",font=font4)
                    E_prenom.place(x=560,y=280,width=500,height=50)

                    l_ID=Label(usr,text="Identifiant :",bg='#336699',fg="#130D41")
                    l_ID.place(x=280,y=390,width=300,height=30)
                    l_ID.configure(font=font4)

                    E_ID=Entry(usr,bg="#ccffff",font=font4)
                    E_ID.place(x=560,y=380,width=500,height=50)

                    l_PASSWORD=Label(usr,text="Mot De Passe :",bg='#336699',fg="#130D41")
                    l_PASSWORD.place(x=260,y=490,width=300,height=30)
                    l_PASSWORD.configure(font=font4)

                    E_PASSWORD=Entry(usr,bg="#ccffff",font=font4)
                    E_PASSWORD.place(x=560,y=480,width=500,height=50)

                    B=Button(usr,text="Ajouter",command=add_usr,bd=5,bg='#B04BE3',fg="#000066")
                    B.place(x=610,y=650,width=150,height=30)
                    B.configure(font=font4)
                    
                    font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                    user_label=Label(usr,text=user_name,fg="black",bg='#336699')
                    user_label.place(x=1200,y=20)
                    user_label.configure(font=font3)

                    def retour_a_laccueil():
                        usr.destroy()
                        accueil(id_value)
                    b_accueil=Button(usr,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                    b_accueil.place(x=65,y=650,width=150, height=30)
                    b_accueil.configure(font=font4)
                    
                    def exit():
                        usr.destroy()

                    b_exit=Button(usr,text="Exit",command=exit,bd=5,bg='#B04BE3',fg="#000066")
                    b_exit.place(x=1150,y=650,width=150, height=30)
                    b_exit.configure(font=font4)

                    usr.mainloop()

            def add_local():
                try:
                    acc.destroy()
                except Exception:
                    pass  
                loc=Tk()
                loc.title("Ajouter Un Local")
                # full screan tkinter
                width= loc.winfo_screenwidth()
                height= loc.winfo_screenheight()
                #setting tkinter window size
                loc.geometry("%dx%d" % (width, height))
                #wallpaper color
                loc.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                
                def add_district():
                    loc.destroy()
                    dis=Tk()
                    dis.title("Ajouter Un District")
                    # full screan tkinter
                    width= dis.winfo_screenwidth()
                    height= dis.winfo_screenheight()
                    #setting tkinter window size
                    dis.geometry("%dx%d" % (width, height))
                    #wallpaper color
                    dis.configure(bg='#336699')
                    #logo etap------------
                    img=Image.open("etap.jpg")
                    imag=img.resize((300, 150))
                    my_img = ImageTk.PhotoImage(imag)
                    my_label=Label(image=my_img)
                    my_label.place(x=0,y=0)
                    
                    def add_dis():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            query="select district from district"
                            cursor.execute(query)
                            district_items = cursor.fetchall()
                            # Convert the result to a list of strings
                            district_item_names = [row[0] for row in district_items]
                            #return district_item_names
                            if E.get() not in district_item_names:
                                q="insert into district(district) values (%s)"
                                cursor.execute(q,(E.get(),))
                                connection.commit()
                                messagebox.showinfo("Message", "Ajouté avec succés")    
                            else:
                                messagebox.showinfo("Message", "ce district exist déjà")    
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                    font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
                    l=Label(dis,text="Ajouter Un District :",bg='#336699',fg="#130D41")
                    l.place(x=260,y=330,width=300,height=30)
                    l.configure(font=font4)

                    E=Entry(dis,bg="#ccffff",font=font4)
                    E.place(x=560,y=320,width=500,height=50)

                    B=Button(dis,text="Ajouter",command=add_dis,bd=5,bg='#B04BE3',fg="#000066")
                    B.place(x=610,y=650,width=150,height=30)
                    B.configure(font=font4)

                    def retour():
                        dis.destroy()
                        add_local()

                    B=Button(dis,text="Retour",command=retour,bd=5,bg='#B04BE3',fg="#000066")
                    B.place(x=1150,y=650,width=150,height=30)
                    B.configure(font=font4)

                    font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                    user_label=Label(dis,text=user_name,fg="black",bg='#336699')
                    user_label.place(x=1200,y=20)
                    user_label.configure(font=font3)

                    dis.mainloop()

                def load_districts():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT district FROM district"
                        cursor.execute(query)
                        districts = cursor.fetchall()
                        # Convert the result to a list of strings
                        district_names = [row[0] for row in districts]
                        return district_names
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def code_district():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "select codedistrict from district where district= %s;"
                        cursor.execute(query,(district_combobox.get(),))
                        code_dis = cursor.fetchall()
                        return code_dis
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def add_loc():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local items based on the selected district
                        query="select libellelocal,adresselocal from locaux"
                        cursor.execute(query)
                        local_adress_list = cursor.fetchall()
                        if E_libelle.get().strip()!="" and E_adress.get().strip()!="":
                            if (E_libelle.get(),E_adress.get()) not in local_adress_list:
                                code_dis=code_district()
                                q="insert into locaux(libellelocal,adresselocal,codedistrict) values (%s,%s,%s)"
                                data_list=(E_libelle.get(),E_adress.get(),code_dis[0][0])
                                cursor.execute(q,data_list)
                                connection.commit()   
                                E_libelle.delete(0,END) 
                                E_adress.delete(0,END)
                                messagebox.showinfo("Message", "Ajouté avec succés ") 
                            else:
                                messagebox.showinfo("Message", "l'ocal exist deja !")    
                                E_libelle.delete(0,END)
                                E_adress.delete(0,END)

                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()                

                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                B=Button(loc,text="Ajouter \n Un District",command=add_district,bd=5,bg="#669999",fg="#130D41")
                B.place(x=1100,y=180,width=200,height=50)
                B.configure(font=font4)

                district_combobox = ttk.Combobox(loc)
                district_combobox.place(x=560,y=180,width=500,height=50)
                district_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                district_combobox['values'] = load_districts()
                district_combobox.set(district_combobox['values'][0])  # Set the default value
                district_combobox['state']='readonly'

                l_name=Label(loc,text="District :",bg='#336699',fg="#130D41")
                l_name.place(x=290,y=190,width=270,height=30)
                l_name.configure(font=font4)

                l_libelle=Label(loc,text="Local :",bg='#336699',fg="#130D41")
                l_libelle.place(x=285,y=290,width=300,height=30)
                l_libelle.configure(font=font4)

                E_libelle=Entry(loc,bg="#ccffff",font=font4)
                E_libelle.place(x=560,y=280,width=500,height=50)

                l_adress=Label(loc,text="Adresse :",bg='#336699',fg="#130D41")
                l_adress.place(x=275,y=390,width=300,height=30)
                l_adress.configure(font=font4)

                E_adress=Entry(loc,bg="#ccffff",font=font4)
                E_adress.place(x=560,y=380,width=500,height=50)
                
                B=Button(loc,text="Ajouter",command=add_loc,bd=5,bg='#B04BE3',fg="#000066")
                B.place(x=610,y=650,width=150,height=30)
                B.configure(font=font4)
                
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(loc,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                def retour_a_laccueil():
                    loc.destroy()
                    accueil(id_value)
                b_accueil=Button(loc,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)
                def exit():
                    loc.destroy()

                b_exit=Button(loc,text="Exit",command=exit,bd=5,bg='#B04BE3',fg="#000066")
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)

                loc.mainloop()

            def add_compteur():
                try:
                    acc.destroy()
                except Exception:
                    pass   
                cmp=Tk()
                # full screan tkinter
                width= cmp.winfo_screenwidth()
                height= cmp.winfo_screenheight()
                #setting tkinter window size
                cmp.geometry("%dx%d" % (width, height))
                cmp.title("Ajouter Un Compteur")
                #wallpaper color
                cmp.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_local():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve local names from the database
                        query = "SELECT libellelocal,adresselocal FROM locaux"
                        cursor.execute(query)
                        local = cursor.fetchall()
                        locals=[]
                        for l in local:
                            locals.append(l[0]+' @= '+l[1])
                    
                        return locals
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def code_local():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        s=local_combobox.get()
                        # Retrieve codelocal from the database
                        query = "select codelocal from locaux where libellelocal= %s and adresselocal=%s;"
                        cursor.execute(query,(s[:s.find("@")].strip(),s[s.find("@")+2:].strip()))
                        code_loc = cursor.fetchall()
                        return code_loc
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def type_compteur():
                    if type_combobox.get()=="Électricité":
                        code_type=1
                    elif type_combobox.get()=="Eau":
                        code_type=2
                    else :
                        code_type=3   
                    return code_type

                def add_cmp():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # list of compteur references 
                        query="select reference from compteur"
                        cursor.execute(query)
                        list_ref = cursor.fetchall()
                        code_type=type_compteur()
                        s=local_combobox.get()
                        try:
                            ref=(int(E_ref.get()),)
                        except:
                            messagebox.showinfo("Message", "Verifier la reference !")  

                        if  ref not in list_ref:
                            code_loc=code_local()
                            try:        
                                q="insert into compteur(reference,codelocal,codetypecompteur) values (%s,%s,%s)"
                                data_list=(E_ref.get(),code_loc[0][0],code_type)
                                cursor.execute(q,data_list)
                                connection.commit()   
                                E_ref.delete(0,END) 
                                messagebox.showinfo("Message", "Ajouté avec succés ") 
                            except:
                                messagebox.showinfo("Message", "invalid local !")        
                        else:
                            messagebox.showinfo("Message", "compteur exist deja !")    
                            E_ref.delete(0,END)
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
                def add_loc():
                    cmp.destroy()
                    add_local()
                B=Button(cmp,text="Ajouter \n un local",command=add_loc,bd=5,bg="#669999",fg="#130D41")
                B.place(x=1100,y=180,width=200,height=50)
                B.configure(font=font4)

                l_name=Label(cmp,text="Local :",bg='#336699',fg="#130D41")
                l_name.place(x=290,y=190,width=270,height=30)
                l_name.configure(font=font4)

                local_combobox = ttk.Combobox(cmp)
                local_combobox.place(x=560,y=180,width=500,height=50)
                local_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                local_combobox['values'] = load_local()
                try:
                    local_combobox.set(local_combobox['values'][0])  # Set the default value
                except:
                    pass
                local_combobox['state']='readonly'

                l_type=Label(cmp,text="Type Compteur :",bg='#336699',fg="#130D41")
                l_type.place(x=290,y=290,width=270,height=30)
                l_type.configure(font=font4)

                type_combobox = ttk.Combobox(cmp)
                type_combobox.place(x=560,y=280,width=500,height=50)
                type_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                type_combobox['values'] = ["Électricité","Gaz","Eau"]
                type_combobox.set(type_combobox['values'][0])  # Set the default value
                type_combobox['state']='readonly'

                l_ref=Label(cmp,text="Référence :",bg='#336699',fg="#130D41")
                l_ref.place(x=285,y=390,width=300,height=30)
                l_ref.configure(font=font4)

                E_ref=Entry(cmp,bg="#ccffff",font=font4)
                E_ref.place(x=560,y=380,width=500,height=50)

                B=Button(cmp,text="Ajouter",command=add_cmp,bd=5,bg='#B04BE3',fg="#000066")
                B.place(x=610,y=650,width=150,height=30)
                B.configure(font=font4)
                
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(cmp,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                def retour_a_laccueil():
                    cmp.destroy()
                    accueil(id_value)
                b_accueil=Button(cmp,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)
                def exit():
                    cmp.destroy()
                b_exit=Button(cmp,text="Exit",command=exit,bd=5,bg='#B04BE3',fg="#000066")
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)

                cmp.mainloop()

            def user_supression():
                try:
                    acc.destroy()
                except Exception:
                    pass
                sup =Tk()
                sup.title("Supprimer Un Employé")
                # full screan tkinter
                width= sup.winfo_screenwidth()
                height= sup.winfo_screenheight()
                #setting tkinter window size
                sup.geometry("%dx%d" % (width, height))
                #wallpaper color
                sup.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_user():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT userid,nom,prenom FROM user where userid!=159"
                        cursor.execute(query)
                        user_info = cursor.fetchall()
                        # Convert the result to a list of strings
                        user = [f"ID : {row[0]} , {row[1]} {row[2]}" for row in user_info]
                        return user
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def delete_user():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        user_info=load_user()
                        try:
                            if user_combobox.get() in user_info:
                                msg_box=messagebox.askquestion('Supprimer',"êtes-vous sûr de supprimer l'Employé ?",icon='warning')
                                if msg_box == 'yes':
                                    query = "delete from user where userid=%s"
                                    cursor.execute(query,(int(user_combobox.get().split()[2]),))
                                    connection.commit()
                                    messagebox.showinfo('Done', 'Supprimer Avec succés')
                                    sup.destroy()
                                    user_supression()
                            else:
                                messagebox.showinfo('Erreur', 'Employé inexistant ') 
                        except Exception:
                            
                            pass

                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()            

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                user_combobox = ttk.Combobox(sup)
                user_combobox.place(x=380, y=300, width=600, height=50)
                user_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                user_info=load_user()
                user_combobox['values'] = user_info
                try:
                    user_combobox.set(user_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                user_combobox['state']='readonly'

                font=tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                
                delete_button=Button(sup,text="Supprimer",bg='#B04BE3',fg="#000066",bd=5,command =delete_user)
                delete_button.place(x=610,y=650,width=150, height=30)
                delete_button.configure(font=font)
                def exit():
                    sup.destroy()
                exit_button=Button(sup,text="Exit",bg='#B04BE3',fg="#000066",bd=5,command =exit)
                exit_button.place(x=1150,y=650,width=150, height=30)
                exit_button.configure(font=font)

                def retour_a_laccueil():
                    sup.destroy()
                    accueil(id_value)
                b_accueil=Button(sup,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font)

                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(sup,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                sup.mainloop()

            def update_facture():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                upd =Tk()
                upd.title("Modifier Une Facture")
                # full screan tkinter
                width= upd.winfo_screenwidth()
                height= upd.winfo_screenheight()
                #setting tkinter window size
                upd.geometry("%dx%d" % (width, height))
                #wallpaper color
                upd.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
                def load_factures():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT key_facture,numerofacture,month,year,newindex,montant FROM facture"
                        cursor.execute(query)
                        f = cursor.fetchall()
                        # Convert the result to a list of strings
                        facture=[f"{row[0]} ) Reference = {row[1]} , Mois = {row[2]} , Année = {row[3]}  , Nouveau Indice = {row[4]} , Montant = {row[5]}" for row in f]
                        return facture
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()
                def afficher_fac():   
                    try:
                        global key
                        global id
                        key=fact_combobox.get().split()[0]    
                        id=fact_combobox.get().split()[4]
                    except:
                        return
                    upd.destroy()
                    try:
                        upd.destroy()
                    except Exception:
                        pass 
                    up =Tk()
                    up.title("Modifier Une Factures")
                    # full screan tkinter
                    width= up.winfo_screenwidth()
                    height= up.winfo_screenheight()
                    #setting tkinter window size
                    up.geometry("%dx%d" % (width, height))
                    #wallpaper color
                    up.configure(bg='#336699')
                    #logo etap------------
                    img=Image.open("etap.jpg")
                    imag=img.resize((300, 150))
                    my_img = ImageTk.PhotoImage(imag)
                    my_label=Label(image=my_img)
                    my_label.place(x=0,y=0)

                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        query = "SELECT month,year,newindex,montant from facture where key_facture=%s"
                        cursor.execute(query,(int(key),))
                        info = cursor.fetchall()
                        # Convert the result to a list of strings
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                    def update():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            
                            cursor = connection.cursor()
                            try:
                                m=int(E_month.get())
                                y=int(E_year.get())
                                nx=int(E_new_index.get())
                                mo=float(E_montant.get())
                            except:
                                messagebox.showinfo("Message", "Verifier les champs")     
                                    
                            if(m>0 and m<13 and y<2100 and y>2000):
                                q="select  MIN(key_facture) from facture where key_facture > %s and numerofacture = %s"
                                cursor.execute(q,(int(key),id))
                                a=cursor.fetchall()
                               
                                msg_box=messagebox.askquestion('Supprimer',"êtes-vous sûr de Modifier la facture ?",icon='warning')
                                if msg_box == 'yes':
                                    query = """update facture SET 
                                                month=%s,
                                                year=%s,
                                                newindex=%s,
                                                montant=%s
                                                where key_facture=%s"""
                                    cursor.execute(query,(m,y,nx,mo,key))
                                    
                                    query2 = """update facture SET 
                                                oldindex=%s
                                                where key_facture=%s"""
                                    cursor.execute(query2,(nx,a[0][0]))
                                    connection.commit()
                                    messagebox.showinfo("Message", "Modifier Avec Succée")             
                            else:
                                messagebox.showinfo("Message", "ERREUR: Verifier le mois et l'année")
                                
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()


                    font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                    l_month=Label(up,text="Mois:",bg='#336699',fg="#130D41")
                    l_month.place(x=350,y=130,width=300,height=30)
                    l_month.configure(font=font4)

                    E_month=Entry(up,bg="#ccffff",font=font4)
                    E_month.place(x=600,y=120,width=500,height=50)

                    l_year=Label(up,text="Année:",bg='#336699',fg="#130D41")
                    l_year.place(x=340,y=230,width=300,height=30)
                    l_year.configure(font=font4)

                    E_year=Entry(up,bg="#ccffff",font=font4)
                    E_year.place(x=600,y=220,width=500,height=50)

                    l_new_index=Label(up,text="Nouvel Indice:",bg='#336699',fg="#130D41")
                    l_new_index.place(x=300,y=330,width=300,height=30)
                    l_new_index.configure(font=font4)

                    E_new_index=Entry(up,bg="#ccffff",font=font4)
                    E_new_index.place(x=600,y=320,width=500,height=50)


                    l_montant=Label(up,text="Montant:",bg='#336699',fg="#130D41")
                    l_montant.place(x=290,y=430,width=300,height=30)
                    l_montant.configure(font=font4)

                    E_montant=Entry(up,bg="#ccffff",font=font4)
                    E_montant.place(x=600,y=420,width=500,height=50)

                    button=Button(up,text="Modifier",bg='#B04BE3',fg="#000066",bd=5,command =update)
                    button.place(x=610,y=650,width=150, height=30)
                    button.configure(font=font4)
                    E_month.insert(0,info[0][0])
                    E_year.insert(0,info[0][1])
                    E_new_index.insert(0,info[0][2])
                    E_montant.insert(0,info[0][3])

                    font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                    get_user_name(id_value)
                    user_label=Label(up,text=user_name,fg="black",bg='#336699')
                    user_label.place(x=1200,y=20)
                    user_label.configure(font=font3)

                    def exit():
                        up.destroy()
                    b_exit=Button(up,text='Exit',bg='#B04BE3',fg="#000066",bd=5,command=exit)
                    b_exit.place(x=1150,y=650,width=150, height=30)
                    b_exit.configure(font=font4)

                    def retour_a_laccueil():
                        up.destroy()
                        update_facture()
                    b_accueil=Button(up,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                    b_accueil.place(x=65,y=650,width=150, height=30)
                    b_accueil.configure(font=font4)


                    up.mainloop()
                
                font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

                msg_label=Label(upd, text="Choisissez La Facture a Modifier ",bg='#336699',fg="#130D41")
                msg_label.place(x=500,y=200)
                msg_label.configure(font=font4)
                
                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                fact_combobox = ttk.Combobox(upd)
                fact_combobox.place(x=30, y=350, width=1300, height=50)
                fact_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                fact_combobox['values'] = load_factures()
                try:
                    fact_combobox.set(fact_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                fact_combobox['state']='readonly'

                open_button=Button(upd,text="Modifier",bg='#B04BE3',fg="#000066",bd=5,command =afficher_fac)
                open_button.place(x=610,y=650,width=150, height=30)
                open_button.configure(font=font4)

                def exit():
                    upd.destroy()
                b_exit=Button(upd,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
                b_exit.place(x=1150,y=650,width=150, height=30)
                b_exit.configure(font=font4)

                def retour_a_laccueil():
                    upd.destroy()
                    accueil(id_value)
                b_accueil=Button(upd,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font4)

                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(upd,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                upd.mainloop()

            def facture_supression():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                sup =Tk()
                sup.title("Supprimer Une Facture")
                # full screan tkinter
                width= sup.winfo_screenwidth()
                height= sup.winfo_screenheight()
                #setting tkinter window size
                sup.geometry("%dx%d" % (width, height))
                #wallpaper color
                sup.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)

                def load_facture():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "SELECT numerofacture,month,year FROM facture"
                        cursor.execute(query)
                        f = cursor.fetchall()
                        # Convert the result to a list of strings
                        facture = [f"Reference = {row[0]} , Mois = {row[1]} , Année = {row[2]}" for row in f]
                        return facture
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                def delete_facture():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        facture=load_facture()
                        try:
                            msg_box=messagebox.askquestion('Supprimer',"êtes-vous sûr de supprimer la facture ?",icon='warning')
                            if msg_box == 'yes':
                                query = "delete from facture where numerofacture = %s and month=%s and year=%s"
                                cursor.execute(query,(fact_combobox.get().split()[2],fact_combobox.get().split()[6],fact_combobox.get().split()[10]))
                                connection.commit()
                                messagebox.showinfo('Done', 'Supprimer Avec succés')
                                sup.destroy()
                                facture_supression()                    
                        except Exception:
                            pass

                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()            

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")
                # Create the district combobox
                fact_combobox = ttk.Combobox(sup)
                fact_combobox.place(x=30, y=300, width=1300, height=50)
                fact_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                fact_combobox['values'] = load_facture()
                try:
                    fact_combobox.set(fact_combobox['values'][0])  # Set the default value
                except Exception:
                    pass
                fact_combobox['state']='readonly'
                font=tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                
                delete_button=Button(sup,text="Supprimer",bg='#B04BE3',fg="#000066",bd=5,command =delete_facture)
                delete_button.place(x=610,y=650,width=150, height=30)
                delete_button.configure(font=font)
                def exit():
                    sup.destroy()
                exit_button=Button(sup,text="Exit",bg='#B04BE3',fg="#000066",bd=5,command =exit)
                exit_button.place(x=1150,y=650,width=150, height=30)
                exit_button.configure(font=font)

                def retour_a_laccueil():
                    sup.destroy()
                    accueil(id_value)
                b_accueil=Button(sup,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
                b_accueil.place(x=65,y=650,width=150, height=30)
                b_accueil.configure(font=font)

                #user_name_au_fond_de_la_page
                font2 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(sup,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font2)

                sup.mainloop()

            def dashboerd():
                try:
                    acc.destroy()
                except Exception:
                    pass    
                dash =Tk()
                dash.title("Dashboerd")
                # full screan tkinter
                width= dash.winfo_screenwidth()
                height= dash.winfo_screenheight()
                #setting tkinter window size
                dash.geometry("%dx%d" % (width, height))
                #wallpaper color
                dash.configure(bg='#336699')
                #logo etap------------
                img=Image.open("etap.jpg")
                imag=img.resize((300, 150))
                my_img = ImageTk.PhotoImage(imag)
                my_label=Label(image=my_img)
                my_label.place(x=0,y=0)
 
                def innerdascboard():
                    year=year_combobox.get()
                    try:
                        dash.destroy()
                    except Exception:
                        pass    
                    def type_cmp2(a):
                        if a == 1:
                            return 'Électricité'
                        elif a==2:
                            return 'Eau'
                        else:
                            return 'Gaz'    
                    stat = Tk()
                    stat.title("Dashboard")
                    stat.state('zoomed')
                    stat.configure(bg='#F7BDF5')

                    def mesure():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            list=[]
                            if year=="ALL":
                                for i in range(1,4):
                                    query = "select count(distinct numerofacture) from facture join compteur on referencecompteur=reference where codetypecompteur=%s"
                                    cursor.execute(query,(i,))
                                    f = cursor.fetchall()
                                    list.append(f)
                            else:
                                for i in range(1,4):
                                    query = "select count(distinct numerofacture) from facture join compteur on referencecompteur=reference where year=%s and codetypecompteur=%s"
                                    cursor.execute(query,(year,i))
                                    f = cursor.fetchall()
                                    list.append(f)
                            
                            return list
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()
                    font2 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                    
                    nbfact_label=Label(stat,text="Nombre des Factures:",fg="#336699",bg='#F7BDF5')
                    nbfact_label.place(x=145,y=15)
                    nbfact_label.configure(font=font2)
                    
                    t=mesure()
                    stat.totalfactureImage = Image.open('image3.jpeg')
                    photo = ImageTk.PhotoImage(stat.totalfactureImage)
                    stat.totalfacture = Label(stat, image=photo)
                    stat.totalfacture.image = photo
                    stat.totalfacture.place(x=150, y=60,width=120,height=120)

                    stat.totalfacture_text = Label(stat, text=t[0],bg="#ff8bb6", font=("", 25, "bold"))
                    stat.totalfacture_text.place(x=195, y=100)

                    stat.total_facture = Label(stat, text='Électricité',bg="#ff8bb6", font=("", 13, "bold"))
                    stat.total_facture.place(x=150, y=60)

                    stat.totalfacture1Image = Image.open('image4.jpeg')
                    photo = ImageTk.PhotoImage(stat.totalfacture1Image)
                    stat.totalfacture1 = Label(stat, image=photo)
                    stat.totalfacture1.image = photo
                    stat.totalfacture1.place(x=365, y=60,width=120,height=120)

                    stat.totalfacture1_text = Label(stat, text=t[1],bg="#de3372", font=("", 25, "bold"))
                    stat.totalfacture1_text.place(x=410, y=100)

                    stat.total_facture1 = Label(stat, text='EAU',bg="#de3372", font=("", 13, "bold"))
                    stat.total_facture1.place(x=365, y=60)

                    stat.totalfacture2Image = Image.open('image0.jpeg')
                    photo = ImageTk.PhotoImage(stat.totalfacture2Image)
                    stat.totalfacture2 = Label(stat, image=photo)
                    stat.totalfacture2.image = photo
                    stat.totalfacture2.place(x=580, y=60,width=120,height=120)

                    stat.totalfacture2_text = Label(stat, text=t[2],bg="#c64c79", font=("", 25, "bold"))
                    stat.totalfacture2_text.place(x=625, y=100)

                    stat.total_facture2 = Label(stat, text='GAZ',bg="#c64c79", font=("", 13, "bold"))
                    stat.total_facture2.place(x=580, y=60)

                    side_frame = Frame(stat, bg="#336699")
                    side_frame.pack(side="left", fill="y")

                    label = Label(side_frame, text="Dashboard", bg="#336699", fg="#FFF", font=25)
                    label.pack(pady=50, padx=20)

                    def load_montant_per_year():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            if year!='ALL':
                                query = "select codetypecompteur,sum(montant) from facture join compteur on referencecompteur=reference where year=%s group by codetypecompteur order by codetypecompteur"
                                cursor.execute(query,(year,))
                            else:
                                query = "select codetypecompteur,sum(montant) from facture join compteur on referencecompteur=reference group by codetypecompteur order by codetypecompteur"
                                cursor.execute(query)
                            f = cursor.fetchall()
                            
                            # Convert the result to a list of strings
                            return f
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()                        

                    list=load_montant_per_year() 
                    fig1,ax1=plt.subplots(figsize=(6,2))
                    x = [type_cmp2(row[0]) for row in list]
                    y = [row[1] for row in list]

                    ax1.bar(x,y,color="#336699")
                    ax1.set_title("Montant par Type Compteur",color="#c7024b")
                    ax1.set_xlabel("Type Compteur")
                    ax1.set_ylabel("Montant")
                    #plt.show()

                    def piechart():
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            if year!='ALL':
                                query = "select codetypecompteur,sum(montant) from facture join compteur on referencecompteur=reference where year=%s group by codetypecompteur order by codetypecompteur;"
                                cursor.execute(query,(int(year),))
                            else:
                                query = "select codetypecompteur,sum(montant) from facture join compteur on referencecompteur=reference group by codetypecompteur  order by codetypecompteur"
                                cursor.execute(query)
                            f = cursor.fetchall()
                           
                            return f
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                    list1=piechart()  
                    montant = [row[1] for row in list1]
                    label=[type_cmp2(row[0]) for row in list1]
                    colors=["#de3372","#162FCF","#c64c79"]
                    fig2,ax2=plt.subplots()
                    ax2.pie(montant,labels=label, autopct='%1.1f%%',colors=colors,shadow=True, startangle=90)
                    ax2.set_title("Le Cout par Typecompteur",color="#c7024b")

                    def load_consommation_per_local(type):
                        try:
                            # Establish a connection to the MySQL server
                            connection = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='112713',
                                database='etapproject'
                            )
                            # Create a cursor
                            cursor = connection.cursor()
                            if year=="ALL":
                                query = "select libellelocal,adresselocal,sum(newindex),sum(oldindex) from facture join compteur c on referencecompteur=reference join locaux lc on lc.codelocal=c.codelocal where codetypecompteur=%s group by lc.codelocal "
                                cursor.execute(query,(type,))
                            else:
                                query = "select libellelocal,adresselocal,sum(newindex),sum(oldindex) from facture join compteur c on referencecompteur=reference join locaux lc on lc.codelocal=c.codelocal where codetypecompteur=%s and year=%s group by lc.codelocal limit 4"
                                cursor.execute(query,(type,year))
                                    
                            f = cursor.fetchall()
                            return f
                        except mysql.connector.Error as error:
                            print("Error:", error)
                        finally:
                            # Close the cursor and connection
                            if cursor:
                                cursor.close()
                            if connection:
                                connection.close()

                    list=load_consommation_per_local(3)
                    local = [f"{row[0]} {row[1]}" for row in list]
                    consommation=[(row[2]-row[3])/1000 for row in list]
                    fig3,ax3=plt.subplots()
                    ax3.bar(local,consommation ,color="#336699")
                    ax3.set_xlabel("local")
                    ax3.set_ylabel('1000 m3')
                    ax3.set_title("Consommation de Gaz Par Local",color="#c7024b")

                    list=load_consommation_per_local(1)
                    local = [f"{row[0]} {row[1]}" for row in list]
                    consommation=[(row[2]-row[3])/1000 for row in list]
                    """if len(consommation)>3:
                        cons=[consommation[i] for i in range(3)]
                        consommation=cons"""
                    fig4,ax4=plt.subplots()
                    ax4.bar(local,consommation,color="#336699" )
                    ax4.set_xlabel("local")
                    ax4.set_ylabel('1000 Kwh')
                    ax4.set_title("Consommation d'Électricité Par Local",color="#c7024b")

                    list=load_consommation_per_local(2)
                    local = [f"{row[0]} {row[1]}" for row in list]
                    consommation=[(row[2]-row[3])/1000 for row in list]
                    fig5,ax5=plt.subplots(figsize=(6,2))
                    ax5.bar(local,consommation,color="#336699")
                    ax5.set_xlabel("local")
                    ax5.set_ylabel('1000 m3')
                    ax5.set_title("Consommation d'Eau Par Local",color="#c7024b")

                    canvas1 = FigureCanvasTkAgg(fig1, stat)
                    canvas1.draw()
                    canvas1.get_tk_widget().place(x=130, y=480,width=600,height=220)

                    canvas2 = FigureCanvasTkAgg(fig2, stat)
                    canvas2.draw()
                    canvas2.get_tk_widget().place(x=130, y=245,width=600,height=220)

                    canvas3 = FigureCanvasTkAgg(fig3, stat)
                    canvas3.draw()
                    canvas3.get_tk_widget().place(x=750, y=10,width=600,height=220)

                    canvas4 = FigureCanvasTkAgg(fig4, stat)
                    canvas4.draw()
                    canvas4.get_tk_widget().place(x=750, y=245,width=600,height=220)

                    canvas5 = FigureCanvasTkAgg(fig5, stat)
                    canvas5.draw()
                    canvas5.get_tk_widget().place(x=750, y=480,width=600,height=220)
                    font2 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")

                    def retour():
                        stat.destroy()
                        dashboerd()

                    B=Button(stat,text="Retour",command=retour,bd=5,bg="#c64c79",fg="Blue")
                    B.place(x=10,y=650,width=150,height=30)
                    B.configure(font=font2) 

                    stat.mainloop()

                def load_year():
                    try:
                        # Establish a connection to the MySQL server
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='112713',
                            database='etapproject'
                        )
                        # Create a cursor
                        cursor = connection.cursor()
                        # Retrieve district names from the database
                        query = "select distinct year from facture"
                        cursor.execute(query)
                        f = cursor.fetchall()
                        # Convert the result to a list of strings
                        return f
                    except mysql.connector.Error as error:
                        print("Error:", error)
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()            
                list_year=["ALL"]
                for row in load_year():
                    list_year.append(row[0])

                stylebox= ttk.Style()
                stylebox.theme_use('clam')
                stylebox.configure("TCombobox", fieldbackground= "#AFAFC2", background= "#5B5B5E")

                year_combobox = ttk.Combobox(dash)
                year_combobox.place(x=530,y=310,width=300,height=50)
                year_combobox.configure(font=tkFont.Font(family="Times New Roman", size=18, weight="bold", slant="italic"))
                year_combobox['values'] = list_year
                year_combobox.set(year_combobox['values'][0]) 
                year_combobox['state']='readonly'

                font2 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
                year_label=Label(dash,text="Choisissez l'année:",fg="#26223b",bg='#336699')
                year_label.place(x=530,y=250)
                year_label.configure(font=font2)

                #user_name_au_fond_de_la_page
                font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
                user_label=Label(dash,text=user_name,fg="black",bg='#336699')
                user_label.place(x=1200,y=20)
                user_label.configure(font=font3)

                my_button=Button(dash,text="click",command=innerdascboard,bg='#B04BE3',fg="#000066",bd=5)
                my_button.place(x=635,y=400,width=80,height=30) 
                my_button.configure(font=font2)

                def retour():
                    dash.destroy()
                    accueil(id_value)

                B=Button(dash,text="Retour",command=retour,bg='#B04BE3',fg="#000066",bd=5)
                B.place(x=65,y=650,width=150,height=30)
                B.configure(font=font2) 
                dash.mainloop()

            var = IntVar()
            R1 = Radiobutton(acc, text="Ajouter un district", bg="#CBA1C5",variable=var, value=1,
                            command=add_district)
            R1.place( anchor = W ,x=140,y=200 ,width=300,height=35)

            R2 = Radiobutton(acc, text="Ajouter un local", bg="#CBA1C5", variable=var, value=2,
                            command=add_local)
            R2.place( anchor = W ,x=140,y=300,width=300,height=35)

            R3 = Radiobutton(acc, text="Ajouter un compteur", bg="#CBA1C5", variable=var, value=3,
                            command=add_compteur)
            R3.place( anchor = W,x=140,y=400,width=300,height=35)

            R4 = Radiobutton(acc, text="Ajouter une facture", bg="#CBA1C5", variable=var, value=1,
                            command=facture )
            R4.place( anchor = W ,x=140,y=500,width=300,height=35)

            R5 = Radiobutton(acc, text="Ajouter un Employé", bg="#CBA1C5", variable=var, value=2,
                            command=add_user)
            R5.place( anchor = W ,x=540,y=200 ,width=300,height=35)

            R6 = Radiobutton(acc, text="Consulter Les Factures", bg="#CBA1C5", variable=var, value=3,
                            command=afficher_fact_admin)
            R6.place( anchor = W,x=540,y=400,width=300,height=35)

            R7 = Radiobutton(acc, text="Consulter Les Employés", bg="#CBA1C5", variable=var, value=3,
                            command=afficher_user)
            R7.place( anchor = W,x=540,y=500,width=300,height=35)

            R8 = Radiobutton(acc, text=" Suprpimer Un Employé", bg="#CBA1C5", variable=var, value=3,
                            command=user_supression)
            R8.place( anchor = W,x=940,y=300,width=300,height=35)

            R9 = Radiobutton(acc, text="Suprpimer Une Facture", bg="#CBA1C5", variable=var, value=3,
                            command=facture_supression)
            R9.place( anchor = W,x=940,y=200,width=300,height=35)

            R10 = Radiobutton(acc, text="Modifier Une Facture", bg="#CBA1C5", variable=var, value=3,
                            command=update_facture)
            R10.place( anchor = W,x=540,y=300,width=300,height=35)

            R11 = Radiobutton(acc, text="Dashboard", bg="#CBA1C5", variable=var, value=3,
                            command=dashboerd)
            R11.place( anchor = W,x=940,y=400,width=300,height=35)

            def get_user_name(id_value):
                try:
                    # Establish a connection to the MySQL server
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='112713',
                        database='etapproject'
                    )
                    
                    # Create a cursor
                    c = connection.cursor()
                    q = "select nom,prenom from user where userid=%s"
                    # Execute the query
                    c.execute(q,(id_value,))
                    r=c.fetchall() 
                    global user_name
                    user_name=r[0][0] +' '+ r[0][1]
                        
                    # Commit the changes to the database
                    connection.commit()

                except mysql.connector.Error as error:
                    print("Error:", error)

                finally:
                    # Close the cursor and connection
                    if c:
                        c.close()
                    if connection:
                        connection.close()
            font3 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic",underline=True)
            get_user_name(id_value)
            user_label=Label(acc,text=user_name,fg="black",bg='#336699')
            user_label.place(x=1200,y=20)
            user_label.configure(font=font3)

            font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
            def retour_a_laccueil():
                acc.destroy()
                home_wind()
            b_accueil=Button(acc,text='Deconnecter',bg='#336699',fg="#000066",bd=5,command=retour_a_laccueil)
            b_accueil.place(x=1150,y=650,width=150, height=30)
            b_accueil.configure(font=font4)

            acc.mainloop()

        def log_in():
            try:
                id_value = int(E_id.get())
                password = E_pass.get() 
            except:
                messagebox.showinfo("Message", "Le mot de passe ou l'ID entré est incorrect \n Vous pouvez essayer une autre foix!")
            if (int(id_value),password) != (159,'ranim0000'):
                messagebox.showinfo("Message", "Le mot de passe ou l'ID entré est incorrect \n Vous pouvez essayer une autre foix!")
                E_id.delete(0,END)
                E_pass.delete(0,END)
            else:    
                accueil(id_value)
                 
        l_id=Label(root,text="Id de L'Admin   :",bg='#336699',fg="#660033")
        E_id=Entry(root,bg='#9C9398',font=font2)
        l_pass=Label(root,text="Mot de passe  :",bg='#336699',fg="#660033")
        E_pass=Entry(root,bg='#9C9398',font=font2,show="*")

        font = tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")

        l_id.configure(font=font)
        l_pass.configure(font=font)
        l_id.place(x=450,y=250)
        E_id.place(x=650,y=250,width=200, height=30)
        l_pass.place(x=450,y=350)
        E_pass.place(x=650,y=350,width=200, height=30)

        b_login=Button(root,text='Se Connecter',bg='#B04BE3',fg="#000066",bd=5,command=log_in)
        b_login.place(x=610,y=650,width=150, height=30)
        b_login.configure(font=font)

        def exit():
            root.destroy()
        b_exit=Button(root,text='Exit',command=exit,bg='#B04BE3',fg="#000066",bd=5)
        b_exit.place(x=1150,y=650,width=150, height=30)
        b_exit.configure(font=font)

        font4=tkFont.Font(family="Times New Roman", size=16, weight="bold", slant="italic")
        def retour_a_laccueil():
            root.destroy()
            home_wind()
        b_accueil=Button(root,text='Accueil',bg='#B04BE3',fg="#000066",bd=5,command=retour_a_laccueil)
        b_accueil.place(x=65,y=650,width=150, height=30)
        b_accueil.configure(font=font4)

        root.mainloop()

    font2 = tkFont.Font(family="Times New Roman", size=25, weight="bold", slant="italic")
    font5 = tkFont.Font(family="Times New Roman", size=15, weight="bold", slant="italic")

    b_admin=Button(text="ADMIN",bg="#ffcccc",fg='#336699',bd=10,command=admin_log_in)
    b_user=Button(text='Employé',bg="#ffcccc",bd=10,fg='#336699',command=user_log_in)

    b_admin.place(x=310,y=220,width=250,height=250)
    b_user.place(x=780,y=220,width=250,height=250)

    b_admin.configure(font=font2)
    b_user.configure(font=font2)

    def exit():
        home.destroy()
    b_exit=Button(home,text='EXIT',command=exit,bg="#ffcccc",fg='#336699',bd=5)
    b_exit.place(x=615,y=600,width=100, height=30)
    b_exit.configure(font=font5)

    home.mainloop()
home_wind()  