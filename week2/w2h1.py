

#
# print("1.Öğrenci Ekle")
# print("2.Öğrenci Sil")
# print("3.Tüm Öğrencileri görüntüle")
# print("4.Öğrenci numarasını görüntüle")
# print("5.Birden fazla öğrenci Sil")
# studentList=[]
# code = input("Seçim:")
# while(code!=0):
#    if code ==1:
#        studentName=input("Adı")
#        studentSurName=input("Soyadı")
#        studentList.append(studentName+" "+studentSurName)
giriş = """
(1) Öğrenci Ekle
(2) Öğrenci Sil
(3) Tüm Öğrencileri görüntüle
(4) Öğrenci numarasını görüntüle
(5) Birden fazla öğrenci Sil
"""
studentList=[]
print(giriş)

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        studentName = input("Adı: ")
        studentSurName=input("Soyadı: ")
        studentList.append(studentName+" "+studentSurName)
        print("Eklenen Öğrenci: "+studentList[-1])

    elif soru == "2":
        beforeDelLength= len(studentList)
        deleteStudent=input("Silinecek Öğrenci Adı-Soyadı: ")
        isDelete = studentList.remove(deleteStudent)
        afterDelLenght=len(studentList)
        if(beforeDelLength==afterDelLenght):print("Silme Başarısız")
        else:print("Silme başarılı")

    elif soru == "3":
       for student in studentList:
           print(student)

    elif soru == "4":
        getNumberName = input("Numarasını görüntülemek istediğiniz Öğrenci Adı Soyadı: ")
        number = studentList.index(getNumberName)
        print("Numarası: "+str(number))
    elif soru == "5":
        num1 = int(input("Silmek istediğiniz numara aralığı:başlangıç  "))
        num2 = int(input("Silmek istediğiniz numara aralığı:bitiş  "))
        for delStudent in studentList[num1:num2]:
            studentList.remove(delStudent)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

