import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,220),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (100,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (282,178),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (386,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (570,40),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (760,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Urans",
            (974,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1106,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )



cv2.imshow("output",img)
cv2.waitKey(0)