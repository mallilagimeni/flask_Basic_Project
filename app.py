from flask import Flask
OB=Flask(__name__)
@OB.route('/Arjun')
def Arjun():
    return 'Arjun Malli'
@OB.route('/malli')
def malli():
    return 'Yadav'

OB.run()