import tkinter
import re

pencere = tkinter.Tk()
pencere.title("Calculator")
#pencere.geometry("300x400")
pencere.config(bg="#1c1c1c")

ekran = tkinter.Entry(pencere, width=12, font=("Arial", 24), justify="right", bg="#1c1c1c", fg="white", bd=0, insertbackground="white")
ekran.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=20, padx=8, pady=(8, 12))


# Sayı Butonlarının olduğu kodlar.
def bir_yaz():
        ekran.insert(tkinter.END, "1")

buton_1 = tkinter.Button(pencere, text="1", command=bir_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_1.grid(row=1, column=0)

def iki_yaz():
        ekran.insert(tkinter.END, "2")

buton_2 = tkinter.Button(pencere, text="2", command=iki_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_2.grid(row=1, column=1)

def uc_yaz():
        ekran.insert(tkinter.END, "3")

buton_3 = tkinter.Button(pencere, text="3", command=uc_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_3.grid(row=1, column=2)

def dort_yaz():
        ekran.insert(tkinter.END, "4")

buton_4 = tkinter.Button(pencere, text="4", command=dort_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_4.grid(row=2, column=0)

def bes_yaz():
        ekran.insert(tkinter.END, "5")

buton_5 = tkinter.Button(pencere, text="5", command=bes_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_5.grid(row=2, column=1)

def alti_yaz():
        ekran.insert(tkinter.END, "6")

buton_6 = tkinter.Button(pencere, text="6", command=alti_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_6.grid(row=2, column=2)


def yedi_yaz():
        ekran.insert(tkinter.END, "7")

buton_7 = tkinter.Button(pencere, text="7", command=yedi_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_7.grid(row=3, column=0)

def sekiz_yaz():
        ekran.insert(tkinter.END, "8")

buton_8 = tkinter.Button(pencere, text="8", command=sekiz_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_8.grid(row=3, column=1)

def dokuz_yaz():
        ekran.insert(tkinter.END, "9")

buton_9 = tkinter.Button(pencere, text="9", command=dokuz_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_9.grid(row=3, column=2)

def sifir_yaz():
        ekran.insert(tkinter.END, "0")

buton_0 = tkinter.Button(pencere, text="0", command=sifir_yaz, font=("Arial", 18), bg="#333333", fg="white", width=5, height=2, relief="flat")
buton_0.grid(row=4, column=1)

# İşlem Butonları

def bolme_yaz():
        ekran.insert(tkinter.END, "/")

buton_bolme = tkinter.Button(pencere, text="/", command=bolme_yaz, font=("Arial", 18), bg="#ff9500", fg="white", width=5, height=2, relief="flat")
buton_bolme.grid(row=1, column=3)

def carpma_yaz():
        ekran.insert(tkinter.END, "*")

buton_carpma = tkinter.Button(pencere, text="*", command=carpma_yaz, font=("Arial", 18), bg="#ff9500", fg="white", width=5, height=2, relief="flat")
buton_carpma.grid(row=2, column=3)

def cikarma_yaz():
        ekran.insert(tkinter.END, "-")

buton_cikarma = tkinter.Button(pencere, text="-", command=cikarma_yaz, font=("Arial", 18), bg="#ff9500", fg="white", width=5, height=2, relief="flat")
buton_cikarma.grid(row=3, column=3)

def toplama_yaz():
        ekran.insert(tkinter.END, "+")

buton_toplama = tkinter.Button(pencere, text="+", command=toplama_yaz, font=("Arial", 18), bg="#ff9500", fg="white", width=5, height=2, relief="flat")
buton_toplama.grid(row=4, column=3)

#Temizleme ve Sonuç Butonları

def temizle():
        ekran.delete(0, tkinter.END)

buton_temizle = tkinter.Button(pencere, text="C", command=temizle, font=("Arial", 18), bg="#a5a5a5", fg="black", width=5, height=2, relief="flat")
buton_temizle.grid(row=4, column=0)

def hesapla():
        ifade = ekran.get()
        if not  re.fullmatch(r"[0-9+\-*/(). ]+", ifade):
            ekran.delete(0, tkinter.END)
            ekran.insert(tkinter.END, "Geçersiz İfade")
            return
        sonuc = eval(ifade, {"__builtins__": {}})
        ekran.delete(0, tkinter.END)
        ekran.insert(tkinter.END, str(sonuc))

buton_esittir = tkinter.Button(pencere, text="=", command=hesapla, font=("Arial", 18), bg="#ff9500", fg="white", width=5, height=2, relief="flat")
buton_esittir.grid(row=4, column=2)

pencere.mainloop()

#Developed by https://github.com/xealperen