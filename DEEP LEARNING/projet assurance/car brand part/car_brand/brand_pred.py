model_path='car_brand/carBrand_model.h5'
image_path1='car_brand/Acura_NSX.jpg'
image_path2='car_brand/Acura_ILX.jpg'
image_path3='car_brand/Acura_MDX.jpg'
image_path4='car_brand/Aston Martin_Vanquish.jpg'
image_path5='car_brand/Audi_TT.jpg'
image_path6='car_brand/Alfa Romeo_Giulia.jpg'
image_path7='car_brand/Audi_A6.jpg'
image_path8='car_brand/Audi_Q5.jpg'
image_path9='car_brand/Audi_e-tron.jpg'
image_path10='car_brand/Aston Martin_DBS.jpg'
brand_name='car_brand/brand_name.csv'
def pred_car_brand(model_path,image_path,brand_name):
    from tensorflow.keras.models import load_model
    import cv2
    import numpy as np

    model=load_model(model_path)
    img1=cv2.imread(image_path)
    resized_img1=cv2.resize(img1,(100,100))
    y_pred_1=model.predict(resized_img1[None,...])
    y_pred_1_classe=np.argmax(y_pred_1)
    data = open(brand_name, encoding="utf8").read()
    corpus = data.split("\n")
    for i in corpus:
        if i == "":
            corpus.remove('')
    corpus = corpus[1:-1]
    return corpus[y_pred_1_classe]
print(pred_car_brand(model_path,image_path1,brand_name))
print(pred_car_brand(model_path,image_path2,brand_name))
print(pred_car_brand(model_path,image_path3,brand_name))
print(pred_car_brand(model_path,image_path4,brand_name))
print(pred_car_brand(model_path,image_path5,brand_name))
print(pred_car_brand(model_path,image_path6,brand_name))
print(pred_car_brand(model_path,image_path7,brand_name))
print(pred_car_brand(model_path,image_path8,brand_name))
print(pred_car_brand(model_path,image_path9,brand_name))
print(pred_car_brand(model_path,image_path10,brand_name))
