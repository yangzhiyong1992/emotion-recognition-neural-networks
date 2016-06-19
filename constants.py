#                               __                    __             
#                              /\ \__                /\ \__          
#   ___    ___     ___     ____\ \ ,_\    __      ___\ \ ,_\   ____  
#  /'___\ / __`\ /' _ `\  /',__\\ \ \/  /'__`\  /' _ `\ \ \/  /',__\ 
# /\ \__//\ \L\ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_/\ \/\ \ \ \_/\__, `\
# \ \____\ \____/\ \_\ \_\/\____/ \ \__\ \__/.\_\ \_\ \_\ \__\/\____/
#  \/____/\/___/  \/_/\/_/\/___/   \/__/\/__/\/_/\/_/\/_/\/__/\/___/  .txt
#
#

CACHE_DATASET_PATH = './dataset/cache/'
DATASET_PATH = './dataset/'
CASC_PATH = './haarcascade_files/haarcascade_frontalface_default.xml'
SIZE_FACE = 48
EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
SAVE_DIRECTORY = './fer2013 preprocessed data/'
SAVE_MODEL_FILENAME = 'model.tfl'
SAVE_DATASET_IMAGES_FILENAME = 'data_set_fer2013.npy'
SAVE_DATASET_LABELS_FILENAME = 'data_labels_fer2013.npy'
SAVE_DATASET_IMAGES_TEST_FILENAME = 'preprocessed data final - with disgusted/test_set_rafd.npy'
SAVE_DATASET_LABELS_TEST_FILENAME = 'preprocessed data final - with disgusted/test_labels_rafd.npy'