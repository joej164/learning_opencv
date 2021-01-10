import cv2
import mss
import numpy
import pytesseract

import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

with mss.mss() as sct:
    # sct_img = sct.shot(mon=2)

    # monitor_number = 2
    # mon = sct.monitors[monitor_number]

    # monitor = {
    #     # "top": mon["top"] + 270,  # 100px from the top
    #     # "left": mon["left"] + 520,  # 100px from the left
    #     # "width": 100,
    #     # "height": 30,
    #     "mon": monitor_number
    # }

    # sct_img = sct.grab(monitor)
    sct_img = sct.grab(sct.monitors[2])
    src = numpy.array(sct_img)

    grayscaled = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('iron_chunk_grey.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(grayscaled, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.86
    loc = np.where(res >= threshold)
    print(loc)
    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(src, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow('Detected', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # retval, threshold = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY)
    # retval, threshold = cv2.threshold(
    #     grayscaled, 110, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # th = cv2.adaptiveThreshold(
    #     grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    # cv2.imshow('Threshold', threshold)

    scale_percent = 100

    width = int(grayscaled.shape[1] * scale_percent / 100)
    height = int(grayscaled.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    img = cv2.resize(grayscaled, dsize)

    cv2.imshow('Threshold', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # print(pytesseract.image_to_string(img))
    output = pytesseract.image_to_string(img, config=f'--psm 1')
    print(output)

    for x in range(14):
        print(f'PSM Type: {x}')
        for y in range(5):
            try:
                print(pytesseract.image_to_string(img, config=f'--psm {x}'))
                #print(pytesseract.image_to_string(threshold, config=f'--psm {x}'))
            except Exception:
                print(f'failed {x}')
