import os
import shutil

from deepface import DeepFace

# 获取文件列表
to_reco_path = 'to_reco'
file_list = os.listdir(to_reco_path)

model_name = "Facenet512"
db_path = "database"
detector_backend = "mtcnn"

result_list = []

for f in file_list:
    img_path = os.path.join("to_reco", f)
    
    # 识别并标记
    try:
        dfs = DeepFace.find(
            img_path=img_path, db_path=db_path, model_name=model_name, detector_backend=detector_backend,
            threshold=0.25  # 设置一个相似度(distance)门槛，区分出不认识的脸，归在一起。只有很相似的人脸才能过
        )
        df = dfs[0]
        identity = list(df["identity"])[0]  # 取出第一个作为结果
        name = identity.split('\\')[1]
        # print(f, df[["identity", "distance"]])
        print(name)
        result_list.append((f, name))
    except ValueError as e:
        # 没有人脸的标记为 none face
        if "Face could not be detected" in str(e):
            print("Face could not be detected")
            result_list.append((f, "none face"))
    except IndexError as e:
        # IndexError 有人脸，但是相似度达不到
        print("Other face")
        result_list.append((f, "other face"))
    finally:
        print("-----------")

# 移动文件
for file_name, identity in result_list:
    source_path = os.path.join(to_reco_path, file_name)
    target_path = os.path.join("reco_result", identity)
    
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        
    shutil.move(source_path, target_path)
    print(f"Moved {file_name} to {target_path}")
