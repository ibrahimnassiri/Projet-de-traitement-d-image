import download as dw
import process as pr
import analyze as az
import argparse 
import os 
import numpy as np

parser = argparse.ArgumentParser(description="Traite les fichiers CSV et calcule le périmètre et la surface.")
parser.add_argument("-i", "--input_dir", type=str, required=True, help="Dossier contenant les fichiers à traiter")
parser.add_argument("-o", "--output_dir", type=str, required=True, help="Dossier où les fichiers de sortie seront enregistrés")


args = parser.parse_args()

    
   
    
    
   #runfile('M:/python/PROJET_PYTHON/data/mainb.py', wdir='M:/python/PROJET_PYTHON/data',args="-i M:/python/PROJET_PYTHON/data -o output" ) 

    


if __name__ == "__main__":
   
    
     
    limages, ldonnees,  list_image_name = dw.getfile(args.input_dir)

    
    
    for i, (image, donnee, image_name) in enumerate(zip(limages, ldonnees, list_image_name)):
        
        
        lm2x=[]
        lm2y=[]
        lm3x=[]
        lm3y=[]
        lm4x=[]
        lm4y=[]
        
        
        
        
        X, Y, Major, Minor, Angle = pr.bulles(image, donnee, image_name) 
        
        #az.analyze(donnee, args.output_dir, image_name)
        
        lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight = pr.roi(X, Y, Major, Minor, Angle)
        
        pr.rectangle(image, lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight)
        
        for xtopleft, ytopleft, xbottomright, ybottomright in zip(lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight):
              a = (xbottomright - xtopleft) / 2
              b = (ybottomright - ytopleft) / 2
        
              m2x = (np.pi / 4) * a * b**3
              m2y = (np.pi / 4) * a**3 * b
              m3x = (np.pi / 8) * a**2 * b**3
              m3y = (np.pi / 8) * a**3 * b**2
              m4x = (3 * np.pi / 16) * a**3 * b**3
              m4y = (3 * np.pi / 16) * a**3 * b**3
              
              
              lm2x.append(m2x)
              lm2y.append(m2y)
              lm3x.append(m3x)
              lm3y.append(m3y)
              lm4x.append(m4x)
              lm4y.append(m4y)
              
              
          
        
        az.analyze_moments(donnee, args.output_dir, image_name, lm2x, lm2y, lm3x, lm3y, lm4x, lm4y)        
    
    #runfile('M:/PROJET_BULLES/student/data/main.py', wdir='M:/PROJET_BULLES/student/data',args="-i M:/PROJET_BULLES/student/data -o output")