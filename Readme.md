## コードの説明

1. クリックすると反応するウィンドウを作る。
2. そしてクリックしたら画像の座標を返す関数を作る。
3.用意した画像と同じサイズの０行列の画像を用意し、クリックした座標のところと
同じ座標に１を入れる。(クリックの数の省略のために範囲を１０×１０にした。)
4.用意した画像のフーリエ逆変換したものと3で用意したものを掛け合わせ
それをクリックするたびに足し合わせていく。

## 使い方

1. まずpython furie.pyで実行する。
2. ウィンドウが５つ開く。
3. clickという名前のウィンドウ上でクリックする。
4.ifftという名前のウィンドウに逆変換の合計が表示され、
ifft_singleという名前のウィンドウにクリックした場所の逆変換が表示される。

## 依存ライブラリ
cv2,numpy,Image

## 参考文献
http://whitecat-student.hatenablog.com/entry/2016/11/09/225631

http://labs.eecs.tottoriu.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
