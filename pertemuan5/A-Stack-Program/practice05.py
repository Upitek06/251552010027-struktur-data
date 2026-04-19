class Texteditor:
    def __init__ (keep):
        keep.Text = ''
        keep.undo_stack = []

    def write(keep,teks):
        keep.undo_stack.append(keep.Text)
        keep.Text += teks
        print(f"Tulis: {keep.Text}")

    def undo(keep):
        if keep.undo_stack:
            keep.Text = keep.undo_stack.pop()
            print(f"Undo: {keep.Text}")
        else:
            print("Tidak ada yang bisa di-undo")

pembalik = Texteditor()
pembalik.write("Dulu ")
pembalik.write("Saya ")
pembalik.write("Penggila ")
pembalik.write("Game ")
pembalik.undo()
pembalik.undo()
pembalik.undo()
pembalik.undo()