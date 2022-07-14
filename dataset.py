from tqdm import tqdm
from halo import Halo
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import json, os, time, shutil, glob, random, sys, cv2

class data_handler():
    
    def main(self):
        
        files = glob.glob("images/*.*")
        
        filename, extension = files[0].split(".")
        
        if (extension == "png") or (extension == "PNG"):
            
            print("Image type: 'PNG' (Portable Network Graphics).\r")
            self.do_png()
            
        elif (extension == "jpg") or (extension == "JPG"):
            
            print("Image type: 'JPG' (Joint Photographic Experts Group).\r")
            print("Processing images.\r")
            self.do_jpg(files)  
            
        else:
            
            print("No compatible image format found. Quitting.\r")
            sys.exit()
            
    def do_png(delf):
        
        '''
        Check dataset is even
        '''
        
        files = glob.glob("images/*.png")
        
        amt_files = len(files)
        
        test = amt_files % 2
        
        idx = random.choice([0, amt_files-1])
        
        if test != 0:
            
            file_name = files[idx]
            del files[idx]
            os.remove(file_name)
            
        '''
        Run resizer regardless
        '''
        
        for file in tqdm(files, desc = "Resizing"):
            
            image = Image.open(file)
            new_image = image.resize((800, 800))
            new_image.save(file)
                               
        '''
        
        Create Train, test and eval image sets
        
        '''
        
        end_2 = amt_files-1
        
        start_0 = 0
        
        end_0 = (int(end_2/2))+1
        
        start_1 = end_0
        
        end_1 = end_2+1
        
        os.mkdir("images_test")
        
        files_2 = files
        
        files_1 = files[start_1:end_1]
        
        files_0 = files[start_0:end_0]
        
        filename_count = 0
        
        for item in files_2:
            
            shutil.copyfile(item, "images_test/"+os.path.basename(item))
            os.rename("images_test/"+os.path.basename(item), "images_test/2_"+"%04d" % (filename_count)+".png")
            filename_count += 1   
            
        filename_count = 0
        
        for item in files_1:
            
            shutil.copyfile(item, "images_test/"+os.path.basename(item))
            os.rename("images_test/"+os.path.basename(item), "images_test/1_"+"%04d" % (filename_count)+".png")
            filename_count += 1    
            
        filename_count = 0
        
        for item in files_0:
            
            shutil.copyfile(item, "images_test/"+os.path.basename(item))
            os.rename("images_test/"+os.path.basename(item), "images_test/0_"+"%04d" % (filename_count)+".png")
            filename_count += 1 
            
        shutil.rmtree("images")
        
        os.rename ("images_test", "images")
        
        '''
        Start Data Processing
        '''
        
        spinner = Halo(text='Creating dataset', spinner='dots')
        spinner.start()
        command = 'python colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 16 > log.txt'
        os.system(command)
        
        work_dir = "dataset"+str(time.time())
        
        os.mkdir(work_dir)
        os.mkdir(work_dir+"/pose")
                
        shutil.copytree("images", work_dir+"/images")
        
        with open('transforms.json') as file:
            
            data = json.load(file)
        
        objects = len(data["frames"])
        
        filecount = 0
        
        print("\rGenerating Training dataset.\r")
           
        for i in tqdm(range(0, objects), desc = "Working"):
            
            rawdata = (str(data["frames"][i])).split(":")
            
            image_path_original = rawdata[1].replace(", 'sharpness'", "")
            transform_matrix = rawdata[3]
            transform_matrix = transform_matrix.split(",")
            path1, p2, p3 = image_path_original.split("/")
            image_name = p3.replace("'", "")
            
            os.remove("images/"+image_name)
            
            new_pose_file = work_dir+"/pose/"+os.path.basename(image_name).replace("png", "txt")
            
            with open(new_pose_file, "w") as pose_file:
                
                pose_file.write(transform_matrix[0].replace(" [[", "").lstrip()+" "+transform_matrix[1].lstrip()+" "+transform_matrix[2].lstrip()+" "+transform_matrix[3].replace("]", "").lstrip()+"\r")
                pose_file.write(transform_matrix[4].replace(" [", "").lstrip()+" "+transform_matrix[5].lstrip()+" "+transform_matrix[6].lstrip()+" "+transform_matrix[7].replace("]", "").lstrip()+"\r")
                pose_file.write(transform_matrix[8].replace(" [", "").lstrip()+" "+transform_matrix[9].lstrip()+" "+transform_matrix[10].lstrip()+" "+transform_matrix[11].replace("]", "").lstrip()+"\r")
                pose_file.write(transform_matrix[12].replace(" [", "").lstrip()+" "+transform_matrix[13].lstrip()+" "+transform_matrix[14].lstrip()+" "+transform_matrix[15].replace("]", "").replace("}", "").lstrip()+"\r")
          
            filecount += 1
                
        '''
        
        Create bounding box
        '''
        
        with open(work_dir+"/bbox.txt", "w") as bbox:
            
            bbox.write("-7.500 -7.500 -7.500 8.500 8.500 8.500 0.4")
        '''
  
        Create arbitrary intrinsics
        
        '''
        
        with open(work_dir+"/intrinsics.txt", "w") as instrinsics:
            
            instrinsics.write("1111.1110311937682 400 400 0.\r0. 0. 0.\r0.\r1.\r800 800")
        
            
        '''
        Finally, rename the images dir to rgb and remove empty images folder on root
        
        '''
        
        os.rename(work_dir+"/images", work_dir+"/rgb")
        
        shutil.rmtree("images")
        shutil.rmtree("colmap_sparse")
        shutil.rmtree("colmap_text")
        os.remove("transforms.json")
        os.remove("log.txt")
        os.remove("colmap.db")
        
        print("\nDone.")
        sys.exit()
        
    def do_jpg(self, files):
        
        for file in files:
            file_to_png = file
            
            img = Image.open(file_to_png)
            img.save(file_to_png+'.png') 
            os.remove(file)
            
        files = glob.glob("images/*.*")
        
        for file in files:
            
            file_to_rename = file.replace(".jpg", "")
            
            os.rename(file, file_to_rename)
            
        self.do_png()
    
if __name__ == "__main__":
    
    data_handler().main()
