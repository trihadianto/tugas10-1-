#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("""
To Do List
by Tri hadianto\n""")
tasks = []
def add_tugas(tugas):
    tasks.append(tugas)

def view_tugas():
    for i, tugas in enumerate(tasks):
        print(f"{i+1}. {tugas}")

def remove_tugas(index):
    del tasks[index]
    
def mark_tugas_complete(index):
    tasks[index] = 'X ' + tasks[index]

def main():
    print("Selamat Datang Di Dalam List Kamu!")
    while True:
        print("Apa Yang Ingin Anda Lakukan?")
        print("1. Tambahkan Tugas")
        print("2. Hapus Tugas")
        print("3. Tandai Tugas Yang Sudah Selesai")
        print("4. Quit")
        pilihan = int(input("Pilihan Kamu: "))
        if pilihan == 1:
            tugas = input("Masukkan Tugas: ")
            add_tugas(tugas)
        elif pilihan == 2:
            index = int(input("Masukkan nomor Tugas: "))
            remove_tugas(index)
        elif pilihan == 3:
            index = int(input("Masukkan nomor Tugas: "))
            mark_tugas_complete(index)
        elif pilihan == 4:      
            break
        else:
            
            print("ERROR,Anda Kurang Beruntung Coba Lagi.")

        
        print()
main()


# In[ ]:





# In[ ]:




