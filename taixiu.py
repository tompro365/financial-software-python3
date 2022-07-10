from tkinter import *
import random

random.seed()
root = Tk()
root.title("Cứ đánh tất vận may sẽ đến")
root.geometry('630x530')
dice_faces= ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
dice_label = Label(root, font = ("Helvetica", 200))
result_label = Label(root, font = ("Helvetica", 40))

def roll():
	first_dice = random.randint(1, 6)
	second_dice = random.randint(1, 6)
	third_dice = random.randint(1, 6)

	dice_label.config(
		text = f'{dice_faces[first_dice - 1]}{dice_faces[second_dice - 1]}{dice_faces[third_dice -1]}')
	dice_label.pack()

	sum = first_dice + second_dice + third_dice
	result_label.config(text = 'Tài' if sum > 10 else 'Xỉu',
						foreground = 'red' if sum > 10 else 'green')
	result_label.pack(after = dice_label)

b1 = Button(root, text = "Quay !", foreground = 'blue', command = roll)
b1.pack()

root.mainloop()