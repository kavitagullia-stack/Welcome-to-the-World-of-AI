import matplotlib.pyplot as plt
weights=[2.5,3.0,4.5,5.0,6.5,7.0,8.0,9.5]
height=[20,22,25,27,40,42,45,48]
labels=["Cat","Cat","Dog","Dog","Cat","Cat","Dog","Dog"]
for w,h,l in zip(weights,height,labels):
    print(f"{w} kg,{h} cm,{l}")
def rulebasedclassifier(weights,height):
    if weights<5 and height<30:
        return "cat"
    else:
        return "dog"
print(rulebasedclassifier(weights=4.5,height=30))
print(rulebasedclassifier(weights=3.5,height=45))
cat_weigths=[]
cat_height=[]
dog_weigths=[]
dog_height=[]
for w,h,label in zip(weights,height,labels):
    print(label)
    if label=="Cat":
        cat_weigths.append(w)
        cat_height.append(h)
    else:
        dog_height.append(w)
        dog_weigths.append(h)
print(f"Average weight of cat:{sum(cat_weigths)/len(cat_weigths)},kg")
print(f"Average height of cat:{sum(cat_height)/len(cat_height)},cm")
print(f"Average weight of dog:{sum(dog_weigths)/len(dog_weigths)},kg")
print(f"Average height of dog:{sum(dog_height)/len(dog_height)},cm")
