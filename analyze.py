import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analyze(donnee, output_dir, image_name):
        
        
        if not os.path.exists(output_dir): 
            os.makedirs(output_dir)
    
        # Extraire les colonnes X, Y, Major, Minor et Angle
        
        X = donnee["X"].to_numpy().astype(int)
        Y = donnee["Y"].to_numpy().astype(int)
        Major = donnee["Major"].to_numpy().astype(int)
        Minor = donnee["Minor"].to_numpy().astype(int)
        Angle = donnee["Angle"].to_numpy()

        # Surface:
        S = np.pi * (Major / 2.0) * (Minor / 2.0)
        # Périmètre:
        P = 2 * np.pi * np.sqrt((Major ** 2 + Minor ** 2) / 2)

        # Créer un DataFrame pour stocker les résultats
        df = pd.DataFrame({'X': X, 'Y': Y, 'Major': Major, 'Minor': Minor, 'Angle': Angle, 'Périmètre': P.round(2), 'Surface': S.round(2)})
        
        # Sauvegarder le DataFrame au format CSV
        output_file = os.path.join(output_dir, f"{image_name}_out.csv")
        df.to_csv(output_file, sep=";", index=False)
        
        # Créer un histogramme et le sauvegarder en PDF
        plt.figure()
        plt.hist(S, bins=100)
        plt.title(f"Histogramme des surfaces {image_name}")
        plt.savefig(os.path.join(output_dir, f"{image_name}_hist.pdf"))
    
        

def analyze_moments(donnee, output_dir, image_name, lm2x, lm2y, lm3x, lm3y, lm4x, lm4y):
        
        
        if not os.path.exists(output_dir): 
            os.makedirs(output_dir)
    
        # Extraire les colonnes X, Y, Major, Minor et Angle
        N = donnee["n° bulle"].to_numpy()
        X = donnee["X"].to_numpy().astype(int)
        Y = donnee["Y"].to_numpy().astype(int)
        Major = donnee["Major"].to_numpy().astype(int)
        Minor = donnee["Minor"].to_numpy().astype(int)
        Angle = donnee["Angle"].to_numpy()

        # Surface:
        S = np.pi * (Major / 2.0) * (Minor / 2.0)
        # Périmètre:
        P = 2 * np.pi * np.sqrt((Major ** 2 + Minor ** 2) / 2)
        # moment d'ordre 2:
        #lm2x=[]
        #lm2y=[]
           
        #print(f"{m2x:.3f}, {m2y:.3f}")

        # Créer un DataFrame pour stocker les résultats
        # df = pd.DataFrame({'X': X, 'Y': Y, 'Major': Major, 'Minor': Minor, 'Angle': Angle, 'Périmètre': P.round(2), 'Surface': S.round(2), 'Moment ordre 2 pour x': lm2x, 'Moment ordre 2 pour y': lm2y}) 
        df = pd.DataFrame({'n° bulle': N, 'X': X, 'Y': Y, 'Major': Major, 'Minor': Minor, 'Angle': Angle, 'Périmètre': P.round(2), 'Surface': S.round(2), 'Moment ordre 2 pour x': [m2x.round(2) for m2x in lm2x], 'Moment ordre 2 pour y': [m2y.round(2) for m2y in lm2y], 'Moment ordre 3 pour x': [m3x.round(2) for m3x in lm3x], 'Moment ordre 3 pour y': [m3y.round(2) for m3y in lm3y], 'Moment ordre 4 pour x': [m4x.round(2) for m4x in lm4x], 'Moment ordre 4 pour y': [m4y.round(2) for m4y in lm4y]})
        #df['Moment d''ordre 2 pour x'] = lm2x
        #df['Moment d''ordre 2 pour y'] = lm2y

        # Sauvegarder le DataFrame au format CSV
        output_file = os.path.join(output_dir, f"{image_name}_out.csv")
        df.to_csv(output_file, sep=";", index=False)
        
        # Créer un histogramme et le sauvegarder en PDF
        plt.figure()
        plt.hist(S, bins=100)
        plt.title(f"Histogramme des surfaces {image_name}")
        plt.savefig(os.path.join(output_dir, f"{image_name}_hist.pdf"))






def moment_2(xTopLeft, yTopLeft, xBottomRight, yBottomRight):
    for xtopleft, ytopleft, xbottomright, ybottomright in zip(xTopLeft, yTopLeft, xBottomRight, yBottomRight):
          a = (xbottomright - xtopleft) / 2
          b = (ybottomright - ytopleft) / 2
    
          m2x = (np.pi / 4) * a * b**3
          m2y = (np.pi / 4) * a**3 * b
          print(f"{m2x:.3f}, {m2y:.3f}")
          #print (m2x , m2y);

    return m2x, m2y





def moment_3(xtopleft, ytopleft, xbottomright, ybottomright):
    a = (xbottomright - xtopleft) / 2
    b = (ybottomright - ytopleft) / 2
    
    m30 = (np.pi / 8) * a**2 * b**3
    m03 = (np.pi / 8) * a**3 * b**2
    
    
    return m30, m03

def moment_4(xtopleft, ytopleft, xbottomright, ybottomright):
    a = (xbottomright - xtopleft) / 2
    b = (ybottomright - ytopleft) / 2
    
    m40 = (3 * np.pi / 16) * a**3 * b**3
    m04 = (3 * np.pi / 16) * a**3 * b**3
   
    
    return m40, m04