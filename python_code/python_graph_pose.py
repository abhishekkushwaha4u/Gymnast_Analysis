import numpy as np
import cv2
# import matplotlib.pyplot as plt


protofile_path = "models\pose\mpi\pose_deploy_linevec_faster_4_stages.prototxt"          # Paste server path
weights_path = "models\pose\mpi\pose_iter_160000.caffemodel"   # Paste server path
image_path = "data\images\im00001.jpg"                 # Paste the image_analysis path
nPoints = 15
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ] # Pair models as given


def get_image_graph(protofile_path, weights_path, im, nPoints, POSE_PAIRS):
    net = cv2.dnn.readNetFromCaffe(protofile_path, weights_path)
    
    # im = cv2.imread(image_path)
    # if():

    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    
    inWidth = im.shape[1]
    inHeight = im.shape[0]

    netInputSize = (368, 368)
    inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB=True, crop=False)
    net.setInput(inpBlob)

    output = net.forward()

    scaleX = inWidth / output.shape[3]
    scaleY = inHeight / output.shape[2]

    points = []
    threshold = 0.1

    for i in range(nPoints):
        # Obtain probability map
        probMap = output[0, i, :, :]
        
        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image
        x = scaleX * point[0]
        y = scaleY * point[1]

        if prob > threshold : 
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)
    
    # print(points)

    imPoints = im.copy()
    imSkeleton = im.copy()

    for i, p in enumerate(points):
        cv2.circle(imPoints, p, 2, (255, 255,0), thickness=-1, lineType=cv2.FILLED)
        # cv2.putText(imPoints, "{}".format(i), p, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, lineType=cv2.LINE_AA)
    # plt.imshow(imPoints)

    # Draw skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(imSkeleton, points[partA], points[partB], (255, 255,0), 2)
            cv2.circle(imSkeleton, points[partA], 2, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)
    
    try:
        i = 0
        cv2.imwrite("img_pts" + i + ".png",imPoints)
        cv2.imwrite("img_skeleton" + i + ".png",imSkeleton)
        i += 1
        return(0, points)

    except Exception as e:
        return (1, points)

ret, points = get_image_graph(protofile_path, weights_path, image_path, nPoints, POSE_PAIRS)



