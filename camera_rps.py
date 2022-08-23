import cv2
from keras.models import load_model
import numpy as np
import time
import random


class RPS:

    def __init__(self, user_score=0, computer_score=0):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.rps_array = ['rock', 'paper', 'scissors', 'nothing']
        self.user_score = user_score
        self.computer_score = computer_score

    def get_computer_choice(self):
        return random.choice(self.rps_array[:3])

    # def get_user_choice(self):
    #     print("type either rock, paper or scissors")
    #     userInput = input()
    #     while userInput.lower() not in self.rps_array:
    #         print("type either rock, paper or scissors")
    #         userInput = input()
    #     return userInput.lower()

    def countdown(self) -> None:
        end_time = time.time() + 3
        return end_time

    def get_user_choice(self):
        end_time = self.countdown()

        while end_time > time.time():
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(
                frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) /
                                127.0) - 1  # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(np.argmax(prediction[0]))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

        # Destroy all the windows

        # After the loop release the cap object

        return self.rps_array[np.argmax(prediction[0])]

    def get_winner(self, computer_choice, user_choice):
        cIndex = self.rps_array.index(computer_choice)
        uIndex = self.rps_array.index(user_choice)

        print(f"you chose {user_choice}, computer chose {computer_choice}")

        # maybe a way to cut down on code using index - 1?
        if uIndex == 3:
            print("you chose nothing, try again")
            self.computer_score += 1
        elif cIndex == uIndex:
            print("draw")
            self.user_score += 1  # edit this out later, bug testing
        elif cIndex == uIndex + 1 or cIndex == uIndex - 2:
            print("lose")
            self.computer_score += 1
        elif cIndex == uIndex - 1 or cIndex == uIndex + 2:
            print("win")
            self.user_score += 1
        else:
            print("something went wrong")
            self.user_score += 1  # edit this out later, bug testing

    def score(self):
        self.user_score += 1


def play():
    game = RPS(user_score=0, computer_score=0)
    # while (game.computer_score < 3) or (game.user_score < 3):
    computer_choice = game.get_computer_choice()
    user_choice = game.get_user_choice()
    game.get_winner(computer_choice, user_choice)


play()
