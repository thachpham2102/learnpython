def ve():
    import random
    dic_v_e = {'uốn đất':'earthbending',
               'đang diễn ra':'ongoing',
               'thô':'raw',
               'kim loại':'metal',
               'đường hầm':'tunnel',
               'điều hướng':'navigate',
               'tù nhân':'prisoner',
               'tài sản':'asset',
               'thừa kế':'inherited',
               'liên kết':'bonding'
               }
    word=random.choice(list(dic_v_e.keys()))
    print('Hãy nhập nghĩa của từ sau:✍️✍️✍️',word)
    Eng = str(input('Đáp án của bạn là : '))
    if Eng==(dic_v_e[word]):
        print('Bạn đã trả lời đúng  👍 ')
    else:
        print('Bạn đã trả lòi sai👎,vui lòng hãy học lại📚📚📚 ')
def ev():
    import random
    dic_e_v = {'earthbending':'uon đat',
               'ongoing':'dang dien ra',
               'raw':'tho',
               'metal':'kim loai',
               'tunnel':'đuong ham',
               'navigate':'đieu huong',
               'prisoner':'tu nhan',
               'asset':'tai san',
               'inherited':'thua ke',
               'bonding':'lien ket'
               }
    word=random.choice(list(dic_e_v.keys()))
    print('Hãy nhập nghĩa của từ sau(vui lòng viết không dấu):✍️✍️✍️',word)
    Eng = str(input('Đáp án của bạn là : '))
    if Eng==(dic_e_v[word]):
        print('Bạn đã trả lời đúng  👍 ')
    else:
        print('Bạn đã trả lòi sai👎,vui lòng hãy học lại📚📚📚 ')
def menu():
    print('__________')
    print('this is a super dictionary of pro coder gon')
    print('this app has two kinds of dictionary')
    print("")
    print('1.vietnamese english')
    print('2.english vietnamese')
    print("")
#___________________________________________________
menu()
numwo = float(input('Please enter the number of the kind of dictionary:'))
if numwo==1:
    check1=1
    while check1:
        ve()
        check1=int(input("press 1 to continue /press 0 to exit  : "))
        
elif numwo==2:
    check2=1
    while check2:
        ev()
        check2=int(input("press 1 to continue /press 0 to exit  :"))
else:
    print('Goodbye')

if (check1==0)&(check2==0):
    print('Goodbye')
input('Nhấn Enter để thoát chương trình .')