from DeepImageSearch import Load_Data, Search_Setup
import cv2
print("Please input query image:")
query = input()
image_list = Load_Data().from_folder(['test_images'])
st = Search_Setup(image_list, model_name="vgg19", pretrained=True, image_count=None)
st.run_index()
#st.plot_similar_images(image_path='test1.jpg', number_of_images=3)
similar_images = st.get_similar_images(image_path=query, number_of_images=3)
print(similar_images)

query_image = cv2.imread(query)
(h, w) = query_image.shape[:2]
width = 800
r = width / float(w)
dim = (width, int(h * r))
resizeQuery = cv2.resize(query_image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Query", resizeQuery)

file_paths = [value for value in similar_images.values()]
for image in file_paths:
    filename = str(image)
    result = cv2.imread(filename)
    (h, w) = result.shape[:2]
    width = 800
    r = width / float(w)
    dim = (width, int(h * r))
    resize = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Result", resize)
    cv2.waitKey(0)