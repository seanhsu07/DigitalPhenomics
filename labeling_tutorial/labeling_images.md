Labeling Tutorial

The labeling tool chosen for this project is the VGG Image Annotator (http://www.robots.ox.ac.uk/~vgg/software/via/). 

To label the images, go to the webpage listed above go to downloads / Version 2 _ Image Annotator/ via.html. 

![alt text](https://github.com/seanhsu07/DigitalPhenomics/blob/master/labeling_tutorial/VGG_WP.JPG)

In the UI, go to project and upload the image files to be annotated. 
  To configure the attributes, enter the name of the attribute and press the + symbol on the right. Select checkbox for type and enter the id and description (optional) of the option. 
  Now that the label is configured, go back to the image and select polyline for attributes and label the mask over the region of interest, an area should appear on the area you selected. Click on the options to confirm that the classification of selected region. 

![alt text](https://github.com/seanhsu07/DigitalPhenomics/blob/master/labeling_tutorial/VGG_UI.JPG)

After finishing the labeling process of all images, select the annotation button on top of the screen and select "export annotations as json". The webpage will output a json file recording the file name, size, attributes, region count, and region location. 
