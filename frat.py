import face_recognition
import cv2
import numpy as np
import threading
import os
import pickle

from VideoCapture import VideoCapture

class FRAT:
    def __init__(self, filepath="encodings") -> None:
        self.videocapture = VideoCapture(0)
        self.draw = True
        self.callback = None
        self.thread = None
        self.filepath = filepath

        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.datpath = os.path.join(self.dir_path,'dataset_faces.dat')

        self.process_frame = True
        self.proc_face_locations = []
        self.proc_face_names = []

        self.running = False


    def encodeFaces(self):
        all_face_encodings = {}

        directory = 'images'
        

        for i,(root, dirs, files) in enumerate(os.walk(os.path.join(self.dir_path,directory))):
            if i > 0:
                foldername = root.split('\\')[-1]
                for file in files:
                    filename = file.split('.')[0]

                    img = face_recognition.load_image_file(os.path.join(root,file))
                    all_face_encodings[foldername] = face_recognition.face_encodings(img)[0]


        print(self.dir_path)
        print(all_face_encodings)

        # Write encoding
        with open(self.datpath, 'wb') as f:
            pickle.dump(all_face_encodings,f)
            f.close()


        pass
    
    # Get faces using frame 2
    def getFaces(self,callback=None):
        print('Start get faces')

        # Load encodings
        with open(self.datpath, 'rb') as f:
            all_face_encodings = pickle.load(f)

        # Grab the list of names and the list of encodings
        known_face_encodings = np.array(list(all_face_encodings.values()))
        known_face_names = list(all_face_encodings.keys())

        print(known_face_encodings)
        print(known_face_names)

        while self.running:
            
            self.temp_face_locations = []
            self.temp_face_names = []

            # Only process every other frame of video to save time
            if self.videocapture.frame2 is not None:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(self.videocapture.frame2, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]
                
                # Find all the faces and face encodings in the current frame of video
                self.temp_face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, self.temp_face_locations)

                
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    self.temp_face_names.append(name)
                

                self.proc_face_names = self.temp_face_names
                self.proc_face_locations = self.temp_face_locations

                print('Getting faces')
                # print(self.proc_face_names)
                # print(self.proc_face_locations)

                if callback is not None and type(callback) is function:
                    callback(self.proc_face_names,self.proc_face_locations)

            

        return

    # Draw frame using frame 3
    def drawFrame(self):
        print('Start draw frame')
        while self.running:

            for (top, right, bottom, left), name in zip(self.proc_face_locations, self.proc_face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(self.videocapture.frame3, (left, top), (right, bottom), (0, 0, 255), 2)
                # Draw a label with a name below the face
                cv2.rectangle(self.videocapture.frame3, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(self.videocapture.frame3, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            if self.videocapture.frame3 is not None:
                # Display the resulting image
                cv2.imshow('Video', self.videocapture.frame3)
                print('Drawing frame')


                # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()
                break
    
    def start(self):
        self.running = True
        self.videocapture.start()
        t1 = threading.Thread(target=self.getFaces)
        t2 = threading.Thread(target=self.drawFrame)
        t1.start()
        t2.start()
    
    def stop(self):
        print('Stopping...')
        self.running = False
        self.videocapture.stop()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    frat = FRAT()
    frat.start()

