# Luke Coddington
# 10/16/22
# Assignment - Facial Recognition
# Assumed Time: 1hr
# Actual Time: 30mins
# Reasoning: The deepface library, though inacurate, had all the needed functions for this assignment. 

from deepface import DeepFace

face_analysis = DeepFace.analyze(img_path = "Face_1.jpg",enforce_detection=False)
age=DeepFace.analyze("Face_1.jpg",actions=["age"],enforce_detection=False)

print("\n\n")
print("="*50)
print("Age: ")
print(str(age["age"]))
print("="*50)

print("\n\n")
print("="*50)
print("Facial Analysis:")
print(str(face_analysis))
print("="*50)