hight=input('請輸入您的身高:')
weight=input('請輸入您的體重:')
hight=int(hight)
weight=int(weight)
hight=hight/100
bmi=weight/hight/hight
if bmi < 18.5:
    print('您的bmi值為:', bmi, '屬於過輕')
elif bmi >= 18.5 and bmi < 24:
    print('您的bmi值為:', bmi, '屬於正常')
elif bmi>=24 and bmi < 27: 
    print('您的bmi值為:', bmi, '屬於過重')
elif bmi>=27 and bmi < 30:
    print('您的bmi值為:', bmi, '屬於輕度肥胖')
elif bmi>=30 and bmi <35:
    print('您的bmi值為:', bmi, '屬於中度肥胖')    
elif bmi>=35:
    print('您的bmi值為:', bmi, '屬於重度肥胖')