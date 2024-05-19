une documentation pour les deux commandes Pour commencer:

1. **wsl -l -v**:
   - Cette commande affiche une liste de toutes les distributions WSL (Windows Subsystem for Linux) installées sur votre système Windows, ainsi que leur état et leur version.
   - **Options**:
     - `-l` ou `--list` : Affiche la liste des distributions WSL installées.
     - `-v` ou `--verbose` : Affiche des informations supplémentaires, y compris la version de chaque distribution WSL.
   - **Exemple d'utilisation**:
     ```
     wsl -l -v
     ```
   - Cette commande affiche la liste des distributions WSL installées, leur état (Running ou Stopped) et leur version.

2. **wsl -d Ubuntu**:
   - Cette commande permet de démarrer une instance WSL spécifique directement en ouvrant un terminal à l'intérieur de cette instance.
   - **Options**:
     - `-d <distribution>` ou `--distribution <distribution>` : Spécifie la distribution WSL à démarrer.
   - **Exemple d'utilisation**:
     ```
     wsl -d Ubuntu
     ```
   - Cette commande ouvre un terminal directement dans l'instance WSL d'Ubuntu en cours d'exécution.

Ces commandes sont utiles pour gérer et interagir avec les distributions WSL installées sur votre système Windows. 
Elles peuvent vous aider à afficher des informations sur les distributions WSL et à démarrer rapidement une instance spécifique pour travailler dans un environnement Linux.