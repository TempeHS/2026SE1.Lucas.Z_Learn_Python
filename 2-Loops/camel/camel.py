camel=input("camel?")
snake=""
for let in camel:
    if let.isupper():
        snake+="_"+let.lower()
    else:
        snake+=let
if snake.startswith("_"):
    snake=snake[1:]
print(snake)