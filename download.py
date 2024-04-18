import cv2
import pandas as pd
import os



def getfile(input_dir):

    limages = []
    ldonnees = []
    list_image_name = []
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.tiff'):
            tiff_file = os.path.join(input_dir, filename)
            image = cv2.imread(tiff_file, cv2.IMREAD_GRAYSCALE)
            limages.append(image)
            basename = os.path.splitext(filename)[0]
            list_image_name.append(basename)
            
            
        elif filename.endswith('.csv'):
            csv_file = os.path.join(input_dir, filename)
            donnees = pd.read_csv(csv_file, sep=";", encoding="windows-1252")
            ldonnees.append(donnees)
            
    return limages, ldonnees, list_image_name



    
