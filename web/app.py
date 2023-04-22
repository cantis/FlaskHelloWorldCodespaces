from flask import Flask

@app.route('/')
def index ():
    '''Index page'''
    return("Hello World")
