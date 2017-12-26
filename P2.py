### Preprocess the data here. It is required to normalize the data. Other preprocessing steps could include
### converting to grayscale, etc.
### Feel free to use as many code cells as needed.
from sklearn.utils import shuffle
# import cv2

#Normalize grayscale

def normalize_grayscale(image_data):
    """
    Normalize the image data with Min_Max scaling to a range of [0.1, 0.9]

    """
    a = 0.1
    b = 0.9
    grayscale_min = 0
    grayscale_max = 255

    return a + ( ( (image_data - grayscale_min)*(b - a) )/( grayscale_max - grayscale_min ) )

gray_converter = np.array([[0.299],[0.587],[0.114]])
Xg_train = np.zeros((n_train, 32, 32, 1))
Xg_train[:,:,:,] = np.dot(X_train[:,:,:,], gray_converter)

Xg_valid = np.zeros((n_valid, 32, 32, 1))
Xg_valid[:,:,:,] = np.dot(X_valid[:,:,:,], gray_converter)


# X_train_gray = np.dot(X_train[index], [0.299,0.587,0.114])

# X_gtrain = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

print(gray_img.shape)
print(gray_img[0].shape)

# img = gray_img[2].squeeze()
# plt.figure(figsize=(2,2))
# plt.imshow(gray_img[0], cmap='gray')

# X_trainNorm = normalize_grayscale(X_train_gray)
# # y_trainNorm = normalize_grayscale(y_train)

# print(X_trainNorm.shape)


# plt.figure(figsize=(2,2))
# plt.imshow(X_trainNorm)


# #Shuffle data?
# X_train, y_train = shuffle(X_train, y_train)
