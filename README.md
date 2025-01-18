# Higher-Lower Game

This Python app implements a fun **Higher-Lower Game**, where players compare social media follower counts of two entities and guess which one has more followers. The game provides a seamless interactive experience with score tracking and replay options.

# Features:

- **Interactive Gameplay**:
  - Players are presented with two options (e.g., celebrities, brands).
  - Guess which has more followers by typing `A` or `B`.
- **Randomized Options**: Options are randomly selected from a predefined dataset.
- **Score Tracking**: The game keeps track of the player's score for correct guesses.
- **Replay Option**: Continue guessing until an incorrect answer ends the game.
- **Visual Design**: Includes ASCII art for branding and comparison symbols.

# How to Use:

- Run the script using the command:

  ```bash
  python main.py
  ```

- The game will display the logo and provide two comparison options:

  - Option A: Name, description, and country of origin.
  - Option B: Name, description, and country of origin.

- Input your guess:

  - Type `A` if you believe Option A has more followers.
  - Type `B` if you believe Option B has more followers.

- The game will:

  - Display if your choice was correct.
  - Update your score if correct and provide a new comparison.
  - End the game if your guess is incorrect.

- View your final score and decide whether to restart or exit.

# Example Output:

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A : Instagram, a Social media platform, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Compare B : Cristiano Ronaldo, a Footballer, from Portugal

Who has more followers type 'A' or 'B' : A
You are right! Current score: 1
Compare A : Cristiano Ronaldo, a Footballer, from Portugal

 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Compare B : Beyoncé, a Musician, from United States
...
```

# Dataset:

- Predefined in `game_data.py`.
- Includes celebrities, brands, and organizations with follower counts, descriptions, and countries.

# Future Enhancements:

- Expand the dataset with more options.
- Add difficulty levels or hints for closer comparisons.
- Introduce timed gameplay for an added challenge.



