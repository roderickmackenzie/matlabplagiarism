# matlabplagiarism
MATLAB plagiarism detector in python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every year I have to mark around 600 coursework assignments. Sometime students hand in identical code.  To find out if the students are cheating I wrote this python script.  This is not really a nicely presented program so you may have to hack it about to get it to work. To use it:
* place the students work in zip files in a directory called orig.
* run removespace.sh a couple of times to remove spaces from the file names.
* Make a directory called extracted
* run ./extract.sh to extract extract all the zip/rar files from orig to extracted
* Run removespace.sh a couple of times again to make sure there are no spaces in the file names.
* run cmp.py to do the comparison.
* Look in the directory out to see what it finds.

Rod MacKenzie 2015
