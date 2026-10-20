import matplotlib.pyplot as plt
weights=[2.5,3.0,4.5,5.0,6.5,7.0,8.0,9.5]
height=[20,22,25,27,40,42,45,48]
labels=["Cat","Cat","Cat","Cat","Dog","Dog","Dog","Dog"]
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
        dog_height.append(h)
        dog_weigths.append(w)
cat_average_weight=sum(cat_weigths)/len(cat_weigths)
cat_average_height=sum(cat_height)/len(cat_height)
dog_average_weight=sum(dog_weigths)/len(dog_weigths)
dog_average_height=sum(dog_height)/len(dog_height)
print(f"Average weight of cat:{sum(cat_weigths)/len(cat_weigths)},kg")
print(f"Average height of cat:{sum(cat_height)/len(cat_height)},cm")
print(f"Average weight of dog:{sum(dog_weigths)/len(dog_weigths)},kg")
print(f"Average height of dog:{sum(dog_height)/len(dog_height)},cm")
def AI_classifier(weights,height):
    distance_to_cat=abs(weights-cat_average_weight)+abs(height-cat_average_height)
    distance_to_dog=abs(weights-dog_average_weight)+abs(height-dog_average_height)
    if distance_to_cat<distance_to_dog:
        return "cat"
    else:
        return "dog"
new_animals=[(5.2,29),(3.5,57),(5.7,67)]
for w,h in new_animals:
    rule=rulebasedclassifier(w,h)
    Ai=AI_classifier(w,h)
    print(f"{w} kg,{h} cm-> rule says {rule} Ai says {Ai}")
plt.figure(figsize=(6,5))
colors=["orange" if l=="Cat" else "Blue" for l in labels]
plt.scatter(weights,height,c=colors,s=80,label="Training Data")
for w,h in new_animals:
    plt.scatter(w,h,c="red",marker="x",s=100)
plt.xlabel("weights")
plt.ylabel("heights")
plt.show()