FC={"apple":"150","avacado":'50','banana':'110','cantaloupe':'50','grapefuit':'60','grapes':'90','honeydew melon':'50',
'kiwifruit':'90','lemon':'15','lime':'20','nectarine':'60','orange':'80','peach':'60','pear':'100','pineapple':'50',
'plum':'70','strawberry':'50','sweetcherries':'100','tangerine':'50','watermelon':'80'}
Fruit = input("what fruit?")
for i in FC:
    if i == Fruit:
        print(FC[i])