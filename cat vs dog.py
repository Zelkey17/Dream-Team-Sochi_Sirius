
def reimg(img, label):
    img = tf.cast(img, tf.float32)
    img = img / 255.0
    return img, label
train_recomp = train[0].map(reimg)
train_batches = train_recomp.shuffle(1000).batch(15)
model = tf.keras.Sequential(Dropout(0.2))
model.add(Conv2D((3,3),activation="relu"))
model.compile(optimizer=keras.optimizers.Adadelta(), loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])
model.fit(train_batches, epochs=1)
a=int(input())

while a==1:
    imgimi = grab()
    img_array = img_to_array(imgimi)
    img_resized, _ = reimg(img_array, _)
    img_expended = np.expand_dims(img_resized, axis=0)
    prediction = model.predict(img_expended)[0][0]
    pred_label = 'КОТ' if prediction < 0.5 else 'СОБАКА'
    plt.figure()
    plt.title(f'{pred_label} {prediction}')
    print(str(pred_label)+"["+str(math.floor(abs(prediction-0.5)))+"]")

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6, weight=1) # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1) # То же самое для третьего ряда

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        self.canv.bind("<B1-Motion>", self.draw) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw

        color_lab = Label(self, text="Color: ") # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=0, column=0, padx=6) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red")) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1) # Устанавливаем кнопку

        # Создание остальных кнопок повторяет ту же логику, что и создание
        # кнопки установки красного цвета, отличаются лишь аргументы.

        green_btn = Button(self, text="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.set_brush_size(10))
  