import tkinter as tk
import random

class SimpleLudo:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Ludo")
        self.root.geometry("600x500")
        self.root.configure(bg='lightblue')
        
        # Game state
        self.positions = [0, 0, 0, 0]  # All players start at position 0
        self.current_player = 0
        self.dice_value = 0
        self.game_over = False
        self.message_text = "Game started! Player 1's turn"
        
        # Colors for players
        self.colors = ["red", "green", "blue", "yellow"]
        self.player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
        
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="SIMPLE LUDO", 
                              font=("Arial", 20, "bold"), bg='lightblue')
        title_label.pack(pady=10)
        
        # Game board frame
        board_frame = tk.Frame(self.root, bg='white', width=400, height=300, relief='solid', bd=2)
        board_frame.pack(pady=10)
        board_frame.pack_propagate(False)
        
        # Canvas for pawns
        self.canvas = tk.Canvas(board_frame, bg='white', width=400, height=300)
        self.canvas.pack()
        
        # Draw simple board
        self.draw_simple_board()
        
        # Current player info
        self.player_label = tk.Label(self.root, text="Current Player: Player 1", 
                                    font=("Arial", 14, "bold"), bg='lightblue', fg='red')
        self.player_label.pack(pady=5)
        
        # Message display
        self.message_label = tk.Label(self.root, text=self.message_text, 
                                     font=("Arial", 12), bg='lightblue', 
                                     fg='darkblue', wraplength=500)
        self.message_label.pack(pady=5)
        
        # Dice display
        dice_frame = tk.Frame(self.root, bg='lightblue')
        dice_frame.pack(pady=10)
        
        self.dice_label = tk.Label(dice_frame, text="🎲", font=("Arial", 30), 
                                  bg='white', width=4, height=2, relief='solid', bd=2)
        self.dice_label.pack()
        
        self.dice_value_label = tk.Label(dice_frame, text="Click Roll", 
                                        font=("Arial", 12), bg='lightblue')
        self.dice_value_label.pack()
        
        # Roll button
        self.roll_button = tk.Button(self.root, text="ROLL DICE", 
                                    font=("Arial", 14, "bold"),
                                    bg='green', fg='white',
                                    command=self.roll_dice)
        self.roll_button.pack(pady=10)
        
        # Positions display
        positions_frame = tk.Frame(self.root, bg='lightblue')
        positions_frame.pack(pady=10)
        
        self.positions_label = tk.Label(positions_frame, text="", 
                                       font=("Arial", 12), bg='lightblue', justify=tk.LEFT)
        self.positions_label.pack()
        
        # Game info
        info_label = tk.Label(self.root, 
                             text="Rules: Roll 6 to start | Roll 6 for extra turn | Reach 56 to win",
                             font=("Arial", 10), bg='lightblue', wraplength=500)
        info_label.pack(pady=5)
    
    def draw_simple_board(self):
        self.canvas.delete("all")
        
        # Draw a simple board path
        self.canvas.create_rectangle(50, 50, 350, 250, outline='black', width=2)
        
        # Draw start positions
        start_positions = [(100, 100), (300, 100), (300, 200), (100, 200)]
        
        for i, (x, y) in enumerate(start_positions):
            self.canvas.create_oval(x-15, y-15, x+15, y+15, 
                                   fill=self.colors[i], outline='black', width=2)
    
    def update_display(self):
        # Update player label
        self.player_label.config(text=f"Current Player: {self.player_names[self.current_player]}", 
                                fg=self.colors[self.current_player])
        
        # Update positions text
        positions_text = "Current Positions:\n"
        for i in range(4):
            status = "HOME" if self.positions[i] == 0 else f"Position {self.positions[i]}"
            positions_text += f"{self.player_names[i]}: {status}\n"
        self.positions_label.config(text=positions_text)
        
        # Update message
        self.message_label.config(text=self.message_text)
        
        # Draw pawns
        self.draw_pawns()
    
    def draw_pawns(self):
        self.canvas.delete("pawn")
        
        # Calculate positions on simple board
        board_positions = [
            (100 + min(self.positions[0], 14) * 14, 100),  # Player 1 path
            (300, 100 + min(self.positions[1], 14) * 10),  # Player 2 path
            (300 - min(self.positions[2], 14) * 14, 200),  # Player 3 path
            (100, 200 - min(self.positions[3], 14) * 10)   # Player 4 path
        ]
        
        for i in range(4):
            x, y = board_positions[i]
            
            # Draw pawn
            self.canvas.create_oval(x-10, y-10, x+10, y+10, 
                                   fill=self.colors[i], outline='black', width=2, tags="pawn")
            
            # Add player number
            self.canvas.create_text(x, y, text=str(i+1), font=("Arial", 8, "bold"), tags="pawn")
    
    def roll_dice(self):
        if self.game_over:
            self.message_text = "Game Over! Restart to play again."
            self.update_display()
            return
        
        # Roll the dice
        self.dice_value = random.randint(1, 6)
        self.dice_label.config(text=str(self.dice_value))
        self.dice_value_label.config(text=f"Rolled: {self.dice_value}")
        
        # Process the move automatically
        self.process_move()
    
    def process_move(self):
        player_pos = self.positions[self.current_player]
        player_name = self.player_names[self.current_player]
        
        # If pawn is at home (position 0)
        if player_pos == 0:
            if self.dice_value == 6:
                self.positions[self.current_player] = 1
                self.message_text = f"🎉 {player_name} rolled 6! Pawn unlocked at position 1 + Extra turn!"
                self.update_display()
                # Extra turn for rolling 6
                self.roll_dice()
            else:
                self.message_text = f"{player_name} rolled {self.dice_value}. Need 6 to unlock pawn. Next player's turn."
                self.update_display()
                self.next_player()
        
        else:
            # Pawn is already on board
            new_position = player_pos + self.dice_value
            
            # Check for win
            if new_position >= 56:
                self.positions[self.current_player] = 56
                self.message_text = f"🎉 🎉 {player_name} WINS! Reached position 56! 🎉 🎉"
                self.game_over = True
                self.update_display()
                return
            
            # Normal move
            self.positions[self.current_player] = new_position
            
            # Check for extra turn with 6
            if self.dice_value == 6:
                self.message_text = f"🎉 {player_name} rolled 6! Moved to position {new_position} + Extra turn!"
                self.update_display()
                # Extra turn
                self.roll_dice()
            else:
                self.message_text = f"{player_name} moved to position {new_position}. Next player's turn."
                self.update_display()
                self.next_player()
    
    def next_player(self):
        if not self.game_over:
            self.current_player = (self.current_player + 1) % 4
            self.dice_value = 0
            self.dice_label.config(text="🎲")
            self.dice_value_label.config(text="Click Roll")
            self.update_display()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SimpleLudo(root)
    root.mainloop()