class Texteditor:
    def __init__(keep):
        keep.content = ''
        keep.undo_stack = []

    def wrrite(keep, text):
        keep.undo_stack.append(keep.content)
        keep.content += text
        print(f"Tulis: {keep.content}")

    def undo(keep):
        if keep.undo_stack:
            keep.content = keep.undo_stack.pop()
            print(f"Undo: {keep.content}")
        else:
            print("Tidak ada yang bisa di-undo")

editor = Texteditor()
editor.wrrite("Hello")
editor.wrrite("Dunia")
editor.wrrite("!")
editor.undo()
editor.undo()
