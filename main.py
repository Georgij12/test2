# from flask import Flask
# import random
# app=Flask(__name__)
#
# number=random.randint(0,9)
# print(number)
#
# @app.route('/')
# def home():
#     return "<h1>Guess a    number between 0 and 9</h1>" \
#            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
#
# @app.route('/<int:guess>')
# def guess_number(guess):
#     if guess > number:
#         return "<h1> Too high. Try again! </h1>" \
#                "<img src='https://thumbs.gfycat.com/MagnificentExaltedDogwoodtwigborer-size_restricted.gif' >"
#     elif guess < number:
#         return "<h1>Too low try again </h1>"\
#                "<img src='https://giphy.com/embed/y31rRE5h3wyPXey8vx'>"
#
# if __name__== "__main__":
#     app.run(debug=True)


