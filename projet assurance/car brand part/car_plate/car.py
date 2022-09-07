def car_plate(image):
    import cv2
    import numpy as np
    import imutils
    import easyocr
    img=cv2.imread(image)
    resized = cv2.resize(img, (800,700), interpolation = cv2.INTER_AREA)
    gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
    bfilter=cv2.bilateralFilter(gray,11,17,17)
    edged=cv2.Canny(bfilter,30,200)
    keypoints=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(keypoints)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)[:10]
    location=None
    for contour in contours:
        approx=cv2.approxPolyDP(contour,10,True)
        if len(approx)==4:
            location=approx
            break
    mask=np.zeros(gray.shape,np.uint8)
    try:
        new_image=cv2.drawContours(mask,[location],0,255,-1)
        new_image=cv2.bitwise_and(resized,resized,mask=mask)
        (x,y)=np.where(mask==255)
        (x1,y1)=(np.min(x),np.min(y))
        (x2,y2)=(np.max(x),np.max(y))
        cropped_image=gray[x1-10:x2+20,y1-10:y2+20]
    except:
        return "verifier manuellement !!"
    reader=easyocr.Reader(['ar'])
    result=reader.readtext(cropped_image)
    try:
        text=result[0][-2]
    except:
        return "verifier manuellement!!"
    x = text.split()
    x_new=[]
    for word in x :
        for char in word:
            if char not in ['.','/','?','!']:
                x_new.append(char)
    word=''
    for ch in x_new:
        if ch  in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            word += ch
        else:
            word+=' '
    x_new=word.split()
    count=0
    car_mat=''
    for c in x_new:
        if count ==1:
            car_mat+=' تونس '
        car_mat+=c
        count += 1
    return car_mat





print(car_plate('mama.jpg'))
print(car_plate('pgt.jpg'))
print(car_plate('pgt_arr.jpg'))
print(car_plate('merc.jpg'))
print(car_plate('audi.jpg'))









