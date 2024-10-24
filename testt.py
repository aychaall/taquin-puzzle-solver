import tkinter as tk
from PIL import Image, ImageTk
import random
from DFS import dfs_real_time  # Importer la fonction DFS
from BFS import bfs_real_time  # Importer la fonction BFS

class TaquinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sliding Puzzle")
        self.root.geometry("650x800")
        self.root.config(bg="#3b53a0")

        # Créer l'étiquette du titre
        self.title_label = tk.Label(root, text="Sliding Puzzle", font=("Arial", 24), bg="#3b53a0", fg="#ffffff")
        self.title_label.place(x=220, y=10)

        # Charger et créer les pièces du puzzle
        self.load_puzzle()

        # Bouton de mélange
        self.shuffle_button = tk.Button(root, text="Mélanger", command=self.shuffle_pieces, bg="#fff", fg="#000")
        self.shuffle_button.place(x=150, y=590, width=150, height=30)

        # Boutons radio pour choisir l'algorithme
        self.algorithm_choice = tk.StringVar(value="DFS")  # Par défaut à DFS
        self.dfs_button = tk.Radiobutton(root, text="DFS", variable=self.algorithm_choice, value="DFS", bg="#3b53a0")
        self.dfs_button.place(x=200, y=550)
        self.bfs_button = tk.Radiobutton(root, text="BFS", variable=self.algorithm_choice, value="BFS", bg="#3b53a0")
        self.bfs_button.place(x=300, y=550)

        # Bouton de résolution
        self.solve_button = tk.Button(root, text="Résoudre", command=self.solve_puzzle)
        self.solve_button.place(x=400, y=550)

        # Bouton de réinitialisation
        self.reset_button = tk.Button(root, text="Réinitialiser", command=self.reset_puzzle)
        self.reset_button.place(x=300, y=590, width=150, height=30)

        # Stocker les positions originales pour référence
        self.original_positions = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Positions originales
        self.current_state = self.original_positions  # Initialiser l'état actuel

    def load_puzzle(self):
        # Liste pour contenir les pièces
        self.lt = []
        self.lab = []

        # Charger et redimensionner l'image
        path = "taquin2.png"
        img = Image.open(path).resize((390, 390))

        # Créer les pièces du puzzle
        for i in range(3):
            for j in range(3):
                cropped_img = img.crop((j * 130, i * 130, (j * 130) + 130, (i * 130) + 130))
                photo_img = ImageTk.PhotoImage(cropped_img)
                self.lt.append(photo_img)
                label = tk.Label(self.root, image=photo_img, background="#3b53a0")
                label.place(x=(j * 130) + 80, y=(i * 130) + 100, width=130, height=130)
                self.lab.append(label)

    def shuffle_pieces(self):
        indices = list(range(9))  # Créer une liste d'indices
        random.shuffle(indices)  # Mélanger les indices

        # Mettre à jour les positions des pièces basées sur les indices mélangés
        for index, shuffled_index in enumerate(indices):
            self.lab[index].config(image=self.lt[shuffled_index])  # Mettre à jour l'image
            self.lab[index].place(x=(index % 3) * 130 + 80, y=(index // 3) * 130 + 100)  # Position centrée

        self.current_state = tuple(indices)  # Stocker l'état mélangé comme état actuel

    def solve_puzzle(self):
        # Désactiver le bouton Mélanger pour éviter les interruptions pendant la résolution
        self.shuffle_button.config(state=tk.DISABLED)

        # Appeler l'algorithme approprié en fonction de l'option choisie
        goal_state = (0,1, 2, 3, 4, 5, 6, 7, 8)

        if self.algorithm_choice.get() == "DFS":
            path, nodes = dfs_real_time(self.current_state, goal_state)
        else:  # BFS
            path, nodes = bfs_real_time(self.current_state, goal_state)

        if path is None:
            print("Pas de solution")
            self.shuffle_button.config(state=tk.NORMAL)  # Activer le bouton Mélanger
            self.solve_button.config(state=tk.NORMAL)
        else:
            print(f"Chemin trouvé: {path}")

            # Parcourir tous les nœuds intermédiaires (les états)
            for node in nodes:
                self.update_ui(node)
                self.root.update()  # Forcer la mise à jour de l'interface graphique
                self.root.after(500)  # Pause de 500ms pour visualiser chaque étape

            # Assurer que le dernier état de la solution est bien affiché
            self.update_ui(goal_state)
            self.root.update()

    def reset_puzzle(self):
        self.load_puzzle()  # Correctement appeler la méthode load_puzzle
        self.shuffle_button.config(state=tk.NORMAL)  # Activer le bouton Mélanger

    def update_ui(self, state):
        # Mettre à jour l'interface avec l'état actuel
        for i, value in enumerate(state):
            self.lab[i].config(image=self.lt[value])  # Mettre à jour l'image basée sur l'état actuel
            self.root.update_idletasks()  # Rafraîchir immédiatement l'interface

        # Vérifier si le puzzle est résolu
        if state == (0,1, 2, 3, 4, 5, 6, 7, 8):
            self.shuffle_button.config(state=tk.NORMAL)  # Activer le bouton Mélanger
            self.solve_button.config(state=tk.NORMAL)  # Optionnellement activer le bouton Résoudre

if __name__ == "__main__":
    root = tk.Tk()
    app = TaquinApp(root)
    root.mainloop()
