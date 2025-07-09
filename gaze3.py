import cv2
import os
import dlib
from eye import Eye
from calibration import Calibration

class GazeTracking(object):
    def __init__(self):
        self.frame = None
        self.eye_left = None
        self.eye_right = None
        self.calibration = Calibration()

        # _face_detector is used to detect faces
        self._face_detector = dlib.get_frontal_face_detector()

        # _predictor is used to get facial landmarks of a given face
        cwd = os.path.abspath(os.path.dirname(__file__))
        model_path = os.path.abspath(os.path.join(cwd, "trained_models/shape_predictor_68_face_landmarks.dat"))
        self._predictor = dlib.shape_predictor(model_path)

    @property
    def pupils_located(self):
        """Check that the pupils have been located"""
        if self.eye_left is None or self.eye_right is None:
            return False
        if self.eye_left.pupil is None or self.eye_right.pupil is None:
            return False
        try:
            int(self.eye_left.pupil.x)
            int(self.eye_left.pupil.y)
            int(self.eye_right.pupil.x)
            int(self.eye_right.pupil.y)
            return True
        except Exception:
            return False

    def _analyze(self):
        """Detects the face and initialize Eye objects"""
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self._face_detector(frame)

        try:
            landmarks = self._predictor(frame, faces[0])
            self.eye_left = Eye(frame, landmarks, 0, self.calibration)
            self.eye_right = Eye(frame, landmarks, 1, self.calibration)

        except IndexError:
            self.eye_left = None
            self.eye_right = None

    def refresh(self, frame):
        """Refreshes the frame and analyzes it."""
        self.frame = frame
        self._analyze()

    def pupil_left_coords(self):
        """Returns the coordinates of the left pupil"""
        if self.pupils_located:
            x = self.eye_left.origin[0] + self.eye_left.pupil.x
            y = self.eye_left.origin[1] + self.eye_left.pupil.y
            return (x, y)
        return None

    def pupil_right_coords(self):
        """Returns the coordinates of the right pupil"""
        if self.pupils_located:
            x = self.eye_right.origin[0] + self.eye_right.pupil.x
            y = self.eye_right.origin[1] + self.eye_right.pupil.y
            return (x, y)
        return None

    def annotated_frame(self):
        """Returns the main frame with pupils highlighted, or fallback crosses."""
        frame = self.frame.copy()

        # Attempt to get pupil coordinates
        left_coords = self.pupil_left_coords()
        right_coords = self.pupil_right_coords()

        # If pupils are located, draw crosses
        if left_coords and right_coords:
            color = (0, 255, 0)
            x_left, y_left = left_coords
            x_right, y_right = right_coords
            
            # Draw the crosses on the pupils
            cv2.line(frame, (x_left - 5, y_left), (x_left + 5, y_left), color)
            cv2.line(frame, (x_left, y_left - 5), (x_left, y_left + 5), color)
            cv2.line(frame, (x_right - 5, y_right), (x_right + 5, y_right), color)
            cv2.line(frame, (x_right, y_right - 5), (x_right, y_right + 5), color)
        else:
            # If pupils are not detected, draw fallback crosses in the center or a fixed location
            # Using fixed coordinates as fallback (you can adjust this to other default locations if desired)
            center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
            color = (0, 0, 255)  # Fallback cross color (red)
            cv2.line(frame, (center_x - 5, center_y), (center_x + 5, center_y), color)
            cv2.line(frame, (center_x, center_y - 5), (center_x, center_y + 5), color)

        return frame
