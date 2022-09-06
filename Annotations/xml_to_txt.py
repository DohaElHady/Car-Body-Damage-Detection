import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=['train','val'] #sets of images in folders

classes = ['damage']

vott_export_path = 'Annotations-PascalVOC-export/'#path to vott folder from the script location

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open('%s/Annotations/%s.xml'%(vott_export_path,image_id))
    out_file = open('%s/labels/%s.txt'%(vott_export_path,image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for image_set in sets:
    if not os.path.exists('%s/labels/'%(vott_export_path)):
        os.makedirs('%s/labels/'%(vott_export_path))
    image_ids = open('%s/ImageSets/Main/%s_%s.txt'%(vott_export_path,classes[0],image_set)).read().strip().split("\n")
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        image_id=image_id.split(".",1)[0]
        list_file.write('%s/JPEGImages/%s.jpg\n'%(vott_export_path, image_id))
        convert_annotation(image_id)
    list_file.close()
