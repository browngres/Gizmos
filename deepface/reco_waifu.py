"""
人脸识别，先给定的一些人的照片作为数据库，再给出一张照片识别出是哪位。
项目来源：https://github.com/serengil/deepface
"""
import os
from deepface import DeepFace

model_name = "Facenet512"
# model_name = "VGG-Face"
img_path = os.path.join("to_reco", "20231012_011912.jpg")
db_path = "database"
# detector_backend = "retinaface"
# detector_backend = "opencv"
detector_backend = "mtcnn"


dfs = DeepFace.find(
    img_path=img_path, db_path=db_path, model_name=model_name, detector_backend=detector_backend,
    threshold=0.35,
    enforce_detection=False
)

# assert len(dfs) > 0
for df in dfs:
    print(df[["identity", "distance"]])
    identity = list(df["identity"])[0]  # 取出第一个作为结果
    name = identity.split('\\')[1]
    print(name)

    
# resp_obj = DeepFace.verify(
#     # "database\\zhongben\\20250331_193156.jpg",
#     "database\\zhongben\\20250309_221121.jpg",
#     "database\\zhongben\\20250224_004100.jpg",
#     model_name=model_name, enforce_detection=False, distance_metric="cosine")
#
# print(resp_obj)
#
# if resp_obj["verified"]:
#     print("verify✅")
# else:
#     print("verify❌")


# anal = DeepFace.analyze(
#     img_path="database\\zhongben\\20250309_221121.jpg", actions=['age', 'gender', 'race', 'emotion'], enforce_detection=False
# )
# print(anal)
