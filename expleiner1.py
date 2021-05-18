# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:58:17 2021

@author: EL-RAY2
"""
import pandas as pd 
import xml.etree.ElementTree as ET


tag_names = ['title','seo_meta_description','source_id','developer_name']

tree1 = ET.parse('969140360237.explainer.xml')
root = tree1.getroot()
colmn1 = []
for child in root:
    if (child.tag in tag_names):
        colmn1.append(child.text)

tree2 = ET.parse('972198025105.explainer.xml')
root = tree2.getroot()
colmn2 = []
for child in root:
    if (child.tag in tag_names):
        colmn2.append(child.text)
        
tree3 = ET.parse('973130769145.explainer.xml')
root = tree3.getroot()
colmn3 = []
for child in root:
    if (child.tag in tag_names):
        colmn3.append(child.text)
        
tree4 = ET.parse('973145156531.explainer.xml')
root = tree4.getroot()
colmn4 = []
for child in root:
    if (child.tag in tag_names):
        colmn4.append(child.text)
        
tree5 = ET.parse('974125905106.explainer.xml')
root = tree5.getroot()
colmn5 = []
for child in root:
    if (child.tag in tag_names):
        colmn5.append(child.text)

tree6 = ET.parse('979165921053.explainer.xml')
root = tree6.getroot()
colmn6 = []
for child in root:
    if (child.tag in tag_names):
        colmn6.append(child.text)

tree7 = ET.parse('980162532502.explainer.xml')
root = tree7.getroot()
colmn7 = []
for child in root:
    if (child.tag in tag_names):
        colmn7.append(child.text)

tree8 = ET.parse('985161036067.explainer.xml')
root = tree8.getroot()
colmn8 = []
for child in root:
    if (child.tag in tag_names):
        colmn8.append(child.text)

tree9 = ET.parse('985195836913.explainer.xml')
root = tree9.getroot()
colmn9 = []
for child in root:
    if (child.tag in tag_names):
        colmn9.append(child.text)

tree0 = ET.parse('989130863985.explainer.xml')
root = tree0.getroot()
colmn0 = []
for child in root:
    if (child.tag in tag_names):
        colmn0.append(child.text)
        


data = [colmn1 , colmn2 ,colmn3 , colmn4 , colmn5 ,colmn6, colmn7, colmn8 , colmn9 , colmn0]
df = pd.DataFrame(data)
df.columns = tag_names



df.to_csv('output.csv')
