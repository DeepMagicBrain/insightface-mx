
import sys
sys.path.append('../common')
import os
import face_image

input_dir = sys.argv[1]
out_path = sys.argv[2]
dataset = face_image.get_dataset_common(input_dir, 2)

out_file = open(out_path, 'w')
for item in dataset:
  print("%d\t%s\t%d" % (1, item.image_path, int(item.classname)))
  out_file.write("{}\t{}\t{}\n".format(1, item.image_path, item.classname)) 

out_file.close()
