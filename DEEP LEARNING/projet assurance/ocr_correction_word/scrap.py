##################################################### SCRAPPING FIRST NAME #############################################
def scrapping_first_name_ara():
    import requests
    from bs4 import BeautifulSoup
    import csv
    from itertools import zip_longest

    resultMan=requests.get("https://rqeeqa.com/baby-names/%D8%A7%D8%B3%D9%85%D8%A7%D8%A1-%D8%A7%D9%88%D9%84%D8%A7%D8%AF.html")
    resultGirl= requests.get("https://rqeeqa.com/baby-names/girl-names.html")
    src1=resultMan.content
    src2 = resultGirl.content
    soup1=BeautifulSoup(src1,"lxml")
    soup2 = BeautifulSoup(src2, "lxml")
    names=soup1.find_all("span",{"style":"color: #f30977;"})
    names+=soup1.find_all("span",{"style":"color: #ff00ff;"})
    names+=soup1.find_all("span",{"style":"color:#3366ff;"})
    names += soup2.find_all("span", {"style": "color: #e00d69;"})
    names_save=[]
    for i in range(len(names)):
        names_save.append(names[i].text)
    for i in range(len(names_save)):
        names_save[i]=names_save[i].replace(":","").strip()
    names_save.remove('علا')
    file_list=[names_save]
    exported=zip_longest(*file_list)
    with open("first_name.csv", "w", encoding="utf-8") as file:
        wr=csv.writer(file)
        wr.writerow(["الإسم"])
        wr.writerows(exported)
############################## SCRAPPING LAST NAME #####################################################################
def scrapping_last_name_ara():
    import csv
    from itertools import zip_longest
    lakab = ['الغربي', 'الهمامي', 'الشريف', 'الدريدي', 'العياري', 'الطرابلسي', 'حمدي', 'محمد', 'الماجري', 'العبيدي',
             'السعيدي', 'العيادي', 'الرياحي', 'عمار', 'التركي', 'التومي', 'السلامي', 'الفريڨي', 'الجلاصي', 'كمون',
             'الوسلاتي', 'بن عامر', 'العرفاوي', 'ساسي', 'الشابي', 'العمري', 'بن عبدالله', 'أحمد', 'العلوي', 'السويسي',
             'بن سالم', 'بن صالح', 'المصمودي', 'منصور', 'قلال', 'عبدالله', 'حمزة', 'حداد', 'الرقيق', 'عياد', 'الصغير',
             'قاسم', 'منصوري', 'الجبالي', 'الساحلي', 'خليل', 'شعبان', 'الڨاسمي', 'لسود', 'بلحاج', 'بن حسين',
             'عبيد', 'بن علي', 'حسان', 'البحري', 'النصري', 'التريكي', 'العبيدي', 'السالمي', 'الزواري', 'التليلي',
             'التونسي', 'البجاوي', 'الجويني', 'سالم', 'الفرشيشي', 'بلحاج', 'بن عمار', 'القروي', 'اليحياوي', 'فرحات',
             'رزڨي', 'الحاج', 'الحمروني', 'أمين', 'ماهر', 'التواتي', 'الفوراتي', 'أيمن', 'عامر', 'حسين', 'المناعي',
             'عمارة',
             'بوبكر', 'العوني', 'شقرون', 'الكوكي', 'حسني', 'بن يوسف', 'غربال', 'بن أحمد ', 'المسعودي', 'الجريبي',
             'الجربي', 'البوعزيزي', 'بن رمضان', 'بن سعيد', 'اللواتي', 'الخميري', 'الحاجي', 'عباس', 'الصالحي', 'عاشور',
             'فرجاني', 'سلامة', 'محجوب', 'بن عياد', 'الميساوي', 'البوزيدي', 'سعيد', 'الحناشي', 'مرابط', 'بلڨاسم',
             'حسين', 'الزريبي', 'داود',
             'حبيب', 'المدب', 'كمون', 'الذوادي', 'الفقيه', 'عاطية', 'بسباس', 'البرهومي', 'بن منصور', 'النوري',
             'المحمدي', 'صالح', 'الفخفاخ', 'الشعري', 'الحاج', 'الزواوي', 'الصيد', 'الشرفي', 'يوسف', 'سليم', 'مالك',
             'الشارني', 'السلطاني', 'شاوش', 'صابر', 'مراد', 'الكافي', 'البكوش', 'مبارك', 'بن إبراهيم', 'الخليفي',
             'الرباعي', 'الربعي', 'اللومي', 'حمودة',
             'الخفيفي', 'العياشي', 'زروق', 'دمق', 'موسى', 'المهيري', 'رمضان', 'حشيشة', 'الحجري', 'فريخة', 'بوراوي',
             'ثابت', 'الورتاني', 'معالى', 'خالد', 'خليفة', 'ناجي', 'الخياري', 'المزوغي', 'المولهي', 'الجوادي',
             'الڨاسمي', 'البراهمي', 'بن عمارة', 'شعيب', 'البكلوطي', 'الجلاصي', 'الجماعي', 'دربال', 'مقني', 'اللوز',
             'الجندوبي',
             'الزيتوني', 'بن محمد', 'السنوسي', 'الڨابسي', 'السعداوي', 'بوخريص', 'البوزيدي', 'النفزي', 'الجزيري', 'وليد',
             'ذويب', 'العباسي', 'الخراط', 'سيالة']
    file_list = [lakab]
    exported = zip_longest(*file_list)
    with open("last_name.csv", "w", encoding="utf-8") as file:
        wr = csv.writer(file)
        wr.writerow(["اللقب"])
        wr.writerows(exported)

##################################### SCRAPPING JOB NAME ###############################################################

def scrapping_jobs_ara():
    import requests
    from bs4 import BeautifulSoup
    import csv
    from itertools import zip_longest
    resultJob = requests.get("https://www.apprendrelefrancais1.com/2020/11/les-metiers.html")
    resultJob1 = requests.get("https://www.kaaed.com/2015/07/ci-cu.html")
    src3 = resultJob.content
    src4= resultJob1.content
    soup3 = BeautifulSoup(src3, "lxml")
    soup4 = BeautifulSoup(src4, "lxml")
    travail = soup3.find_all("b")
    travail2 = soup4.find_all("td")
    t = travail[7:-5]
    t2 = travail2[2:]

    word = []
    for st in t:
        w = st.text
        if '-' in w:
            ind = w.index('-')
            word.append(w[:ind - 1])
    for i in range(len(t2)):
        if i % 2 == 0:
            w2 = t2[i].text
            word.append(w2)
    for i in range(len(word)):
        word[i] = word[i].replace("/", "").strip()
        word[i] = word[i].replace(")", "")

    file_list = [word]
    exported = zip_longest(*file_list)
    with open("job_name.csv", "w", encoding="utf-8") as file:
        wr = csv.writer(file)
        wr.writerow(["المهنة"])
        wr.writerows(exported)


######################################## COMPILATION TO CREATE FILES DATA ##############################################


scrapping_first_name_ara()
scrapping_last_name_ara()
scrapping_jobs_ara()