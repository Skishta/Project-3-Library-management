                    #PROJECT 3 (LIBERARIES)
#المشروع عبارة عن مكتبة مكونة من 3 ادوار مكتبية
#مسجل فيها كتاب احصاء (للتجربة علية)
#كل كتاب لة مجموعة من البيانات(اسم المولف, تاريخ الاصدار,مكان التخزين)
#هنطلب من اليوزر 3 حاجات:
#هل تريد تخزين كتاب(وهطلب منة البيانات للكتاب)؟ هل تريد رؤية الكتب الموجودة بالمكتبة؟ هل تريد رؤية تفاصيل معينة حول كتاب معين؟
#اول حاجة هعمل list طبعا بالادوار اللى هيتم تسجيل الكتاب بداخلها
floor=("firstfloor","secondfloor","thirdfloor")
#هنسجل كتاب إحصاء وهخزنة فى الدور الاول : الindex 0 
books={"stat":{"auther":"ahmed","issuedate":"1999","stored":floor[0]}}
#تعالوا نتاكد ان الكتاب تم تسجيلة(هطلب كل كتب المكتبة)
books
#طيب تعالوا نتاكد ان كتاب الstat تم تسجيل بياناتة بشكل صحيح(هطلب كتاب الstat) بس
books["stat"]
#طيب دلوقتى تعالى نتاكد من بيانات داخل كتاب الstat (هطلب مثلا الauther) بس
books["stat"]["auther"]
#طيب دلوقتى انا عايز اعمل list ل function اعرف اخزن فيها الكتب الجديدة من المستخدم
#يعنى هنعمل function ب addnew وبعدين هطلب من اليوزر انة يدخل ليا نفس التفاصيل (ك list) لكتاب الاحصاء(اسم المولف,تاريخ الاصدار, مكان تخزينة)
#هنعمل function وهخليها list بتحتوى على اسم الكتاب واسم المؤلف وتاريخ الاصدار والتخزين
def addnew(book_name,auther_name,issue,store):
#دلوقتى محتاج اضيف فى اخر الlist بتاعة books الكتب الجديد
#هنعملها ب setdefault عشان اعرف اضيف فى اخر الlist قايمة للكتاب الجديد الbook_name
#لكل list بداخلها key:value ..الkey هيا الbook_name الvalue فاضية
    books.setdefault(book_name,{})
#بعد ما عملت list اسمها book_name عايز "أضيف" جواها list ب(اسم الكتاب,اسم المؤلف,تاريخ الاصدار,التخزين)
#هنا انا عايز اليوزر يدخل على الvalue (للكتاب اللى تم ادخالة) اسم المؤلف,تاريخ الاصدار,مكان التخزين
    books[book_name].setdefault("auther",auther_name)
    books[book_name].setdefault("issuedate",issue)
#دلوقتى هوة بيشتغل ازاى ؟
#بقولة book.setdfault : اعملة list اسمها books وخد بالك هضيف على الlist دى key اسمها book_name الvalue بتاعها هتكون list وبعدين قولتلة الlist books اللى الkey بتاعها book_name ضيف value مثلا اسمها auther وجوة الauther هتضيف auther_name 
#طيب لما اليوزر يدخل ليا رقم ازاى اعرف اخزنة ك index داخل الfirst or second or third floor
#بدل ما اقولة انت عندك vlaue اسمة store خزن جواه عالطول..لا هقولة انت عندك متغير (معرف مسبقا) اسمة floor وافتحلة قوس مربع (عشان يفهم ان التخزين جواه هيكون index) وبعدها هقولة اى رقم يدخل ل store سجلة ك index جوة floor
    books[book_name].setdefault("stored",floor[store])
'''
#طيب دلوقتى انا عايز اليوزر يدخل بقى فى المكتبة الكتب بتاعتة بتفاصيلها
book_name=input("plz enter the book name: ")
auther_name=input("plz enter the auther's name: ")
issue=input("plz enter the issue date : ")
store=int(input("plz enter the where to store: "))
#ولازم اعمل call للfunction  فى الاخر عشان يتم تخزينها فى الlist
addnew(book_name,auther_name,issue,store)
'''
#بس طبعا احنا مش عايزين نعمل كدة احنا عايزين نعمل الاتى: 
#دلوقتى هنتكلم مع اليوزر واقعد اسالة لو عايز تضيف كتاب اكتب نعم او لا او لو عايز تعرف تفاصيلة اكتب نعم او لا وهكذا 
#خلينا الtrue==true عشان يدخل فى كل الحالات داخل الloop 
while True==True:
#بسال اليوزر انت عايز تضيف كتاب اكتب Y OR NO
    need=input("do U want to add a new book,plz enter'Y' OR 'NO': ")
 #لو كتب Y هيدخل جوة الloop دة
    if need=="Y":
        book_name=input("plz enter the book name: ")
        auther_name=input("plz enter the auther name: ")
        issue=input("plz enter the issue date: ")
        store=int(input("plz enter where you want to store in which foor: "))
        addnew(book_name,auther_name,issue,store)
#لو كتب NO هيدخل جوة الloop دة
    elif need=="NO":
#وساعتها هسالة بقى طب انت عايز تشوف الكتب الموجودة
        need1=input("Do U want to see books listed,Plz enter 'Y' OR 'NO': ")
#لو كتب Y هيدخل جوة الloop دة
        if need1=="Y":
#وهقول للcompiler اطبعلى الlist بتاعة الbooks كلها
            print(books)
#لو كتب اى حاجة غير Y هيدخل جوة الloop دة
        else:
#وساعتها هسالة انت عايز طيب تعرف تفاصيل عن كتاب معين: اكتب Y OR NO
            need2=input("Do U want a specefic info about certain book,Plz enter 'Y' OR 'NO': ")
#لو كتب Y هيدخل جوة الloop دة
            if need2=="Y":
#وساعتها هسالة انت عايز تعرف تفاصيل عن كتاب اسمة اية
                nameoofthebook=input("Plz enter the name of the book: ")
#هنا بقول للكومبيلر خش جوة الlist وهات اسم الكتاب بامر .get ..بس لو اسم الكتاب لاقيتة مش موجود وظهر ليك(بكلم الكومبيلر) none اطبع لليوزر (اتاكد من اسم الكتاب تانى)
                if books.get(nameoofthebook)==None:
                   print("plz chech UR Name") 
#وبقول للكومبيلر اى حاجة غير كدة (يعنى لو لاقيت الكتاب جوة الlist) ..فاطبع الكتاب من الlist بتاعة الbooks 
                else:
                    print(books.get(nameoofthebook))
#غير كدة اطلع من الloop
    else:
        break