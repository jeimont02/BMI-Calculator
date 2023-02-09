#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:43:20 2023

@author: jacobeimont
"""

def calculate_bmi(height, weight):
    bmi = (weight / (height**2)) * 703
    return bmi

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = calculate_bmi(height, weight)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

