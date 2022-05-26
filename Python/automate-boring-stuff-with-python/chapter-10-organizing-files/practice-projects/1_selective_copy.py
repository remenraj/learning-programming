import os, shutil

def selective_copy(source_folder, ext, destination_folder):
    """ Copies all files with the given extension from the input folder to the output folder. """

    result_folder = os.path.abspath(destination_folder)
    #print(resultFolder)

    for folder_name, sub_folder, file_name in os.walk(source_folder):

        for file in file_name:

            if file.endswith(ext):
                
                file_path = os.path.join(os.path.abspath(folder_name), file)

                if not os.path.exists(result_folder):
                    # create result folder if it doesn't exist
                    os.makedirs(result_folder)

                
                if os.path.dirname(file_path) != result_folder:
                    # prevent copying files from result folder              
                    shutil.copy(file_path, result_folder)
                    print(f'Copied {file_path} to {result_folder}')


if __name__ == '__main__':
    selective_copy('.', 'png', 'result')