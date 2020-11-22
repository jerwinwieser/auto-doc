import pandas as pd
import csv
import json
import os
from shutil import copyfile

df = pd.read_csv('applications.csv')

companies_dates = df[['companynameshort', 'letterdate']]

companies_dates_combined = companies_dates.apply(lambda x: ' '.join(x), axis=1)
var = [x.replace(' ', '_').replace('/', '-') for x in companies_dates_combined]

def write_data(i):

    dirname = var[i]

    base = dirname + '/'
    newline = '\n'

    if not os.path.exists('apply' + '/' + dirname):
        os.makedirs('apply' + '/' + dirname)
        copyfile('templ/letter.tex', 'apply' + '/' + base + 'letter.tex')
        copyfile('templ/body.txt', 'apply' + '/' + base + 'body.txt')
        copyfile('templ/message.txt', 'apply' + '/' + base + 'message.txt')

        obj = df.iloc[i]
        f = open('apply' + '/' + base + 'vars.txt', 'w')

        f.write('\\newcommand{\letterdate}' + '{' + obj.letterdate + '}' + newline)
        f.write('\\newcommand{\sendername}' + '{' + obj.sendername + '}' + newline)
        f.write('\\newcommand{\sendertitle}' + '{' + obj.sendertitle + '}' + newline)
        f.write('\\newcommand{\senderstreet}' + '{' + obj.senderstreet + '}' + newline)
        f.write('\\newcommand{\senderpostal}' + '{' + obj.senderpostal + '}' + newline)
        f.write('\\newcommand{\sendercity}' + '{' + obj.sendercity + '}' + newline)
        f.write('\\newcommand{\sendercountry}' + '{' + obj.sendercountry + '}' + newline)
        f.write('\\newcommand{\senderemail}' + '{' + obj.senderemail + '}' + newline)
        f.write('\\newcommand{\senderphone}' + '{' + str(obj.senderphone) + '}' + newline)
        f.write('\\newcommand{\jobopening}' + '{' + obj.jobopening + '}' + newline)
        f.write('\\newcommand{\jobfield}' + '{' + obj.jobfield + '}' + newline)
        f.write('\\newcommand{\companynameperson}' + '{' + obj.companynameperson + '}' + newline)
        f.write('\\newcommand{\companynamepersontitle}' + '{' + obj.companynamepersontitle + '}' + newline)
        f.write('\\newcommand{\companyname}' + '{' + obj.companyname + '}' + newline)
        f.write('\\newcommand{\companynameshort}' + '{' + obj.companynameshort + '}' + newline)
        f.write('\\newcommand{\companydepartment}' + '{' + obj.companydepartment + '}' + newline)
        f.write('\\newcommand{\companystreet}' + '{' + obj.companystreet + '}' + newline)
        f.write('\\newcommand{\companypostal}' + '{' + obj.companypostal + '}' + newline)
        f.write('\\newcommand{\companycity}' + '{' + obj.companycity + '}' + newline)
        f.write('\\newcommand{\companyemail}' + '{' + obj.companyemail + '}' + newline)
        f.write('\\newcommand{\sourcevacancy}' + '{' + obj.sourcevacancy + '}' + newline)

        f.close()

        name = open('apply' + '/' + base + 'name.txt', 'w') 
        name.write(obj.companynameperson)
        name.close()

        email = open('apply' + '/' + base + 'email.txt', 'w') 
        email.write(obj.companyemail)
        email.close()

for index, row in df.iterrows():
    write_data(i = index)

       
