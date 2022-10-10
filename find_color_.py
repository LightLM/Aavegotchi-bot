import time
import numpy as np
import pyautogui
from mss import mss
import pyautogui as pg
from math import sqrt
import keyboard


class FINDER:

    def __init__(
            self,
            monitor: dict,
            our_colors: list

    ) -> None:
        """Инициализация данных класса"""

        self.__our_colors: list = [[0, 208, 0], [146, 7, 8], [7, 253, 254], [103, 2, 255]]
        self.__monitor: dict = {
            "left": 8,
            "top": 31,
            "width": 1920,
            "height": 1080
        }

    def min_distance(self, x, y, iterable):
        list_of_distances = list(map(lambda t: sqrt(pow(t[0] - x, 2) + pow(t[1] - y, 2)), iterable))
        min_res = min(list_of_distances)
        index_of_min = list_of_distances.index(min_res)
        return iterable[index_of_min]

    def find_colors(self, monitor={}):
        m = mss()
        img = m.grab(self.__monitor)
        img_arr = np.array(img)
        our_map = (our_color[2], our_color[1], our_color[0], 255)
        indexes = np.where(np.all(img_arr == our_map, axis=-1))
        our_crd = np.transpose(indexes)
        return our_crd


if __name__ == '__main__':

    while True:
        # keyboard.wait("q")
        print('start')
        time1 = time.time()
        try:
            result1 = find_color(our_color[0], monitor)
            if result1.__len__():
                x1 = result1[0][1] + monitor.get('left')
                y1 = result1[0][0] + monitor.get('top')
                green = [x1, y1]
                print('first green', green)

            result2 = find_color(our_color[1], monitor)
            if result2.__len__():
                x2 = result2[0][1] + monitor.get('left')
                y2 = result2[0][0] + monitor.get('top')
                red = [x2, y2]
                print('second red', red)

            result3 = find_color(our_color[2], monitor)
            if result3.__len__():
                x3 = result3[0][1] + monitor.get('left')
                y3 = result3[0][0] + monitor.get('top')
                blue = [x3, y3]
                print('therd blue', blue)

            result4 = find_color(our_color[3], monitor)
            if result4.__len__():
                x4 = result4[0][1] + monitor.get('left')
                y4 = result4[0][0] + monitor.get('top')
                purple = [x4, y4]
                print('four purple', purple)

            all_cord = [green, red, blue, purple]
            centre = [955, 535]
            a = min_distance(955, 535, all_cord)
            time2 = time.time()
            print('Общее время нахождения ближайшего кристала: ', time2 - time1)
            pg.moveTo(a)
            pyautogui.mouseDown(a)
            time.sleep(0.1)
        except:
            pass

            time.sleep(1)
