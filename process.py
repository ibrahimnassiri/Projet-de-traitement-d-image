
import matplotlib.pyplot as plt
import cv2
import numpy as np



   
def bulles(image, donnee, image_name):
    


    
        # Extraire les colonnes X, Y, Major, Minor et Angle
    X = donnee["X"].to_numpy().astype(int)
    Y = donnee["Y"].to_numpy().astype(int)
    Major = donnee["Major"].to_numpy().astype(int)
    Minor = donnee["Minor"].to_numpy().astype(int)
    Angle = donnee["Angle"].to_numpy()


        # Ajouter des ellipses à l'image
    for x, y, major, minor, angle in zip(X, Y, Major, Minor, Angle):
            cv2.ellipse(image, (x, y), (int(major/2.0), int(minor/2.0)), -angle, 0, 360, 0, 1)

        # Afficher l'image
    plt.figure(f"{image_name}")
    plt.imshow(image, cmap="gray")
    plt.show()

    return X,Y,Major,Minor,Angle


        

def roi(Xmean,Ymean,Major,Minor,Angle):
    # This function computes a bounding box around an ellipe
    # The bounding box is a rectangle with sides parallel to the x and y axis    
    lxTopLeft = []
    lyTopLeft = []
    lxBottomRight = []
    lyBottomRight = []

    for xm, ym, major, minor, angle in zip(Xmean, Ymean, Major, Minor, Angle):
        major = major/2
        minor = minor/2
        angle = angle * np.pi/180
        lx = [] 
        ly = [] 
        lx.append(xm + major*np.cos(angle))
        lx.append(xm - major*np.cos(angle))
        lx.append(xm + minor*np.cos(angle))
        lx.append(xm - minor*np.cos(angle))
        ly.append(ym + major*np.sin(angle))
        ly.append(ym - major*np.sin(angle))
        ly.append(ym + minor*np.cos(angle))
        ly.append(ym - minor*np.cos(angle))
        
        xTopLeft = min(lx)
        yTopLeft = min(ly)
        xBottomRight = max(lx)
        yBottomRight = max(ly)
        lxTopLeft.append(xTopLeft)
        lyTopLeft.append(yTopLeft)
        lxBottomRight.append(xBottomRight)
        lyBottomRight.append(yBottomRight)

    return lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight
        
        
def rectangle(image, lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight, color=(0, 255, 0), thickness=1):

        img = image.copy()
        
        # Draw rectangles on the image
        for xtopleft, ytopleft, xbottomright, ybottomright in zip(lxTopLeft, lyTopLeft, lxBottomRight, lyBottomRight):
            pt1 = (int(xtopleft), int(ytopleft))
            pt2 = (int(xbottomright), int(ybottomright))
            img = cv2.rectangle(img, pt1, pt2, color, thickness)
        
        # Display the image with the rectangles
        plt.figure(figsize=(8, 6))
        plt.imshow(img, cmap="gray")
        plt.title(f"Image {1} with Rectangles")
        plt.axis("off")
        plt.show()

        
        







        
        



 
